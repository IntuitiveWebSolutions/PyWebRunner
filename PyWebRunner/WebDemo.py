from PyWebRunner import WebTester
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import random


class WebDemo(WebTester):
    """
    A class that extends WebRunner and TestCase This class adds
    some additional testing capabilities and shortcuts to
    WebRunner.
    """
    base_url = None

    def __init__(self, **kwargs):
        WebTester.__init__(self, **kwargs)

    def _before(self):
        sleep(random())

    def set_value(self, selector, value, clear=True, blur=True, **kwargs):
        WebTester.set_value(self, selector, value, clear=True,
                            blur=True, typing=True, typing_speed=3, **kwargs)

    def go(self, address):
        WebTester.go(self, address)
        self.wait_for_presence('head')
        self.show_cursor(load_jquery=False)
        self.show_keys(load_jquery=False)

    def move_to(self, selector, click=False):
        WebTester.move_to(self, selector, click)
        self.wait(1)

    def show_cursor(self, load_jquery=False):
        if load_jquery:
            js = '''(function(){
                  var newscript = document.createElement('script');
                     newscript.type = 'text/javascript';
                     newscript.async = true;
                     newscript.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js';
                  (document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(newscript);
                })();
                '''
            self.js(js)

        js = '''var seleniumFollowerImg=document.createElement("img");
                seleniumFollowerImg.setAttribute('src', 'data:image/png;base64,'
                    + 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAQAAACGG/bgAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAA'
                    + 'HsYAAB7GAZEt8iwAAAAHdElNRQfgAwgMIwdxU/i7AAABZklEQVQ4y43TsU4UURSH8W+XmYwkS2I0'
                    + '9CRKpKGhsvIJjG9giQmliHFZlkUIGnEF7KTiCagpsYHWhoTQaiUUxLixYZb5KAAZZhbunu7O/PKf'
                    + 'e+fcA+/pqwb4DuximEqXhT4iI8dMpBWEsWsuGYdpZFttiLSSgTvhZ1W/SvfO1CvYdV1kPghV68a3'
                    + '0zzUWZH5pBqEui7dnqlFmLoq0gxC1XfGZdoLal2kea8ahLoqKXNAJQBT2yJzwUTVt0bS6ANqy1ga'
                    + 'VCEq/oVTtjji4hQVhhnlYBH4WIJV9vlkXLm+10R8oJb79Jl1j9UdazJRGpkrmNkSF9SOz2T71s7M'
                    + 'SIfD2lmmfjGSRz3hK8l4w1P+bah/HJLN0sys2JSMZQB+jKo6KSc8vLlLn5ikzF4268Wg2+pPOWW6'
                    + 'ONcpr3PrXy9VfS473M/D7H+TLmrqsXtOGctvxvMv2oVNP+Av0uHbzbxyJaywyUjx8TlnPY2YxqkD'
                    + 'dAAAAABJRU5ErkJggg==');
                seleniumFollowerImg.setAttribute('id', 'selenium-mouse-follower');
                seleniumFollowerImg.setAttribute('style', 'position: absolute; z-index: 99999999999; pointer-events: none;');
                document.body.appendChild(seleniumFollowerImg);
                jQuery(document).mousemove(function(e){
                    jQuery("#selenium-mouse-follower").stop().animate({left:e.pageX, top:e.pageY});
                });
            '''
        self.js(js)

    def show_keys(self, load_jquery=False):
        js = '''var seleniumKeyPress=document.createElement("div");
        var seleniumKeyPressInner=document.createElement("div");
        seleniumKeyPress.setAttribute('id', 'selenium-key-press');
        seleniumKeyPressInner.setAttribute('id', 'selenium-key-press-inner');
        seleniumKeyPress.setAttribute('style', 'border: 1px solid black; border-radius: 25px;'
                                             + 'position: absolute; z-index: 99999999999; '
                                             + 'opacity: 0.0; '
                                             + 'min-width: 125px; min-height: 125px; '
                                             + 'vertical-align: middle;'
                                             + 'top: 50%; left: 50%');
        seleniumKeyPressInner.setAttribute('style', 'font-size: 110px; line-height: 110px; '
                                             + 'position: absolute; color: black; '
                                             + 'vertical-align: middle;'
                                             + 'transform: translate(-50%, -50%);'
                                             + 'top: 50%; left: 50%');
        seleniumKeyPress.appendChild(seleniumKeyPressInner);
        document.body.appendChild(seleniumKeyPress);
        jQuery(document).bind('keydown', function(e) {
            jQuery('#selenium-key-press').fadeTo(0, 1, function() {
                jQuery('#selenium-key-press-inner').html('');
                var p____key = String.fromCharCode(e.keyCode);
                if (e.keyCode == '13') {
                    p____key = "&lAarr;";
                }
                jQuery('#selenium-key-press-inner').html(p____key);
                jQuery('#selenium-key-press').fadeTo(50, 0.0)
            });
        });
        '''
        self.js(js)
