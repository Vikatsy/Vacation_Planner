import sys
import nose
from nose.tools import *
import unittest2 as unittest


from wizzair_scraper import WizzairScraper

class WizzAirScraperTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def teardownClass(cls):
    	pass

    def setUp(self):
    	pass

    def tearDown(self):
    	pass


    def test_get_api(self):
    	scraper = WizzairScraper()
    	api_url = scraper._get_api_url()
    	import re
		ok_(re.match('https:\/\/be\.wizzair\.com\/\d\.\d\.\d\/Api', api_url))
    	# eq_(1, 1)
    