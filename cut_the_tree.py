#https://www.hackerrank.com/challenges/cut-the-tree
#incomplete

class Tree:

    def __init__(self, data, index):
        self.index = index
        self.data = data
        self.left = None
        self.right = None


    def add_to_tree(self, index, node):
        if self.left == None:
            self.right = node
        else:
            self.left = node

n = int(input())

weights = list(map(int, input().split()))
sum_weights = sum(weights)

s =  [list(map(int, input().split())) for i in range(1,n)]
print (s)

v = [0 for i in range(n)]
