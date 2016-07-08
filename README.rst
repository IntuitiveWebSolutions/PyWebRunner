WebRunner
=========

A helpful wrapper for Selenium

|Build Status|

Full documentation can be located here:
https://intuitivewebsolutions.github.io/PyWebRunner

You could use WebRunner to scrape a website, automate web tasks, or
anything else you could imagine. It is easy to initialize and use. It's
also compatible with
`BrowserStack <https://www.browserstack.com/automate/python>`__ using
the command\_executor and remote\_capabilities examples on that page.
Please note that you will need a subscription, username, and API key to
make it work.

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

    wr.stop()

Let's say you wanted to do some things in FireFox and then switch to
Chrome. You could do it like so:

.. code:: python

    wr = WebRunner()

    wr.start()

    # Do things...

    wr.stop()

    # Change the browser. This is accomplished by setting the property directly at present.
    wr.browser = "Chrome"

    # You could also choose to run headlessly if you wanted:
    wr.xvfb = True

    wr.start()

    # Do things in Chrome now.

    wr.stop()

The main utility of the WebRunner class is its ability to shortcut many
of the most common tasks that you would need to automate the interaction
with a web page.

The most critical of these would be to open a webpage.

.. code:: python

    wr.go('http://someaddress.here/page.html')

Once we have a page open we can interact with it in various ways. The
methods in this class are well-documented so fully explaining them all
is outside of the scope of this guide. I strongly recommend that you
look at the docstrings for all the methods and see for yourself how to
interact with them.

Here is a list of available methods in WebRunner with basic explanations
about what they do:

Browser control:
~~~~~~~~~~~~~~~~

-  start
-  stop
-  refresh\_page
-  forward
-  back
-  go
-  current\_url
-  js

Scrolling
^^^^^^^^^

-  scroll\_browser

Misc
^^^^

-  get\_page\_source
-  screenshot
-  save\_page\_source

Waiting
^^^^^^^

-  wait\_for\_url
-  wait\_for\_title
-  wait\_for\_js

Finding
^^^^^^^

-  is\_text\_on\_page

Element Methods
~~~~~~~~~~~~~~~

Scrolling
^^^^^^^^^

-  scroll\_to\_element

Selecting
^^^^^^^^^

-  find\_element
-  find\_elements
-  get\_element
-  get\_elements
-  get\_text
-  get\_value
-  get\_texts

Waiting
^^^^^^^

-  wait\_for
-  wait\_for\_visible
-  wait\_for\_invisible
-  wait\_for\_all\_invisible
-  wait\_for\_clickable
-  wait\_for\_selected
-  wait\_for\_presence
-  wait\_for\_opacity
-  wait\_for\_text
-  wait\_for\_value
-  wait\_for\_ko

Interaction
^^^^^^^^^^^

-  click
-  click\_all
-  hover
-  send\_key
-  clear

Forms
^^^^^

-  fill
-  fill\_form
-  set\_value
-  set\_selectize
-  set\_select\_by\_value
-  set\_select\_by\_text

.. code:: python

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

BrowserStack example:
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from PyWebRunner import WebRunner
    desired = {
        'browser': 'Edge',
        'browser_version': '13.0',
        'os': 'Windows',
        'os_version': '10',
        'resolution': '1440x900'
    }
    wr = WebRunner(desired_capabilities=desired,
                   command_executor='http://USERNAME:API_KEY@hub.browserstack.com:80/wd/hub',
                                 driver='Remote')
    wr.start()
    wr.go('http://google.com')
    wr.set_value('#lst-ib', 'PyWebRunner')

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

Helpers
~~~~~~~

-  goto
-  wait

Testing Asserts
~~~~~~~~~~~~~~~

-  assert\_element\_has\_class
-  assert\_not\_found
-  assert\_not\_visible
-  assert\_exists
-  assert\_alert\_present
-  assert\_text\_in\_page
-  assert\_visible
-  assert\_text\_not\_in\_page
-  assert\_url
-  assert\_alert\_not\_present
-  assert\_text\_in\_elements
-  assert\_text\_in\_element
-  assert\_found
-  assert\_element\_contains\_text
-  assert\_value\_of\_element
-  assert\_element\_not\_has\_class

.. |Build Status| image:: https://travis-ci.org/IntuitiveWebSolutions/PyWebRunner.svg?branch=master
   :target: https://travis-ci.org/IntuitiveWebSolutions/PyWebRunner
