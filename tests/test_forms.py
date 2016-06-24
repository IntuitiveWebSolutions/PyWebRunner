import unittest
import threading
from PyWebRunner import WebTester
import SimpleHTTPServer
import SocketServer


class TestForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", 5000), Handler)
        httpd_thread = threading.Thread(target=httpd.serve_forever)
        httpd_thread.setDaemon(True)
        httpd_thread.start()

        cls.wt = WebTester()
        cls.wt.start()

    @classmethod
    def tearDownClass(cls):
        cls.wt.stop()

    def test_fill_form(self):
        self.wt.goto('/tests/html/forms.html')