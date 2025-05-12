from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")
def main():
    server = HTTPServer(('', 8888), MyHandler)
    print("Started WebServer 8888.")
    print("Press ^C to quit.")
    server.serve_forever()
    
if __name__ == "__main__":
    main()