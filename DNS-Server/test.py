import threading
import socket
import socketserver
from dnslib import DNSRecord
import dnslib


class Handler(socketserver.BaseRequestHandler):    
    def handle(self):
        #self.cache={}
        # 外部添加
        
        cache["abc.com."]="1.2.3.4"
        
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
            ret.add_answer(dnslib.RR(qname,rdata=dnslib.A(search)))
            #ret.add_answer(dnslib.RR(qname,rdata=dnslib.A("1.2.3.5")))
            ret.header.id=qid
            client_socket.sendto(bytes(ret.pack()), self.client_address)
        else:
            # 将请求转发到 外部 DNS
            redirect_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            redirect_socket.sendto(request_data, ('202.38.64.56', 53))
            response_data, address = redirect_socket.recvfrom(1024)
            # 将外部响应响应给客户
            client_socket.sendto(response_data, self.client_address)

    
class Server(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


if __name__ == "__main__":
    cache={}
    # ip需换成自己电脑的ip
    server = Server(('114.214.176.57', 53), Handler)
    with server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print('The DNS server is running at 114.214.176.57 ...')
        server_thread.join()