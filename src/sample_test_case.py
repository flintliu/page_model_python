import nose
from nose.tools import ok_, eq_, raises
from sample_action import *

def test_search_url():
    browser = open_browser("firefox", "https://www.google.com.au")
    do_search(browser, "flint")
    eq_(browser.current_url.split("=")[-1], "flint")

if __name__ == "__main__":
	nose.run()