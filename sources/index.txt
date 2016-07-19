Elemental
=========

A helpful wrapper for Selenium

Installation
************

.. code-block:: bash

    pip install WebElemental

Hello World!
============

.. code:: python

    from WebElemental import Elemental

    # Running headless FireFox is the default.
    elemental = Elemental() # Defaults to xvfb=True, driver=FireFox
    # If xvfb is not installed, it will be bypassed automatically.

    # If you explicitly don't want headless operation:
    elemental = Elemental(xvfb=False)

Once we've initialized Elemental, we still need to kick off the browser.
I've made this a manual step so that it is easy to start and stop
different browsers using the same Elemental instance if desired.

.. code:: python

    # Start your engines...

    elemental.start()

    # DO SOME STUFF
    print(elemental.current_url())
    # outputs 'http://someaddress.here/page.html'

    elemental.click('#some-button') # Clicks a button.

    elemental.js('console.log("I am executing JS on the page!");')

    elem = elemental.find_element('#my-id') # Returns a selenium element object

    elems = elemental.find_elements('.some-class') # Returns a list of selenium element objects

    form_data = {
        '#username': 'person',
        '#password': 'somepass'
    }
    elemental.fill(form_data) # Fills a form. Takes a dict of CSS keys and values.

    elemental.screenshot('/tmp/screenshot1.png')

    elemental.stop()

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

    elemental.browser.find_elements_by_id('#some-id') # Use elemental.find_element instead.

--------------

TestElemental
=========

TestElemental inherits Elemental so it has all the same methods that
Elemental has but it adds some additional methods that are useful for
testing.

Documentation
*************

Elemental
=========

.. autoclass:: WebElemental.Elemental
    :members:

TestElemental
=========

.. autoclass:: WebElemental.TestElemental
    :members:
