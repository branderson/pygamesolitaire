__author__ = 'brad'
import includes
import StackClass
from includes import *
from StackClass import *


class Foundation(Stack):

    type = "foundation"
    suite = -1

    def __init__(self, suite):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.rect = self.image.get_rect()
        self.suite = suite
        print("Generated foundation suite " + str(suite))

    def rebuildStack(self):
        self.cardGroup.empty()
        for i in xrange(0, self.cardStack.__len__()):
            # self.cardStack[i].faceUp = 1
            self.cardGroup.add(self.cardStack[i])
            self.cardStack[i].rect.x = self.rect.x
            self.cardStack[i].rect.y = self.rect.y
        self.type = "foundation"

    def draw(self, surface):
        self.rebuildStack()
        self.cardGroup.update()
        pygame.draw.rect(surface, GREY, self.rect, 1)
        if self.length() > 0:
            self.cardGroup.draw(surface)