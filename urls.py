def list_user(conn, param_dict=None):
    try:
        conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
            conn.send(content.encode(encoding='utf-8'))

        # conn.send("<h1>这是首页!</h1>".encode(encoding="utf-8"))
    except Exception as e:
        page_not_found(conn, param_dict)

def detail(conn, param_dict=None):
    try:
        conn.send("HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
        id = param_dict.get('id')
        with open('detail.html', 'r', encoding='utf-8') as f:
            content = f.read()
            # 替换参数
            content = content.replace('{{id}}', id)
            conn.send(content.encode(encoding="utf-8"))

        # conn.send("<h1>这是首页!</h1>".encode(encoding="utf-8"))
    except Exception as e:
        page_not_found(conn, param_dict)


def page_not_found(conn, param_dict=None):
    conn.send("HTTP/1.1 404 OK \r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode(encoding="utf-8"))
    conn.send("<h1>Page Not Found</h1>".encode(encoding='utf-8'))


urlpatterns = [
    ('/index', list_user),
    ('/detail', detail),
]


