import http.server
import socketserver

PORT = 9000
handler = http.server.SimpleHTTPRequestHandler

handler.extensions_map.update({
    ".js": "application/javascript"
})

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}")
    print(handler.extensions_map[".js"])
    httpd.serve_forever()