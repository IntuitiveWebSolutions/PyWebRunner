from time import sleep
from unittest import TestCase
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from PyWebRunner import WebRunner


class WebTester(WebRunner):
    """
    A class that extends WebRunner and TestCase This class adds
    some additional testing capabilities and shortcuts to
    WebRunner.
    """

    base_url = None

    def __init__(self, base_url='http://127.0.0.1:5000', xvfb=True,
                 driver='Firefox', mootools=False, timeout=90,
                 width=1440, height=1200, root_path='./', firefox_version=46,
                 remote_capabilities='FIREFOX',
                 command_executor='http://127.0.0.1:4444/wd/hub'):
        self.base_url = base_url
        self.root_path = root_path
        WebRunner.__init__(self, xvfb, driver, mootools, timeout, width, height,
                           firefox_version, remote_capabilities, command_executor)

    def wait(self, seconds=500):
        '''
        Sleeps for some amount of time.

        Parameters
        ----------

        seconds: int
            Seconds to sleep for.

        '''
        # You probably shouldn't use this for anything
        # real in tests. I use this for pausing execution.
        sleep(seconds)

    def goto(self, url, wait_for_visible=None, wait_for_presence=None):
        '''
        Shortcut to go to a relative path of the base_url. Useful for navigation
        in the same website.

        url: str
            Relative url to go to.

        wait_for_visible: str
            CSS selector to wait for visibility of after navigation.

        wait_for_presence: str
            CSS Selector to wait for presence of after navigation.

        '''
        self.go('{}{}'.format(self.base_url, url))

        if wait_for_visible:
            self.wait_for_visible(wait_for_visible)

        if wait_for_presence:
            self.wait_for_presence(wait_for_presence)

    def assert_element_has_class(self, selector, cls, wait_for='presence', **kwargs):
        '''
        Asserts the element obtained from a given CSS selector has specified class.
        Parameters
        ----------
        selector: str
            Any valid css selector
        class: str
            The class to check for
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*
        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        el = self.get_element(selector)
        assert cls in el.get_attribute('class')

    def assert_element_not_has_class(self, selector, cls, wait_for='presence', **kwargs):
        '''
        Asserts the element obtained from a given CSS selector does not have
        the specified class.
        Parameters
        ----------
        selector: str
            Any valid css selector
        class: str
            The class to check for
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*
        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        el = self.get_element(selector)
        assert cls not in el.get_attribute('class')

    def assert_exists(self, selector):
        '''
        Asserts that the element found from a given CSS selector exists on the page.

        Parameters
        ----------
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.

        '''
        exists = True
        try:
            self.get_element(selector)
        except NoSuchElementException:
            exists = False

        msg = 'An element could not be found for the selector: {}'.format(selector)
        assert exists == True, msg

    def assert_url(self, url):
        '''
        Asserts that the current URL is equal to a specific value.

        Parameters
        ----------
        url: str
            The URL to assert.

        '''
        current_url = self.browser.current_url
        assert current_url == url, 'The URL was: {0} instead of {1}'.format(current_url, url)

    def assert_text_in_page(self, text):
        '''
        Asserts that the text exists on the page.

        Parameters
        ----------
        text: str
            Text to search for.

        '''
        assert self.is_text_on_page(text) == True, '{} was not present in the source code.'.format(text)

    def assert_text_not_in_page(self, text):
        '''
        Asserts that the text does not exist on the page.

        Parameters
        ----------
        text: str
            Text to search for.

        '''
        assert self.is_text_on_page(text) == False, '{} was present in the source code.'.format(text)

    def assert_not_visible(self, selector):
        '''
        Asserts that the element found from a given CSS selector
        is NOT visible on the page.

        Parameters
        ----------
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.

        '''
        self.wait_for_presence(selector)

        elem = self.get_element(selector)
        assert elem.is_displayed() == False, 'The {} element was visible.'.format(selector)

    def assert_visible(self, selector, **kwargs):
        '''
        Asserts that the element found from a given CSS selector is visible on the page.

        Parameters
        ----------
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.
        kwargs:
            passed on to wait_for_presence

        '''
        self.wait_for_presence(selector, **kwargs)

        elem = self.get_element(selector)
        assert elem.is_displayed() == True, 'The {} element was not visible.'.format(selector)

    def assert_value_of_element(self, selector, value, wait_for='presence', **kwargs):
        '''
        Asserts the value of the element obtained from a given CSS selector.

        Parameters
        ----------
        value: str
            The string to look for. Must be exact.
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*

        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        sval = self.get_value(selector)
        assert value == sval

    def assert_text_in_elements(self, selector, text, wait_for='presence', **kwargs):
        '''
        Asserts that the text can be found inside of the elements
        obtained from a given CSS selector.

        Parameters
        ----------
        text: str
            The string to look for. Must be exact.
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*

        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        texts = self.get_texts(selector)
        assert text in texts, 'The string "{}" was not found in the selector: {}'.format(text, selector)

    def assert_text_in_element(self, selector, text, wait_for='presence', **kwargs):
        '''
        Asserts that the text can be found inside of the element
        obtained from a given CSS selector.

        Parameters
        ----------
        text: str
            The string to look for. Must be exact.
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*

        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        element_value = self.get_text(selector)
        assert any([text in element_value, text == element_value]) == True, "{} not in or equal to {}".format(text, element_value)

    def assert_element_contains_text(self, selector, text, wait_for='presence', **kwargs):
        '''
        Asserts that the text can be found inside of the element
        obtained from a given CSS selector.

        Parameters
        ----------
        text: str
            The string to look for. Must be exact.
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.
        wait_for: str
            'presence' or 'visible' - defaults to presence
        kwargs:
            passed on to wait_for_*
        '''
        self._wait_for_presence_or_visible(selector, wait_for, **kwargs)

        text_value = self.get_text(selector)
        assert text in text_value, "{} in in {}".format(text, text_value)

    def assert_not_found(self, selector):
        '''
        Asserts that the element cannot be found.

        Parameters
        ----------
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.

        '''
        elem = self.find_element(selector)
        assert elem is None, '{} was unexpectedly found on the page'.format(selector)

    def assert_found(self, selector):
        '''
        Asserts that the element can be found.

        Parameters
        ----------
        selector: str
            A CSS selector to search for. This can be any valid CSS selector.

        '''
        elem = self.find_element(selector)
        assert elem is not None, '{} was not found on the page'.format(selector)

    def assert_alert_present(self):
        '''
        Asserts that an alert exists.

        '''
        alert = self.browser.switch_to_alert()
        msg = 'An alert was not present but was expected.'

        try:
            atext = bool(alert.text)
        except NoAlertPresentException:
            atext = False

        assert atext == True, msg

    def assert_alert_not_present(self):
        '''
        Asserts that an alert does not exist.

        '''
        def check_text(alert):
            bool(alert.text)

        alert = self.browser.switch_to_alert()
        present = False
        try:
            present = bool(alert.text)
        except NoAlertPresentException:
            pass
        assert present == False
