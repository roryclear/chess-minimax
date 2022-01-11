import chess

maxDepth = 5


class Node(object):
    def __init__(self):
        self.value = None
        self.move = None
        self.children = []
        self.board = None


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


board = chess.Board()
print(board)

