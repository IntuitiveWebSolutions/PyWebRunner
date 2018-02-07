import sys
from datetime import datetime

from HttpBase import HttpBase


class TestMisc(HttpBase):

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.wt.screenshot(test_method_name + "-" + now + ".png")

    def test_misc(self):
        self.wt.goto('/tests/html/misc.html')
        self.wt.wait_for_visible('table')
        self.wt.wait_for_visible('/html/body/table/tbody/tr')
        assert self.wt.count('/html/body/table/tbody/tr') == 3
        assert self.wt.count('/html/body/table/thead/tr') == 1
        assert self.wt.count('/html/body/table/thead/tr/th') == 8
        assert self.wt.count('/html/body/table/tbody/tr/td') == 8 * 3
        assert self.wt.count('li') == 8

    def test_screenshot(self):
        import os.path
        path = '/tmp/selenium-screenshot.png'
        self.wt.screenshot()
        assert os.path.isfile(path)
        assert os.path.getsize(path) > 0

    def test_alert(self):
        self.wt.goto('/tests/html/alert.html')
        self.wt.click('#instaalert')
        self.wt.wait_for_alert()
        assert self.wt.alert_present()
        self.wt.close_alert()

    def test_delayed_alert(self):
        self.wt.goto('/tests/html/alert.html')
        self.wt.click('#delayedalert')
        self.wt.wait_for_alert()
        assert self.wt.alert_present()
        self.wt.close_alert()

    def test_delayed_alert_short_timeout(self):
        import pytest
        from selenium.common.exceptions import TimeoutException

        self.wt.goto('/tests/html/alert.html')
        self.wt.click('#delayedalert')
        with pytest.raises(TimeoutException):
            self.wt.wait_for_alert(timeout=.01)

    # def test_no_js_errors(self):
    #     self.wt.goto('/tests/html/misc.html')
    #     self.wt.assert_js_errors(False)

    # def test_js_errors(self):
    #     self.wt.goto('/tests/html/js_error.html')
    #     self.wt.assert_js_errors(True)
