__author__ = 'Samuel'

import BaseHTTPServer
from multiprocessing import Process
from urlparse import urlparse, parse_qs

class WebServer(Process):

    def __init__(self, queue, pipe):
        Process.__init__(self)
        self.queue = queue
        self.pipe = pipe

    def return_name(self):
        return "Process returned %s" % self.name

    def run(self):
        server_class=BaseHTTPServer.HTTPServer
        handler_class=RequestHandler

        server_address = ('', 8080)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)

