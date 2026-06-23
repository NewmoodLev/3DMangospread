import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # serve orchard_3d.html at root
        if path in ('/', ''):
            path = '/orchard_3d.html'
        return super().translate_path(path)

    def log_message(self, fmt, *args):
        pass  # suppress access logs

port = int(os.environ.get('PORT', 8080))
print(f'MangoMap 3D serving on port {port}')
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
