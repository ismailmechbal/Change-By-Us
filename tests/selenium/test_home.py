"""
Module to hold basic home Selenium tests.
"""
from selenium import selenium
import unittest, time, re, os, subprocess

def rel_to_abs(path):
    """
    Function to take relative path and make absolute
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_dir, path)
    

class test_home(unittest.TestCase):
    """
    Tests that the home page can be reached and home link can be used.
    """
    
    def setUp(self):
        self.verificationErrors = []
        config = rel_to_abs("../../lighttpd.conf")
        
        # self.server_proc = subprocess.Popen(["lighttpd", "-D", "-f %s" % config])
        
        self.selenium = selenium("localhost", 4443, "*chrome", "http://localhost:8080/")
        self.selenium.start()
    
    def test_test_home(self):
        """
        Actual test that checks the home page can be reached and home link can be used.
        """
        
        sel = self.selenium
        sel.open("/")
        sel.click("link=Change by Us NYC")
        sel.wait_for_page_to_load("20000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
        
        # self.server_proc.kill()
        

if __name__ == "__main__":
    unittest.main()
