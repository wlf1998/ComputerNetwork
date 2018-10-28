### 计划表

- [ ] 超时处理

  > 由于 UDP 的不可靠性,考虑求助外部 DNS 服务器(中继)却不能得到应答或者收到迟
  > 到应答的情形

- [ ] 调试信息级别 1

  > 输出查询的域名及其对应的 IP 地址
  >
  > 使用默认名字服务器
  >
  > 使用默认配置文件

- [ ] 调试信息级别 2

  >  输出时间坐标,序号,客户端 IP 地址,查询的域名
  >
  > 使用指定的名字服务器
  >
  > 使用指定的配置文件

- [ ] 调试信息级别 3

  >  输出数据报的内容、接收和发送数据包的地址以及端口、查询的 IP 地址及其域名
  >
  > 使用指定的名字服务器
  >
  > 使用默认配置文件

- [ ] 实验报告，占比超高




### 使用

`ip link`查看本机的ip地址`114.214.176.57`每次不一样

编辑`/etc/resolv.conf`使DNS服务器为上面的地址

编辑源码的ip字段

使用`create_ap`创建热点`sudo create_ap wlp9s0 enp0s20f0u3 Arch archwifi`在另一个电脑上连接，然后修改DNS服务器为上面的ip地址，就可以正常查询了



[DNS 介绍与粗实现](http://www.cnblogs.com/dongkuo/p/6714071.html); [相关代码](https://github.com/dongkuo/dns-server)

[DNS 使用dnslib案例](http://www.isnowfy.com/introduction-to-gevent/); [相关代码](https://github.com/isnowfy/dns)

[dnslib 介绍](https://bitbucket.org/paulc/dnslib/)









