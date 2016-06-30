import sys
from datetime import datetime
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


class TestForms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = HTTPTestServer(("", 5000), Handler)
        httpd_thread = threading.Thread(target=httpd.serve_forever)
        httpd_thread.setDaemon(True)
        httpd_thread.start()

        cls.wt = WebTester()
        cls.wt.start()

    @classmethod
    def tearDownClass(cls):
        cls.wt.stop()

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.wt.screenshot(test_method_name + "-" + now + ".png")

    def test_fill_form(self):
        self.wt.goto('/tests/html/forms.html')
        self.wt.wait_for_visible('#textfield')
        self.wt.set_value('#textfield', 'This is a test')
        self.wt.set_value('#selectfield', '3')
        assert self.wt.get_value('#textfield') == 'This is a test'
        assert self.wt.get_value('#selectfield') == '3'
        # We have to clear the text field when using fill
        self.wt.clear('#textfield')
        self.wt.fill({
            '#textfield': 'Booya!',
            '#selectfield': 'Four'
        })
        assert self.wt.get_value('#textfield') == 'Booya!'
        assert self.wt.get_value('#selectfield') == '4'
        self.wt.set_value('#textfield', 'No clear needed')
        assert self.wt.get_value('#textfield') == 'No clear needed'

    def test_screenshot(self):
        import os.path
        path = '/tmp/selenium-screenshot.png'
        self.wt.screenshot()
        assert os.path.isfile(path)
        assert os.path.getsize(path) > 0
