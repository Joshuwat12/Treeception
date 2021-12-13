from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from tree import TreeNode
import random


class DodgeGame(Widget):

    rootNode = TreeNode("ROOT")
    rootNode.parent = None
    rootNode.directory = ("ROOT")
    rootNode.createChildren(5)
    currentNode = rootNode
    dirDisplay = StringProperty(currentNode.directory)
    nodeValue = ""
    valueDisplay = StringProperty(nodeValue)
    isDisabled = [False]*5
    buttonsDisabled = ListProperty(isDisabled)
    childNames = [str(n) for n in range(5)]
    buttonNames = ListProperty(childNames)
    positions = [(n/10, 0.5) for n in range(1,6)]
    buttonPos = ListProperty(positions)

    def update(self, dt):
        self.dirDisplay = self.currentNode.directory
        self.valueDisplay = "" if type(self.currentNode.value) == bool else str(self.currentNode.value)
        self.isDisabled = [n >= len(self.currentNode) for n in range(5)]
        self.buttonsDisabled = self.isDisabled
        self.childNames = [("" if self.isDisabled[n] else self.currentNode[n].name) for n in range(5)]
        self.buttonNames = self.childNames
        self.buttonPos = self.positions

    def gotoNode(self, node):
        """Switches to the given node for viewing"""
        if node != None:
            if node.children == None:
                node.createChildren()
            print([n.value for n in node.children])
            self.currentNode = node
            if node.value == False:
                self.positions = [(random.random() * 0.8 + 0.1, random.random() * 0.2 + 0.4) for n in range(5)]
            else:
                self.positions = [(n/10, 0.5) for n in range(1,6)]



class DodgeApp(App):
    def build(self):
        game = DodgeGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game



if __name__ == '__main__':
    DodgeApp().run()
