import socket,threading

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

    if '/index' == url:
        # 给出响应
        conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
        conn.send("<h1>这是首页!</h1>".encode(encoding="utf-8"))
    elif '/detail' == url:
        # 给出响应
        conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
        conn.send("<h1>这是详情页!</h1>".encode(encoding="utf-8"))
    else:
        # 给出响应
        conn.send("HTTP/1.1 404 Not Found \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
        conn.send("<h1>Page Not Found </h1>".encode(encoding="utf-8"))

    # 关闭连接
    conn.close()


def main():
    s = socket.socket()
    s.bind(('127.0.0.1', 8006))
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