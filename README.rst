.. figure:: http://iws-public.s3.amazonaws.com/Media/PyWebRunner.png
   :alt: PyWebRunner

   PyWebRunner

A supercharged Python wrapper for Selenium

|Build Status|

Documentation
~~~~~~~~~~~~~

Full documentation can be located here:
https://intuitivewebsolutions.github.io/PyWebRunner

Uses
~~~~

You could use WebRunner to scrape a website, automate web tasks, or
anything else you could imagine. It is easy to initialize and use. It's
also compatible with
`BrowserStack <https://www.browserstack.com/automate/python>`__ using
the command\_executor and remote\_capabilities examples on that page.

(Please note that you will need a subscription, username, and API key to
make it work.)

Installing
~~~~~~~~~~

.. code:: bash

    pip install PyWebRunner

Basic Examples
~~~~~~~~~~~~~~

.. code:: python

    # Import WebRunner if you aren't going to assert anything.
    # WebTester is a sub-class of WebRunner
    from PyWebRunner import WebRunner

    # Running headless FireFox is the default.
    wr = WebRunner() # Defaults to xvfb=True, driver=FireFox
    # If xvfb is not installed, it will be bypassed automatically.

    # Start the browser instance.
    wr.start()

    # Navigate to a page.
    wr.go('https://www.google.com/')

    # Fill in a text field.
    wr.set_value('#lst-ib', 'PyWebRunner')
    wr.send_key('#lst-ib', 'ENTER')

    # Click the link based on a (gross) CSS selector.
    wr.click('#rso > div:nth-child(1) > div:nth-child(1) > div > h3 > a')

    # Wait for the page to load.
    wr.wait_for_presence('div.document')

    # Are we there yet?
    wr.is_text_on_page('A helpful wrapper for Selenium') # True

    # Take a screenshot!
    wr.screenshot('/tmp/screenshot1.png')

    # Stop the browser instance.
    wr.stop()

YAML Scripts
~~~~~~~~~~~~

PyWebRunner supports running YAML scripts and includes the ``webrunner``
command.

Let's say we made a YAML script for the above example and we called it
``script.yml``

.. code:: yaml

    - go: https://www.google.com/
    - set_value:
      - "#lst-ib"
      - PyWebRunner
    - send_key:
      - "#lst-ib"
      - "ENTER"
    - click: "#rso > div:nth-child(1) > div:nth-child(1) > div > h3 > a"
    - wait_for_presence: div.document
    - assert_text_on_page: A helpful wrapper for Selenium
    - screenshot: /tmp/screenshot1.png

We can run it like so:

.. code:: bash

    webrunner script.yml

...and it will behave identically to the Python-based example above.

BrowserStack example:
~~~~~~~~~~~~~~~~~~~~~

This library also has first-class support for BrowserStack. Using it is
not much different than the examples above.

.. code:: python

    from PyWebRunner import WebRunner
    # Change any of these values to valid ones.
    desired = {
        'browser': 'Edge',
        'browser_version': '13.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1440x900'
    }
    # Make sure you plug in your own USERNAME and API_KEY values here.
    wr = WebRunner(desired_capabilities=desired,
                   command_executor='http://USERNAME:API_KEY@hub.browserstack.com:80/wd/hub',
                                 driver='Remote')
    wr.start()
    wr.go('http://google.com')
    # ... Etc.

--------------

Testing
-------

WebTester
~~~~~~~~~

WebTester inherits WebRunner so it has all the same methods that
WebRunner has but it adds some additional methods that are useful for
testing.

Testing Asserts
^^^^^^^^^^^^^^^

-  assert\_alert\_not\_present
-  assert\_alert\_present
-  assert\_checked
-  assert\_element\_contains\_text
-  assert\_element\_has\_class
-  assert\_element\_not\_has\_class
-  assert\_exists
-  assert\_found
-  assert\_not\_checked
-  assert\_not\_found
-  assert\_not\_visible
-  assert\_text\_in\_element
-  assert\_text\_in\_elements
-  assert\_text\_in\_page
-  assert\_text\_not\_in\_page
-  assert\_url
-  assert\_value\_of\_element
-  assert\_visible

.. |Build Status| image:: https://travis-ci.org/IntuitiveWebSolutions/PyWebRunner.svg?branch=master
   :target: https://travis-ci.org/IntuitiveWebSolutions/PyWebRunner
