.. figure:: http://iws-public.s3.amazonaws.com/Media/PyWebRunner.png
   :alt: PyWebRunner

   PyWebRunner

A supercharged Python wrapper for Selenium

|Build Status| |PyPI version|

Documentation
-------------

Full documentation can be located here:
https://intuitivewebsolutions.github.io/PyWebRunner

Uses
----

You could use WebRunner to scrape a website, automate web tasks, or
anything else you could imagine. It is easy to initialize and use. It's
also compatible with
`BrowserStack <https://www.browserstack.com/automate/python>`__ using
the command\_executor and remote\_capabilities examples on that page.

(Please note that you will need a subscription, username, and API key to
make it work.)

Installing
----------

.. code:: bash

    pip install PyWebRunner

Basic Examples
--------------

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
------------

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

Advanced YAML Features
~~~~~~~~~~~~~~~~~~~~~~

YAML supports the use of the fake-factory library (if it is installed)
as well as evals and python function calls. Though the YAML is not
intended as a complete replacement for Python scripts, this does enable
some pretty flexible scripts to run.

You might be asking yourself, what's the purpose of parsing YAML like
this if you can just write Python and have access to all these things by
default?

The answer is that I wanted a way to write purely data-driven, front-end
tests. The benefits could be summarized as:

-  It makes it possible to write a single loader script that grabs all
   the YAML files in a folder and runs them one at a time (or in
   parallel).
-  The tests themselves could be served up from a single, remote
   web-server.
-  Tests could be written by non-programmers with minimal training and
   effort.
-  GUI tools can easily be created to write tests/automated tasks
   without needing any programming knowledge.

Consider the following example of registering an account:

.. code:: yaml

    # Go to the page.
    - go: https://somesite/page.html
    # Click the register link.
    - click: "#register"
    # Wait for the registration form.
    - wait_for_presence: "#email"
    # Set the email field to a freshly-generated fake email address:
    - set_value:
      - "#email"
      - (( fake-email ))
    # Create a fake password string.
    - set_value:
      - "#password"
      - (( fake-password ))
    # Reference the fake password we already generated.
    - set_value:
      - "#password-verify"
      - (( vars|password ))
    # Click the register button.
    - click: "#register"
    # Wait for the redirect and the confirmation div.
    - wait_for_presence: "#confirmation-div"
    # Assert that the registration was successful.
    - assert_text_in_page: Your registration was successful!

**Fake** **Data**

This example makes use of the fake-factory/faker library to generate a
fake email address as well as a password. Any data that is created using
the (( )) syntax is automatically assigned to a variable list for
reference later.

**Installing** **Faker**

To install prior to September 15th, 2016: ``pip install fake-factory``

To install after September 15th, 2016: ``pip install faker``

fake-factory / faker need only be installed for the YAML to support
``(( fake-* ))`` tags.

``*`` can be any of the methods on the faker class. This list is
extensive and is under active development. For more information, go to
the fake-factory website:

https://faker.readthedocs.io/en/latest/

**((** **special** **))**

Items enclosed in double parentheses (( )) will be parsed in this
special way upon the execution of the script.

**Examples**

.. code:: yaml

    - include: basic_setup.yml
    - import: random.randint
    - set_value:
      - "#someinput"
      - (( randint|1,2 ))

The previous example will import random.randint and use it to generate a
value of either 1 or 2 and insert it into the #someinput element.

--------------

.. code:: yaml

    - import: random.choice
    - set_value:
      - "#someinput"
      - (( choice|['frog','cat','bird'] ))

As you can see, the choice function doesn't take positional arguments
like the randint function does. It needs a list of options.

--------------

What happens when we run a function more than once and we need to
reference the second or third output?

.. code:: yaml

    - import: random.choice
    - set_value:
      - "#someinput-a"
      - (( choice|['frog','cat','bird'] )) # bird
    - set_value:
      - "#someinput-b"
      - (( choice|['frog','cat','bird'] )) # cat
    - set_value:
      - "#someinput-c"
      - (( choice|['frog','cat','bird'] )) # cat (again)
    - assert_value_of_element:
      - "#someinput-a"
      - (( vars|choice )) # The "choice" array. Defaults to index 0.
    - assert_value_of_element:
      - "#someinput-b"
      - (( vars|choice|1 )) # The "choice" array index 1.
    - assert_value_of_element:
      - "#someinput-c"
      - (( vars|choice|2 )) # The "choice" array index 2.

--------------

OK, how about values on the page itself? Is there any way to obtain and
reference them from inside a YAML WebRunner script?

.. code:: yaml

    - value_of: "#my-input-element" # Set the value.
    - set_value:
      - "#someinput-a"
      - (( vars|value_of|0 )) # Use the value at index 0.
    - text_of: "#my-div-element" # Set the text to a variable.
    - set_value:
      - "#someinput-b"
      - (( vars|text_of|0 )) # Use the text value at index 0.

BrowserStack example:
---------------------

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
---------

WebTester inherits WebRunner so it has all the same methods that
WebRunner has but it adds some additional methods that are useful for
testing.

Testing Asserts
~~~~~~~~~~~~~~~

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
.. |PyPI version| image:: https://badge.fury.io/py/PyWebRunner.svg
   :target: https://badge.fury.io/py/PyWebRunner
