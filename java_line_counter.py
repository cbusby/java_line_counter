#----------------------------------------------------------------------
#
# Callie Busby
# 6/5/14
# java_line_counter.py
#
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

class LineCounter:

    #------------------------------------------------------------------

    def __init__ (self):

        self.lineNumber = 0

    #------------------------------------------------------------------

    def readFile(self, fileName):

        pass
        '''
        infile = open(filename, 'r')

        symbolArray = []

        while True:

            if not symbol:
                break '''
         
            
    #------------------------------------------------------------------
    
    def translateEndLine(self, string):



        linesArray = string.split('\n')[:-1]

        for i in linesArray:
            while i[0] == ' ':
                i = i[1:]

            if not ((i[0] == '/') and (i[1] == '/')):
                self.lineNumber = self.lineNumber + 1

        

        return self.lineNumber
    
    #------------------------------------------------------------------
