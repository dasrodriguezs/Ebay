import unittest
import time
import sys
import os

dir_path = os.path.abspath(__file__ + "/../../..")
print(dir_path)

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([dir_path,
                 dir_path + '/Automation',
                 dir_path + '/Automation''/PageObjects',
                 dir_path + '/Automation''/drivers',
                 dir_path + '/Automation/Scripts',
                 dir_path + '/Automation/PageObjects/Pages',
                 dir_path + '/venv',
                 dir_path + '/venv/bin',
                 dir_path + '/venv/include',
                 dir_path + '/venv/lib',
                 dir_path + '/venv/lib64',
                 dir_path + '/.idea',
                 dir_path + '/.idea/inspectionProfiles',
                 dir_path + '/venv/lib/python3.7',
                 dir_path + '/venv/lib/python3.7/site-packages',
                 dir_path + '/venv/lib/python3.7/site-packages/config-0.4.2-py3.7.egg-info',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_internal/cli',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/commands',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/models',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/operations',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_internal/req',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/utils',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/vcs',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/cachecontrol',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/cachecontrol/caches',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_vendor/certifi',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/chardet',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/chardet/cli',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/colorama',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/distlib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/distlib/_backport',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/html5lib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/_trie',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/html5lib/filters',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treeadapters',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treebuilders',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/html5lib/treewalkers',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_vendor/idna',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/lockfile',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/msgpack',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/packaging',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/pep517',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/pkg_resources',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/progress',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/pytoml',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/requests',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg'
                            '/pip/_vendor/urllib3/contrib',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/contrib/_securetransport',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/packages',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/urllib3/packages/backports',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/packages/ssl_match_hostname',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_vendor'
                            '/urllib3/util',
                 dir_path + '/venv/lib/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/webencodings',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/common',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/android',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/blackberry',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/chrome',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common/actions'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/common'
                            '/html5',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver'
                            '/edge',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium'
                            '/webdriver/firefox',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/firefox/amd64'
                            '', dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/firefox'
                                           '/x86',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/ie'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium'
                            '/webdriver/opera',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/phantomjs',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/remote',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/safari',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/support',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium/webdriver/webkitgtk',
                 dir_path + '/venv/lib/python3.7/site-packages/selenium-3.141.0.dist-info',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/contrib',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/contrib/_securetransport'
                            '',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages/backports',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages/rfc3986',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3/packages'
                            '/ssl_match_hostname',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3'
                            '/util',
                 dir_path + '/venv/lib/python3.7/site-packages/urllib3-1.25.3.dist-info',
                 dir_path + '/venv/lib64/python3.7',
                 dir_path + '/venv/lib64/python3.7/site-packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/config-0.4.2-py3.7.egg-info',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/EGG-INFO',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_internal/cli',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/commands',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0'
                            '.3-py3.7.egg/pip/_internal/models',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/operations',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_internal/req',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_internal/utils',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_internal/vcs',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7'
                            '.egg/pip/_vendor/cachecontrol',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/cachecontrol/caches',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/certifi',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/chardet',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/chardet/cli',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_vendor/colorama',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/distlib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/distlib/_backport',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/html5lib/_trie',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/filters',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treeadapters',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treebuilders',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/html5lib/treewalkers',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/idna',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3'
                            '.7.egg/pip/_vendor/lockfile',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/msgpack',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/packaging',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/pep517',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/pkg_resources',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/progress',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/pytoml',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/requests',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3'
                            '-py3.7.egg/pip/_vendor/urllib3',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/contrib',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/contrib/_securetransport',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages/backports',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/packages/ssl_match_hostname',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip'
                            '/_vendor/urllib3/util',
                 dir_path + '/venv/lib64/python3.7/site-packages/pip-19'
                            '.0.3-py3.7.egg/pip/_vendor/webencodings',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/common',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/android',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/blackberry',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/common',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/chrome',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/common'
                            '/actions',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver'
                            '/common/html5',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/edge',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/firefox',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/firefox'
                            '/amd64',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver'
                            '/firefox/x86',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/ie',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/opera',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/phantomjs',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/remote',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/safari',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/support',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium/webdriver/webkitgtk',
                 dir_path + '/venv/lib64/python3.7/site-packages/selenium-3.141.0.dist-info',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/contrib'
                            '/_securetransport',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3'
                            '/contrib',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages/backports',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages/rfc3986',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3/packages'
                            '/ssl_match_hostname',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3'
                            '/util',
                 dir_path + '/venv/lib64/python3.7/site-packages/urllib3-1.25.3.dist-info'])

from selenium import webdriver
from functions import *
from Homepage import SearchTab
from Searchpage import SortItems


class TestSearchShoes(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.ebay.com/")

    def test_home_page_load(self):
        home_page = SearchTab(self.driver)
        self.assertTrue(home_page.check_page_loaded())

    def test_home_search(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()

    def test_search_page_load(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        self.assertTrue(search_page.check_page_loaded())

    def test_pick_brand_and_size(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        results = search_page.resultsnumber()
        time.sleep(2)
        print("Total resuts for the search: " + str(results))
        print("........................................................................................\n")

    def test_sort_items_asc(self):
        home_page = SearchTab(self.driver)
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        search_page.sortitems()
        time.sleep(5)
        number_of_items = 5
        items = search_page.takeproducts(number_of_items)

        print_results(items, "First five results")
        print_results(sort_by_name_asc(items), "Items sorted by name ASC")
        print_results(sort_by_price_desc(items), "Items sorted by price DESC")
        self.assertListEqual(items, sort_by_price_asc(items),
                             msg="Items are not sorted correctly")

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchShoes)
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearchShoes('test_sort_items_asc'))
    unittest.TextTestRunner(verbosity=2).run(suite)
