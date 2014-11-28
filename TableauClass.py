__author__ = 'brad'
import includes
import StackClass
from includes import *
from StackClass import *


class Tableau(Stack):

    type = "tableau"

    def __init__(self, deck, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.rect = self.image.get_rect()

        for i in xrange(0, size):
            self.push(deck.pop())
        self.cardStack[size - 1].faceUp = 1

    def rebuildStack(self):
        self.cardGroup.empty()
        # self.cardStack[self.cardStack.__len__() - 1].rect = self.rect
        for i in xrange(0, self.cardStack.__len__()):
            self.cardGroup.add(self.cardStack[i])
            if i == 0:
                self.cardStack[i].rect.x = self.rect.x
                self.cardStack[i].rect.y = self.rect.y
            else:
                self.cardStack[i].rect.x = self.cardStack[i-1].rect.x
                self.cardStack[i].rect.y = self.cardStack[i-1].rect.y + CARDHEIGHT/5
            self.type = "tableau"
        if self.length() > 0:
            if self.peek().faceUp == 0:
                self.peek().faceUp = 1

    def draw(self, surface):
        self.rebuildStack()
        self.cardGroup.update()
        pygame.draw.rect(surface, GREY, self.rect, 1)
        if self.length() > 0:
            self.cardGroup.draw(surface)
