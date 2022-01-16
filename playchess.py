import chess
from copy import deepcopy

maxDepth = 5

class Node(object):
    def __init__(self):
        self.value = None
        self.move = None
        self.children = []
        self.board = None
        self.depth = 0


    def __str__(self, level=0):

        ret = "\t"*level+repr(self.move)+" value: "+repr(self.value)+" depth: "+repr(self.depth)+"\n"		
        for child in self.children:
            ret += child.__str__(level+1)
        return ret    

    def add_child(self, obj):
        self.children.append(obj)

    def get_child(self,index):
    	i = 0
    	for child in self.children:
    		if i == index:
    			return child
    		else:
    			i+=1

def eval(moves):
	###### use Chess piece relative value from alphazero?? ######

	#white only for now?
	#PAWNS
	board = moves.board

	boardString = str(board)

	if board.is_checkmate():
		if moves.depth % 2 == 1: #white just moved??
			return 420
		else:
			return -420

	wv = boardString.count('P') + (boardString.count('N') * 3.05) + (boardString.count('B') * 3.33 + (boardString.count('R') * 5.63) + (boardString.count('Q') * 9.5))
	bv = boardString.count('p') + (boardString.count('n') * 3.05) + (boardString.count('b') * 3.33 + (boardString.count('r') * 5.63) + (boardString.count('q') * 9.5))

	return wv - bv

def validMoves(gameBoard):

    m = 0
    for i in gameBoard.legal_moves:
        m = m+1
    return m

def getMove(gameBoard,n):
    j = 0
    for i in gameBoard.legal_moves:
        if j == n:
            return i
        j = j+1

def getNextMove(node,parentNode):
	if node.depth == 1:
		print("nodes")
	#just add first move before end for now?		
	if node.depth < maxDepth:
		numberOfValidMoves = validMoves(node.board)
		if node.depth % 2 == 0:
			#print("white")
			for n in range(0,numberOfValidMoves):
				nextMove = Node()
				nextMove.move = getMove(node.board,n)
				nextMove.board = deepcopy(node.board)
				nextMove.board.push_san(str(nextMove.move))
				nextMove.depth = deepcopy(node.depth) + 1
				node.add_child(nextMove)
				if node.value == None:
					node.value = getNextMove(nextMove,node)
				else:
					moveValue = getNextMove(nextMove,node)
					if moveValue > node.value:
						node.value = moveValue
				if parentNode != None and parentNode.value != None:
					if node.value >= parentNode.value:
						node.value = parentNode.value
						break
			if numberOfValidMoves == 0:
				node.value = eval(node)
				if parentNode != None and parentNode.value != None:
					if node.value >= parentNode.value:
						node.value = parentNode.value
		else:
			#print("black")
			for n in range(0,numberOfValidMoves):
			#for n in range(0,2):
				nextMove = Node()
				nextMove.move = getMove(node.board,n)
				nextMove.board = deepcopy(node.board)
				nextMove.board.push_san(str(nextMove.move))
				nextMove.depth = deepcopy(node.depth) + 1
				node.add_child(nextMove)
				if node.value == None:
					node.value = getNextMove(nextMove,node)	
				else:
					moveValue = getNextMove(nextMove,node)
					if moveValue < node.value:
						node.value = moveValue
				if parentNode != None and parentNode.value != None:
					#print("parent is not none")
					if node.value <= parentNode.value:
						node.value = parentNode.value
						break
			if numberOfValidMoves == 0: #no valid moves
				node.value = eval(node)
				if parentNode != None and parentNode.value != None:
					#print("parent is not none")
					if node.value <= parentNode.value:
						node.value = parentNode.value
		if node.value == None:
			node.value = eval(node)
		return node.value
	else:
		#print("depth = ",node.depth)
		node.value = eval(node)
		return node.value	

board = chess.Board()
game = Node()

game.board = board



while validMoves(game.board) > 0:
	gameBoardCopy = deepcopy(game.board)

	game = Node()
	game.board = gameBoardCopy

	print(game.board)

	#get bottom left nodes for now? before prune

	print(game.board.legal_moves)

	getNextMove(game,None)

	#print(game)
	print(game.board)

	print("first moves???")
	value = -500
	nextMove = None
	for child in game.children:
		print(child.move," -> ",child.value)
		if child.value > value:
			value = child.value
			nextMove = child.move

	print("nextMove = ",nextMove)
	game.board.push_san(str(nextMove))
	yourMove = input("Enter your move: ")
	game.board.push_san(str(yourMove))

#pass up best value at last layer through all parents???
#https://media.geeksforgeeks.org/wp-content/uploads/MIN_MAX2.jpg



