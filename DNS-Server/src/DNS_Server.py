import threading
import socket
import socketserver
from dnslib import DNSRecord,QTYPE
import dnslib

class Handler(socketserver.BaseRequestHandler):    
    def handle(self):        
        request_data = self.request[0]
        client_socket = self.request[1]
        #内部搜索
        d=DNSRecord.parse(request_data)
        qname=str(d.q.qname)
        qid=d.header.id
        search=cache.get(qname)
        print(qname)
        if search:
            ret=d.reply()
            # 不良网站
            if search=="0.0.0.0":
                ret.add_answer(dnslib.RR(qname,QTYPE.TXT,rdata=dnslib.TXT(warning)))
            else:
                ret.add_answer(dnslib.RR(qname,rdata=dnslib.A(search)))
            ret.header.id=qid
            client_socket.sendto(bytes(ret.pack()), self.client_address)
        else:
            # 将请求转发到 外部 DNS
            redirect_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            redirect_socket.sendto(request_data, ('202.38.64.56', 53))
            response_data, address = redirect_socket.recvfrom(8192)
            # 将外部响应响应给客户
            client_socket.sendto(response_data, self.client_address)

    
class Server(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":
    # 添加外部的ip地址
    f=open("./ip.txt",'r')
    ip=[]
    for a in f.readlines():
        if len(a)>=2:
            ip.append(a.strip().split(" "))
    
    cache={}
    for i in ip:
        cache[i[1]+'.']=i[0]

    cache["abc.com."]="1.2.3.4"
    cache["wrong.com."]="0.0.0.0"
    cache["drdh.com."]="185.199.109.153"
    # 不良网站警告信息
    warning="illegal website"
   
    # ip需换成自己电脑的ip
    localIP="114.214.175.45"
    server = Server((localIP, 53), Handler)
    with server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print('The DNS server is running at %s ...',localIP)
        server_thread.join()