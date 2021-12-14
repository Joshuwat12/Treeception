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
        Execute this method for a node before referencing its children.
        count: the number of children to create. It is 1-5 by default."""
        if self.children is None:
            self.children = []
            if count < 0:
                count = random.randrange(1, 6)
            names = list("abcdefghijklmnopqrstuvwxyz")
            if self.value is True:
                self.children = [TreeNode(str(n)) for n in range(count)]
            elif self.value is False:
                for n in range(count):
                    newLetter = names.pop(random.randrange(len(names)))
                    self.children.append(TreeNode(newLetter))

            for node in self.children:
                node.parent = self
                if len(self.name) > 1:
                    node.directory = node.name
                else:
                    node.directory = self.directory + node.name

                if random.randrange(5) == 0:
                    node.value = random.randrange(1000, 10000)
                elif random.randrange(4) == 0:
                    node.value = [random.choice(names) for c in range(4)]
                    node.value = "".join(node.value)
                else:
                    node.value = random.choice([True, False])
