"""
1、导包
2、实例化scoket对象
3、绑定ip 端口
4、监听
5、接收请求
6、处理请求并给出响应
7、关闭连接
"""
import socket,threading

from urls import *

def handler_conn(conn):
    # 接收客户端的数据
    request = []
    data = conn.recv(1024)

    data = data.decode(encoding='utf-8')
    print('客户端的数据：%s' % data)

    # 获取url地址
    # GET /detail HTTP/1.1
    request_line = data.split('\r\n')[0]
    url = request_line.split(' ')[1]
    print('请求的url地址是：%s' % url)

    method = request_line.split(' ')[0]
    # 接收get参数
    param_dict = {}

    if 'GET' == method:
        urls = url.split('?')
        if len(urls) > 1:
            url = urls[0]
            # key1=1&key2=2&key3=3
            params = urls[1]
            params_arr = params.split('&')
            for param in params_arr:
                # param--->key1=1
                param_dict[param.split('=')[0]] = param.split('=')[1]
        print('请求参数：%s' % param_dict)

    for urlpattern in urlpatterns:
        u = urlpattern[0]
        if url == u:
            func = urlpattern[1]
            func(conn, param_dict)
            break
    else:
        page_not_found(conn)


    # 关闭连接
    conn.close()


def main():
    s = socket.socket()
    s.bind(('127.0.0.1', 8001))
    s.listen(5)
    print("服务器启动：%s:%d.." % ('127.0.0.1', 8001))
    while True:
        conn, addr = s.accept()
        print("与%s:%s建立连接" % addr)
        # 创建子线程
        t = threading.Thread(target=handler_conn, args=(conn,))
        t.start() # 开启线程


if __name__ == '__main__':
    main()