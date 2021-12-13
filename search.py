from tree import TreeNode



class SearchManager():
    """Manages chain searches"""
    def __init__(self):
        self.queue = []
        self.query = ""
        self.node = None

    def traverseNext(self, speed=1):
        """Traverses the next given number of nodes in the queue, and returns two values
        speed: the number of nodes to traverse per frame; note that higher values may affect framerate.
        The first value represents the outcome of the traversal as well as what the second value is.
        -1 means the chain doesn't exist in the initial node, in which case the second value is the last node traversed.
        0 means no chain has been found, in which case the second value is the last node traversed in this step.
        1 means a chain has been found, in which case the second value is the highest-level node in the chain."""

        if len(self.query) == 0:
            return (1, self.queue[0])

        for n in range(speed):
            self.node = self.queue.pop(0)
            self.node.createChildren()
            chainNode = self.checkChain(self.node)
            if chainNode != None:
                return (1, chainNode)
            self.queue += self.node.children
            if len(self.queue) == 0:
                return (-1, self.node)

        return (0, self.node)



    def checkChain(self, node):
        """Checks if the given node contains a chain based on the query, and if so, returns the highest-level node"""
        chainNodes = [node]
        newNodes = []
        highestNode = None
        for letter in self.query:
            highestNode = None
            for n in chainNodes:
                if self.nodeMatchesLetter(n,letter):
                    highestNode = n
                    n.createChildren()
                    newNodes += n.children
            chainNodes = newNodes[:]
            newNodes = []
        return highestNode



    def nodeMatchesLetter(self, node, letter):
        """Returns whether or not the given node's type correlates to the given letter"""
        if letter == 'l':
            return node.value == True
        elif letter == 'u':
            return node.value == False
        elif letter == 'i':
            return type(node.value) == int
        elif letter == 's':
            return type(node.value) == str
        return False