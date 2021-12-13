import random



class TreeNode():
    """A node for a tree
    name: the name of the node.
    value: a special variable used to specify the value stored within the node.
    children: an array storing the node's children."""

    def __init__(self, name, value=True, children=None):
        self.name = name
        self.value = value
        self.children = children

    def __len__(self):
        return len(self.children)

    def __getitem__(self, key):
        return self.children[key]

    def createChildren(self, count=-1):
        """Creates child nodes with random names and values
        count: the number of children to create"""
        if count < 0:
            count = random.randrange(6)
        names = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if self.value == True:
            self.children = [TreeNode(str(n)) for n in range(count)]
        elif self.value == False:
            self.children = [TreeNode(names.pop(random.randrange(len(names)))) for n in range(count)]
        else:
            self.children = []

        for node in self.children:
            node.parent = self
            node.directory = ("" if len(self.name) > 1 else self.directory) + node.name
            if random.randrange(5) == 0:
                node.value = random.randrange(1000, 10000)
            elif random.randrange(4) == 0:
                node.value = [random.choice(names) for c in range(4)]
                node.value = "".join(node.value)
            else:
                node.value = random.choice([True,False])