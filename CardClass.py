__author__ = 'brad'
import includes
from includes import *


cardValues = {0: "A",
              1: "2",
              2: "3",
              3: "4",
              4: "5",
              5: "6",
              6: "7",
              7: "8",
              8: "9",
              9: "10",
              10: "J",
              11: "Q",
              12: "K"}


class Card(pygame.sprite.Sprite):

    value = 0
    suite = -1
    faceUp = 0
    cardValue = "0"
    num = -1
    id = ""

    def __init__(self, suite, value, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.imageUp = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.imageDown = pygame.Surface([CARDWIDTH, CARDHEIGHT])
        self.cardValue = cardValues[value]
        self.num = num
        if suite == 0:
            self.imageUp.fill(DARKRED)
            self.id = self.cardValue + " of Diamonds"
        elif suite == 1:
            self.imageUp.fill(DARKBLUE)
            self.id = self.cardValue + " of Clubs"
        elif suite == 2:
            self.imageUp.fill(LIGHTRED)
            self.id = self.cardValue + " of Hearts"
        elif suite == 3:
            self.imageUp.fill(LIGHTBLUE)
            self.id = self.cardValue + " of Spades"
        else:
            self.imageUp.fill(BLACK)
            self.id = self.cardValue + " of Nothing"
        # if suite == 0:
        #     self.image.fill(RED)
        # elif suite == 1:
        #     self.image.fill(BLUE)
        # elif suite == 2:
        #     self.image.fill(GREEN)
        # elif suite == 3:
        #     self.image.fill(WHITE)
        # else:
        #     self.image.fill(BLACK)
        self.imageDown.fill(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.imageUp, GREY, self.rect, 1)
        pygame.draw.rect(self.imageDown, GREY, self.rect, 1)
        # pygame.draw.rect(self.image, BLACK, self.rect, 1)
        # pygame.draw.rect(self.image, BLACK, self.rect, 1)
        self.value = value
        self.suite = suite
        self.imageUp.blit(CARDFONT.render(self.cardValue, True, BLACK), (2, 2))
        self.image.blit(self.imageDown, (0, 0))
        # self.image.blit(cardFont.render(self.cardValue, True, BLACK), (2, 2))

    def update(self):
        if self.faceUp == 1:
            self.image.blit(self.imageUp, (0, 0))
        else:
            self.image.blit(self.imageDown, (0, 0))