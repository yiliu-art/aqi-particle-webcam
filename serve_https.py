import http.server
import ssl
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8443
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server = http.server.HTTPServer(("0.0.0.0", PORT), http.server.SimpleHTTPRequestHandler)
server.socket = context.wrap_socket(server.socket, server_side=True)
print(f"Serving HTTPS on 0.0.0.0:{PORT}")
server.serve_forever()
