#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from Testing import game

class TestGuess(unittest.TestCase):
    
    def test_guessgame(self):
        guess = 5
        answer = 5
        result = game.guessgame(guess,answer)
        self.assertTrue(result)

    def test_guessgame2(self):
        guess = 5
        answer = 0
        result = game.guessgame(guess,answer)
        self.assertFalse(result)

    def test_guessgame3(self):
        guess = 5
        answer = 12
        result = game.guessgame(guess,answer)
        self.assertFalse(result)

    def test_guessgame4(self):
        guess = 4
        answer = '6'
        result = game.guessgame(guess,answer)
        self.assertFalse(result)

        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'],exit=False)

