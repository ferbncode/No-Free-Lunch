from board import Board
import pickle
import time
# Agent uses value iteration for learning utilities of the states. An action is taken at random until all the states that are possible from that going state. If
# all states are not present before sellection of an action. It is so because that action will be chosen again and again. Thus random action before all utilites
# are observed. 
class Agent(object):
	'''Class for the playing agent - Tic Tac Toe Player(More of a Learner)'''
	def __init__(self, board, newly_learnt = True):
		self.policy = {}
		self.utilities = {} # Utility of state is initially not known. Thus we need to use get
		self.board = board
		self.state = None
		self.discount = 0.7
		if(self.board.userSymbol) == 'x':
			self.agentSymbol = 'o'
		else:
			self.agentSymbol = 'x'
		if(newly_learnt == False):
			self.utilities = pickle.load(open('utilities', 'r'))

	def get_current_state(self):
		self.state = tuple(self.board.gameState)
#		return self.state
	def determine_reward(self):
		# check the award recieved by the agent for the current states
		ended, reward = self.board.determine_end()
		return reward
	def get_possible_actions(self):
		#print self.board.get_possible_actions()
		self.possible_actions = self.board.get_possible_actions()
	def check_good_state(self, state):
		# good states with reward 100 for the agent
		listsOfCombinations = ([0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
		for list in listsOfCombinations:
			x = [state[index] for index in list]
			if x == list([self.agentSymbol]) * 3:
				return True
		return False
	def check_bad_state(self):
		# bad states with reward -100 for the agent
		listsOfCombinations = ([0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
		for list in listOfCombinations:
			x = [state[index] for index in list]
			if x == list([self.board.userSymbol]) * 3:
				return True
		return False

	def update_utilities_and_take_action(self):
		self.get_current_state()
		presentStateUtility = self.utilities.get(self.state, 0)
		state_present = self.state
		max_utility = -1
		max_utility_action = -1
		self.get_possible_actions()
		for action in self.possible_actions:
			state_present = list(state_present)
			state_present[action] = self.agentSymbol
			state_next = tuple(state_present)
			utility_next_state = self.utilities.get(state_next, 0)
			if(utility_next_state >= max_utility):
				max_utility = utility_next_state
				max_utility_action = action
			state_present = self.state
		self.utilities[self.state] = self.determine_reward() + self.discount*max_utility
		return max_utility_action
	def determine_the_end(self):
		ended, reward = self.board.determine_end()
		if ended == True:
			if reward == 100:
				print "This Game has ended with agent winning"
			elif reward == -100:
				print "This Game has ended with the agent losing"
			else:
				print "Game ended with no one winning"
			return True
		return False

			


ticTacBoard= Board()
learningAgent = Agent(ticTacBoard, newly_learnt = False)
for i in range(100):
	print ticTacBoard
	ticTacBoard.get_user_action(randomize = False)
	action = learningAgent.update_utilities_and_take_action()
	ticTacBoard.gameState[action] = learningAgent.agentSymbol
	action = learningAgent.update_utilities_and_take_action()
	time.sleep(2)
	if(learningAgent.determine_the_end() == True):
		ticTacBoard.gameState = ['_','_','_','_','_','_','_','_','_']
		print "Starting New Game"
	
print learningAgent.utilities
pickle.dump(learningAgent.utilities, open('utilities', 'w'))





