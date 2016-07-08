from HttpBase import HttpBase


class TestForms(HttpBase):

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

