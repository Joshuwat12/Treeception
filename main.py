from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.clock import Clock
from tree import TreeNode
from search import SearchManager
from audio import Audio
import random


class DodgeGame(Widget):

    rootNode = TreeNode("ROOT")
    rootNode.parent = None
    rootNode.directory = "ROOT"
    rootNode.createChildren(5)
    currentNode = rootNode
    dirDisplay = StringProperty(currentNode.directory)
    nodeValue = ""
    valueDisplay = StringProperty(nodeValue)
    isDisabled = [False]*5
    buttonsDisabled = ListProperty(isDisabled)
    childNames = [str(n) for n in range(5)]
    buttonNames = ListProperty(childNames)
    positions = [(n/10, 0.5) for n in range(1, 6)]
    buttonPos = ListProperty(positions)
    searchQuery = ""
    searchDisplay = StringProperty(searchQuery)
    isSearching = False
    disableQuery = BooleanProperty(isSearching)
    searchManager = SearchManager()

    def update(self, dt):
        self.dirDisplay = self.currentNode.directory
        if type(self.currentNode.value) == bool:
            self.valueDisplay = ""
        else:
            self.valueDisplay = str(self.currentNode.value)
        self.isDisabled = [n >= len(self.currentNode) for n in range(5)]
        self.buttonsDisabled = self.isDisabled
        self.childNames = []
        for n in range(5):
            if self.isDisabled[n]:
                self.childNames.append("")
            else:
                self.childNames.append(self.currentNode[n].name)
        self.buttonNames = self.childNames
        self.buttonPos = self.positions
        self.searchDisplay = self.searchQuery
        self.disableQuery = self.isSearching

        if self.isSearching:
            searchResult = self.searchManager.traverseNext(10)
            self.gotoNode(searchResult[1])
            if searchResult[0] != 0:
                self.isSearching = False
                if searchResult[0] == -1:
                    Audio.playAudio("nochain.wav")
                    self.gotoNode(self.rootNode)

    def gotoNode(self, node):
        """Switches to the given node for viewing"""
        if node is not None:
            node.createChildren()
            print([n.value for n in node.children])
            self.currentNode = node
            if node.value is False:
                self.positions = []
                for n in range(5):
                    pos = (random.random()*0.8+0.1, random.random()*0.2+0.4)
                    self.positions.append(pos)
            else:
                self.positions = [(n/10, 0.5) for n in range(1, 6)]

    def addSearch(self, item, caps="is"):
        if len(self.searchQuery) == 0 or self.searchQuery[-1] not in caps:
            self.searchQuery += item

    def backSearch(self):
        if len(self.searchQuery) > 0:
            self.searchQuery = self.searchQuery[:-1]

    def clearSearch(self):
        self.searchQuery = ""

    def startSearch(self):
        if self.isSearching:
            self.isSearching = False
            self.searchManager.queue = []
            self.searchManager.query = ""
        elif len(self.searchQuery) > 0:
            self.isSearching = True
            self.searchManager.queue = [self.currentNode]
            self.searchManager.query = self.searchQuery


class DodgeApp(App):
    def build(self):
        game = DodgeGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    DodgeApp().run()
