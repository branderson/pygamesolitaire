__author__ = 'brad'
import includes
import CardClass
from includes import *


class Stack(pygame.sprite.Sprite):

    cardStack = []
    cardGroup = pygame.sprite.OrderedUpdates()
    type = "stack"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.rect = self.image.get_rect()

    def rebuildStack(self):
        self.cardGroup.empty()
        # for i in xrange(0, self.cardStack.__len__()):
        #    self.cardGroup.add(self.cardStack[i])
        # if self.length() != 0:
        #     self.peek().rect = self.rect
        #     self.cardGroup.add(self.peek())
        # for i in self.cardStack:
        #     i.faceUp = 0
        # if self.length() > 0:
        #     self.cardStack[0].faceUp = 1
        # for card in self.cardStack:
        #     self.cardGroup.add(card)
        for i in xrange(0, self.cardStack.__len__()):
            self.cardStack[i].faceUp = 0
        if self.length() > 0:
            self.peek().rect = self.rect
            self.cardGroup.add(self.peek())
            self.peek().faceUp = 1

    def peek(self):
        return self.cardStack[self.cardStack.__len__() - 1]

    def length(self):
        return self.cardStack.__len__()

    def push(self, card):
        self.cardStack = self.cardStack + [card]

    def recycle(self, card):
        self.cardStack = [card] + self.cardStack

    def pop(self):
        if self.cardStack.__len__() > 1:
            temp = self.cardStack[self.cardStack.__len__() - 1]
            self.cardStack = self.cardStack[:(self.cardStack.__len__() - 1)]
        else:
            temp = self.cardStack[0]
            self.cardStack = []
        return temp

    def draw(self, surface):
        self.rebuildStack()
        self.cardGroup.update()
        pygame.draw.rect(surface, GREY, self.rect, 1)
        if self.length != 0:
            self.cardGroup.draw(surface)

    def drawCard(self, deck):
        print("Deck is " + str(deck.cardStack.__len__()) + " long.")
        self.push(deck.pop())
        if self.length() > 1:
            deck.recycle(self.cardStack[0])
            self.cardStack = self.cardStack[1:]
        print("Deck is now " + str(deck.cardStack.__len__()) + " long.")
        print("Next card in deck is " + deck.cardStack[deck.length() - 1].id)
