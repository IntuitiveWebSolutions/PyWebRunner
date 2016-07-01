import unittest
import threading
from PyWebRunner import WebTester
from six.moves import SimpleHTTPServer
try:
    import SocketServer
except ImportError:
    import socketserver as SocketServer


class HTTPTestServer(SocketServer.TCPServer):
    allow_reuse_address = True


class HttpBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        cls.httpd = HTTPTestServer(("", 5000), Handler)
        cls.httpd_thread = threading.Thread(target=cls.httpd.serve_forever)
        cls.httpd_thread.setDaemon(True)
        cls.httpd_thread.start()

        cls.wt = WebTester()
        cls.wt.start()

    @classmethod
    def tearDownClass(cls):
        cls.wt.stop()
        cls.httpd.shutdown()
        cls.httpd_thread.join()
