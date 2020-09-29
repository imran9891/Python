#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from Testing import main

class TestMain(unittest.TestCase):

    def setUp(self):
        print('about to test a function')
    
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'imran'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result,'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result,'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result,'please enter number')

    def tearDown(self):
        print('cleaning up')

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

