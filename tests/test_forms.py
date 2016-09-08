import sys
from datetime import datetime

from HttpBase import HttpBase


class TestForms(HttpBase):

    def tearDown(self):
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.wt.screenshot(test_method_name + "-" + now + ".png")

    def test_checked(self):
        self.wt.goto('/tests/html/forms.html')
        self.wt.wait_for_clickable('#checkbox')

        self.wt.click('#checkbox')
        self.wt.assert_checked('#checkbox')

        self.wt.click('#checkbox')
        self.wt.assert_not_checked('#checkbox')

    def test_set_values(self):
        self.wt.goto('/tests/html/forms.html')
        self.wt.wait_for_clickable('#textfield')
        # Test set_values:

        # Dict:
        self.wt.set_values({
            '#textfield': 'AAAAAAAA',
            '#selectfield': '5'
        })
        self.wt.wait_for_text_in_value('#textfield', 'AAAAAAAA')
        assert self.wt.get_value('#textfield') == 'AAAAAAAA'
        assert self.wt.get_value('#selectfield') == '5'

        # List of list:
        self.wt.set_values([
            ['#textfield', 'BBBBBBBB'],
            ['#selectfield', '6']
        ])
        self.wt.wait_for_text_in_value('#textfield', 'BBBBBBBB')
        assert self.wt.get_value('#textfield') == 'BBBBBBBB'
        assert self.wt.get_value('#selectfield') == '6'

        # List of Mix:
        self.wt.set_values([
            ('#textfield', 'CCCCCCCC'),
            {'#selectfield': '7'}
        ])
        self.wt.wait_for_text_in_value('#textfield', 'CCCCCCCC')
        assert self.wt.get_value('#textfield') == 'CCCCCCCC'
        assert self.wt.get_value('#selectfield') == '7'

        # Tuple of tuple:
        self.wt.set_values((
            ('#textfield', 'DDDDDDDD'),
            ('#selectfield', '8')
        ))
        self.wt.wait_for_text_in_value('#textfield', 'DDDDDDDD')
        assert self.wt.get_value('#textfield') == 'DDDDDDDD'
        assert self.wt.get_value('#selectfield') == '8'
