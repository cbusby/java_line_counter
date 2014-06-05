#----------------------------------------------------------------------
#
# Callie Busby
# 6/5/14
# test_java_line_counter.py
#
#----------------------------------------------------------------------

import unittest
import sys
from java_line_counter import *

#----------------------------------------------------------------------

class javaLineCounterTest(unittest.TestCase):

    #------------------------------------------------------------------
    '''
    def test_read_file(self):
        pass
    '''
    #------------------------------------------------------------------

    def test_simple_one_line_of_code(self):

        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine(' return \n'), 1)

    #------------------------------------------------------------------
        
    def test_two_lines_of_code_no_comments(self):

        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('x = 12 \n return x \n'), 2)

    #------------------------------------------------------------------

    def test_one_end_of_line_comment(self):

        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('// this is a comment \n'), 0)

    #------------------------------------------------------------------
    def test_one_end_line_between_two_valid(self):
        
        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('x = 12 \n// comment \n y = 1 \n'), 2)

    #------------------------------------------------------------------

    def test_ignore_white_space_before_end_line_comment(self):

        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('x = 1 \n   //comment\n y = 2\n'), 2)

    #------------------------------------------------------------------

    def test_valid_line_with_an_end_of_line_comment(self):
        
        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('x = 1 //this is one line \n'), 1)

    #------------------------------------------------------------------

    def test_string_with_no_newline_character(self):

        count1 = LineCounter()

        self.assertEqual(count1.translateEndLine('x = 5 //comment\n'), 1)

    #------------------------------------------------------------------

    def test_simple_multiple_line_comment(self):

        pass
        
                                                       
#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
