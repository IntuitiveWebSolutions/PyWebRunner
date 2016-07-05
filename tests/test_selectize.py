from HttpBase import HttpBase


class TestSelectize(HttpBase):

    def test_set_selectize_basic(self):
        self.wt.goto('/tests/html/selectize.html')
        select_el = '#testSelectize'
        test_value = 'Option 2'
        self.wt.wait_for_visible(select_el + ' + .selectize-control')
        self.wt.set_selectize(select_el, test_value)
        assert self.wt.get_value(select_el) == test_value

    def test_set_selectize_async(self):
        self.wt.goto('/tests/html/selectize.html?async=true')
        select_el = '#testSelectize'
        test_value = 'Option 3'
        self.wt.wait_for_visible(select_el + ' + .selectize-control')
        self.wt.set_selectize(select_el, test_value)
        assert self.wt.get_value(select_el) == test_value
