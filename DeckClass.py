__author__ = 'brad'
import includes
import StackClass
from includes import *
from StackClass import *
from CardClass import *


class Deck(Stack):

    type = "deck"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.rect = self.image.get_rect()
        num = 0

        for i in xrange(0, 4):
            for j in xrange(0, 13):
                self.push(Card(i, j, num))
                num += 1

    def rebuildStack(self):
        self.cardGroup.empty()
        for i in xrange(0, self.cardStack.__len__()):
            self.cardStack[i].faceUp = 0
            self.cardGroup.add(self.cardStack[i])
            self.cardStack[i].rect.x = self.rect.x
            self.cardStack[i].rect.y = self.rect.y
        self.type = "deck"
        if self.length() > 0:
            if self.peek().faceUp == 0:
                self.peek().faceUp = 1

    def shuffle(self):
        # Fisher-Yates shuffle algorithm
        random.seed(None)
        tempStack = []
        for i in xrange(self.cardStack.__len__()-1, -1, -1):
            k = random.randint(0, i)
            tempStack.append(self.cardStack[k])
            self.cardStack.remove(self.cardStack[k])
        self.cardStack = tempStack


def initializeDeck():
    deck = Deck()
    deck.shuffle()
    return deck