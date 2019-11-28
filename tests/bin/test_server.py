from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        if 'admin-true' in self.path:
            resp = b'{"is_admin": "true"}'
        else:
            resp = b'{"is_admin": "false"}'
        self.wfile.write(resp)

test_server_path = os.path.dirname(os.path.realpath(__file__))
httpd = HTTPServer(('localhost', 4443), SimpleHTTPRequestHandler)

# Uses server.pem, which effectively never expires. 
httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile="{}/server.pem".format(test_server_path)
)
httpd.serve_forever()
