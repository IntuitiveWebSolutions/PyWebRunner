import os
import sys
import unittest
import wait

from subprocess import Popen
from PyWebRunner import WebTester

class Server(object):
    """
    A server class for running a SimpleHTTPServer as a process.
    """

    port = 8000
    env = os.environ.copy()
    root = os.path.join(os.path.dirname(__file__), os.pardir)
    process = None
    extra_verbose = False
    silence = open(os.devnull, 'w')

    def start(self):
        if sys.version_info >= (3, 0):
            module = 'http.server'
        else:
            module = 'SimpleHTTPServer'
        command = ['python', '-m', module]

        if self.extra_verbose:
            self.process = Popen(command, cwd=self.root, env=self.env)
        else:
            self.process = Popen(command, cwd=self.root, stdout=self.silence, stderr=self.silence, env=self.env)

        wait.tcp.open(self.port)

    def stop(self):
        try:
            self.process.kill()
        except:
            print("Could not kill server process.")
            # Try to kill this process but don't fail completely if we can't
            # for some reason.
            pass

    def restart(self):
        self.stop()
        self.start()

class HttpBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = Server()
        cls.server.start()

        browser = os.environ.get('BROWSER', 'chrome')
        cls.wt = WebTester(base_url='http://127.0.0.1:8000/', driver='chrome-headless', timeout=10)
        cls.wt.start()

    @classmethod
    def tearDownClass(cls):
        cls.wt.stop()
        cls.server.stop()
