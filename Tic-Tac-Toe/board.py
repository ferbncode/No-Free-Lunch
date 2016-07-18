import random
class Board(object):
    ''' Board for the tic tac toe game '''
    def __init__(self):
        '''initialize game state'''
        self.gameState = ['_', '_', '_',
                          '_', '_', '_',
                          '_', '_', '_']

        self.symbols = ['x', 'o']
        self.userSymbol = 'o'
    def get_user_symbol(self):
        '''ask user for his preference of symbol'''
        self.userSymbol = raw_input("Enter the symbol you want to play with: ")
    def __str__(self):
        '''ugly print function for board current situation'''
        returnString = ''
        i = 1
        while i!=10:
            returnString = returnString + self.gameState[i-1] + " "
            if(i%3 == 0):
                returnString = returnString + "\n"
            i+=1
        return returnString
    def get_user_action(self, randomize = True):
        '''ask for user action'''
        if randomize == True:
            flag = 0 
            while flag == 0:
                index = random.randrange(0, 9)
                if(self.gameState[index] == '_'):
                    flag = 1
        else:
            x, y = map(int, raw_input("Please enter coordinate of the board you would like to mark your symbol (top left is (0,0))").split())
            index = x*3 + y
        try:
            if(self.gameState[index] == '_'):
                self.gameState[index] = self.userSymbol
        except Exception as e:
            print "Our of bounds player. You need to concentrate."
        #print self #debug
    def determine_end(self):
        '''ugly function to determine board state'''
        listsOfCombinations = ([0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
        for list in listsOfCombinations:
            x = [self.gameState[ind] for ind in list]
            if(x == ['x','x','x'] or x==['o','o','o']):
                if (x ==['x','x','x']):
                    if(self.userSymbol == 'x'):
                       return True, -100
                    else:
                        return True, 100
                elif(x ==['o','o','o']):
                    if(self.userSymbol == 'o'):
                        return True, -100
                    else:
                        return True, 100
        try:
            inde = self.gameState.index('_')
            return False, 1
        except Exception as e:
            return True, 3 #game ended with no one winnig
    def get_possible_actions(self):
        '''returns list of possible indices that can be taken by the bot'''
        actions = []
        for i in range(len(self.gameState)):
            if(self.gameState[i] == '_'):
                actions.append(i)
        return actions
#debug
#a = Board()
#while 1:
#    print a
#   a.get_user_action()
#print a.determine_end()
#print a.get_possible_actions()
