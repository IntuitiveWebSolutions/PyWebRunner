import sys
from datetime import datetime

from HttpBase import HttpBase


class TestForms(HttpBase):

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
        self.wt.wait_for_text_in_value('#textfield', 'This is a test')
        self.wt.wait_for_text_in_value('#selectfield', '3')
        assert self.wt.get_value('#textfield') == 'This is a test'
        assert self.wt.get_value('#selectfield') == '3'
        # We have to clear the text field when using fill
        self.wt.clear('#textfield')
        self.wt.fill({
            '#textfield': 'Booya!',
            '#selectfield': 'Four'
        })
        self.wt.wait_for_text_in_value('#textfield', 'Booya!')
        self.wt.wait_for_text_in_value('#selectfield', '4')
        assert self.wt.get_value('#textfield') == 'Booya!'
        assert self.wt.get_value('#selectfield') == '4'
        self.wt.set_value('#textfield', 'No clear needed')
        self.wt.wait_for_text_in_value('#textfield', 'No clear needed')
        assert self.wt.get_value('#textfield') == 'No clear needed'

        # Test set_values:

        # Dict:
        self.wt.set_values({
            '#textfield': 'AAAAAAAA',
            '#selectfield': '5'
        })
        self.wt.wait_for_text_in_value('#textfield', 'AAAAAAAA')
        self.wt.wait_for_text_in_value('#selectfield', '5')
        assert self.wt.get_value('#textfield') == 'AAAAAAAA'
        assert self.wt.get_value('#selectfield') == '5'

        # List of list:
        self.wt.set_values([
            ['#textfield', 'BBBBBBBB'],
            ['#selectfield', '6']
        ])
        self.wt.wait_for_text_in_value('#textfield', 'BBBBBBBB')
        self.wt.wait_for_text_in_value('#selectfield', '6')
        assert self.wt.get_value('#textfield') == 'BBBBBBBB'
        assert self.wt.get_value('#selectfield') == '6'

        # List of Mix:
        self.wt.set_values([
            ('#textfield', 'CCCCCCCC'),
            {'#selectfield': '7'}
        ])
        self.wt.wait_for_text_in_value('#textfield', 'CCCCCCCC')
        self.wt.wait_for_text_in_value('#selectfield', '7')
        assert self.wt.get_value('#textfield') == 'CCCCCCCC'
        assert self.wt.get_value('#selectfield') == '7'

        # Tuple of tuple:
        self.wt.set_values((
            ('#textfield', 'DDDDDDDD'),
            ('#selectfield', '8')
        ))
        self.wt.wait_for_text_in_value('#textfield', 'DDDDDDDD')
        self.wt.wait_for_text_in_value('#selectfield', '8')
        assert self.wt.get_value('#textfield') == 'DDDDDDDD'
        assert self.wt.get_value('#selectfield') == '8'
