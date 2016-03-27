#!/usr/bin/env python3

import argparse, json, os
from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        content_length = self.headers['content-length']
        data = self.rfile.read(int(content_length)).decode('utf-8')
        self.wfile.write(bytes("OK", "ascii"))
        try:
            pid = os.fork()
            if pid == 0:
                request = json.loads(data)
                if request['repository']['url'] == args.repository:
                    if request['ref'].split('/')[2] == args.branch:
                        if request['object_kind'] == args.kind:
                            os.system(args.post)
        except  e:
            sys.exit(1)
    

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

parser = argparse.ArgumentParser(description='Simple GitLab webhook server')
parser.add_argument('--repository')
parser.add_argument('--branch')
parser.add_argument('--kind')
parser.add_argument('--pull')
parser.add_argument('--post')
parser.add_argument('--port', default=5555)

args = parser.parse_args()

run(port=int(args.port))
