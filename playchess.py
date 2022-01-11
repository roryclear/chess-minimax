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


def getMove(gameBoard,n):
    j = 0
    for i in gameBoard.legal_moves:
        if j == n:
            return i
        j = j+1

def getNextMove(node):
	#just add first move before end for now?
	if node.depth < maxDepth:
		nextMove = Node()
		nextMove.move = getMove(node.board,0)
		nextMove.board = deepcopy(node.board)
		nextMove.board.push_san(str(nextMove.move))
		nextMove.depth = deepcopy(node.depth) + 1
		node.add_child(nextMove)
		getNextMove(nextMove)
	else:
		print("depth = ",node.depth)

board = chess.Board()
game = Node()
print(board)

game.board = board

#get bottom left nodes for now? before prune

print(game.board.legal_moves)
print(game)

getNextMove(game)

print(game)



