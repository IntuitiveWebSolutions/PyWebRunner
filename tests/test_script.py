import sys
from datetime import datetime

from HttpBase import HttpBase


class TestScript(HttpBase):

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.wt.screenshot(test_method_name + "-" + now + ".png")

    def test_script(self):
        self.wt.command_script(filepath='tests/script.yml', errors=False, verbose=True)
