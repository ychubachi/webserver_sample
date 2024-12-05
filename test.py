import http.server
import socketserver
import datetime

class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write('GETメソッドを実装'.encode())

        # 現在の日付と時刻を取得
        now = datetime.datetime.now()
        # 結果を表示
        print("現在の時刻:", now)
        self.wfile.write(now.strftime("%Y-%m-%d %H:%M:%S").encode())

PORT = 8000
# Handler = http.server.SimpleHTTPRequestHandler
Handler = CustomHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()

