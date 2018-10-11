`ip link`查看本机的ip地址`114.214.176.57`每次不一样

编辑`/etc/resolv.conf`使DNS服务器为上面的地址

使用`create_ap`创建热点`sudo create_ap wlp9s0 enp0s20f0u3 Arch archwifi`在另一个电脑上连接，然后修改DNS服务器为上面的ip地址，就可以正常查询了



[DNS 介绍与粗实现](http://www.cnblogs.com/dongkuo/p/6714071.html); [相关代码](https://github.com/dongkuo/dns-server)

[DNS 使用dnslib案例](http://www.isnowfy.com/introduction-to-gevent/); [相关代码](https://github.com/isnowfy/dns)

[dnslib 介绍](https://bitbucket.org/paulc/dnslib/)

