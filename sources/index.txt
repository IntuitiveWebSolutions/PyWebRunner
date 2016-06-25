WebRunner
=========

A helpful wrapper for Selenium

Installation
************

.. code-block:: bash

    pip install PyWebRunner

Hello World!
============

.. code:: python

    from PyWebRunner import WebRunner

    # Running headless FireFox is the default.
    wr = WebRunner() # Defaults to xvfb=True, driver=FireFox
    # If xvfb is not installed, it will be bypassed automatically.

    # If you explicitly don't want headless operation:
    wr = WebRunner(xvfb=False)

Once we've initialized WebRunner, we still need to kick off the browser.
I've made this a manual step so that it is easy to start and stop
different browsers using the same WebRunner instance if desired.

.. code:: python

    # Start your engines...

    wr.start()

    # DO SOME STUFF
    print(wr.current_url())
    # outputs 'http://someaddress.here/page.html'

    wr.click('#some-button') # Clicks a button.

    wr.js('console.log("I am executing JS on the page!");')

    elem = wr.find_element('#my-id') # Returns a selenium element object

    elems = wr.find_elements('.some-class') # Returns a list of selenium element objects

    form_data = {
        '#username': 'person',
        '#password': 'somepass'
    }
    wr.fill(form_data) # Fills a form. Takes a dict of CSS keys and values.

    wr.screenshot('/tmp/screenshot1.png')

    wr.stop()

As you can see, there is almost no reason to ever interact with the
selenium browser object directly. This is by design. If you ever find
yourself needing to, it means that you have uncovered a need that was
unanticipated by the initial design of this utility.

If you are reading this, you are a programmer so it would be nice if you
made the method you require and sent a PR. The more people use and
develop this framework, the better it will become.

So even though I don't recommend using it, you still have access to the
selenium browser object.

.. code:: python

    wr.browser.find_elements_by_id('#some-id') # Use wr.find_element instead.

--------------

WebTester
=========

WebTester inherits WebRunner so it has all the same methods that
WebRunner has but it adds some additional methods that are useful for
testing.

Documentation
*************

Wrapper
=======

.. autoclass:: PyWebRunner.WebRunner
    :members:

.. autoclass:: PyWebRunner.WebTester
    :members:
