__author__ = 'brad'

#!/usr/bin/env python
import includes
import CardClass
import StackClass
import DeckClass
import TableauClass
import FoundationClass
from includes import *
from CardClass import *
from StackClass import *
from DeckClass import *
from TableauClass import *
from FoundationClass import *


def main():

    # set up the window
    pygame.display.set_caption('PyGame Solitaire')

    # draw on the surface object
    DISPLAYSURF.blit(BACKGROUND, (0, 0))

    # run the game loop
    while True:
        if runGame() == False:
            break


def runGame():
    # initialize the game
    deck = initializeDeck()
    tableaus = [Tableau(deck, 1),
                Tableau(deck, 2),
                Tableau(deck, 3),
                Tableau(deck, 4),
                Tableau(deck, 5),
                Tableau(deck, 6),
                Tableau(deck, 7)]
    foundations = [Foundation(0),
                   Foundation(1),
                   Foundation(2),
                   Foundation(3)]
    # drawnCard = Stack()
    # drawnCard.drawCard(deck)

    gameGroup = []

    deck.rect.x = 8
    deck.rect.y = 8
    gameGroup.append(deck)

    for i in xrange(0, 7):
        tableaus[i].rect.x = 8 + (96 * i)
        tableaus[i].rect.y = 128
        gameGroup.append(tableaus[i])
    for i in xrange(0, 4):
        foundations[i].rect.x = 296 + (96 * i)
        foundations[i].rect.y = 8
        gameGroup.append(foundations[i])

    # drawnCard.rect.x = 104
    # drawnCard.rect.y = 8
    # gameGroup.append(drawnCard)
    # Weird bug where all moves from drawnCard are the next card in deck
    # drawnCard seems to become deck
    msg = ""
    selected = pygame.sprite.OrderedUpdates()

    # Game loop
    while True:
        checkQuit()
        if checkWin(foundations):
            # Winning screen here
            break
        if checkRestart():
            break
        # if drawnCard.length() == 0:
        #     drawnCard.drawCard(deck)
        for event in pygame.event.get():
            handleEvents(gameGroup, event, selected)
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        drawGame(gameGroup, msg)
        pygame.display.update()


def checkQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def checkWin(foundations):
    for stack in foundations:
        # if stack.length() == 13:
            # previousCard = None
            # for card in stack:
            #     if previousCard == None:
            #         previousCard = card
            #     else:
            #         if card.value != previousCard.value + 1:
            #             return False
        if stack.length() != 13:
            return False
    return True


def checkRestart():
    for event in pygame.event.get(KEYUP):
        if event.key == K_r:
            return True
        pygame.event.post(event)
    return False


def terminate():
    pygame.quit()
    sys.exit()


def drawGame(spriteGroup, msg):
    for i in spriteGroup:
        # i.update()
        i.draw(DISPLAYSURF)


def handleEvents(spriteGroup, event, selected):
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            # check position for card
            # mousex, mousey = event.pos
            mouseCard = checkPosition(spriteGroup, event.pos)

            # Draw new card
            # Crazy clusterfuck that needs to have card movement put into a function... this is ridiculous
            for stack in spriteGroup:
                if mouseCard is None:
                    selected.empty()
                    return
                elif mouseCard.num == -1:
                    print(stack.type)
                    if stack.rect.colliderect(mouseCard.rect) and selected.sprites().__len__() != 0:
                        topCard = selected.sprites()[0]
                        if topCard.value == 12:
                            moveCards = []
                            for stackMove in spriteGroup:
                                if stackMove.cardStack.count(topCard) != 0:
                                    for card in stackMove.cardStack[stackMove.cardStack.index(topCard):]:
                                        moveCards = moveCards + [card]
                                    stackMove.cardStack = stackMove.cardStack[:stackMove.cardStack.index(topCard)]
                                    stack.cardStack.extend(moveCards)
                                    selected.empty()
                                    print("Moving king")
                                    return
                        selected.empty()
                elif stack.cardStack.count(mouseCard) != 0:
                # if stack.cardGroup.has(mouseCard):
                #     if stack.type == "deck":
                #         for stackTwo in spriteGroup:
                #             if stackTwo.type == "stack":
                #                 selected.empty()
                #                 stackTwo.drawCard(stack)
                #                 return
                    print(stack.type)
                    if stack.type == "deck" or stack.type == "tableau":
                        # Sending aces to foundation
                        if mouseCard.value == 0:
                            print("Should send ace to foundation " + str(mouseCard.suite))
                            for stackMove in spriteGroup:
                                if stackMove.type == "foundation":
                                    print("Checking foundation " + str(stackMove.suite))
                                    if stackMove.suite == mouseCard.suite:
                                        moveCards = []
                                        moveCards = [stack.cardStack[stack.length() - 1]]
                                        # Learn what I fixed here cause it was weird
                                        stack.cardStack = stack.cardStack[:stack.cardStack.index(mouseCard)]
                                        print("Moving ace " + str(stackMove.suite) + str(mouseCard.suite))
                                        stackMove.cardStack = stackMove.cardStack + moveCards
                                        selected.empty()
                                        return

                    if stack.type == "deck":
                        selected.empty()
                        selected.add(stack.cardStack[stack.length() - 1])
                        for card in selected:
                            print(card.id)
                        return

                    elif stack.type == "foundation":
                        if selected.sprites().__len__() == 0:
                            selected.add(stack.cardStack[stack.length() - 1])
                            print("I selected something for the first time")
                            return
                        elif selected.sprites().__len__() == 1 and stack.length() > 0:
                            if selected.sprites()[0].suite == stack.suite and selected.sprites()[0].value == stack.cardStack[stack.length() - 1].value + 1:
                                moveCards = []
                                for stackMove in spriteGroup:
                                    if stackMove.cardStack.count(selected.sprites()[0]) != 0:
                                        moveCards = [stackMove.cardStack[stackMove.cardStack.index(selected.sprites()[0])]]
                                        stackMove.cardStack = stackMove.cardStack[:stackMove.cardStack.index(selected.sprites()[0])]
                                        print("Trying to remove")
                                stack.cardStack = stack.cardStack + moveCards
                        selected.empty()
                        return

                    elif stack.type == "tableau":
                        # If nothing is selected
                        if selected.sprites().__len__() == 0:
                            for card in stack.cardStack[stack.cardStack.index(mouseCard):]:
                                selected.add(card)
                                print("I selected something for the first time")
                        # If something was already selected
                        else:
                            if selected.has(mouseCard):
                                return
                            # If we might be moving something
                            else:
                                topCard = selected.sprites()[0]
                                print("Topcard is " + topCard.id)
                                canMove = False
                                if stack.cardStack.index(mouseCard) == stack.cardStack.__len__() - 1:
                                    canMove = True
                                # Moving cards around
                                if (topCard.suite + mouseCard.suite) % 2 == 1 and canMove and topCard.value == mouseCard.value - 1:
                                    print("Should be moving")
                                    moveCards = []
                                    for stackMove in spriteGroup:
                                        if stackMove.cardStack.count(topCard) != 0:
                                        # if stackTwo.cardGroup.has(topCard):
                                            for card in stackMove.cardStack[stackMove.cardStack.index(topCard):]:
                                                moveCards = moveCards + [card]
                                            stackMove.cardStack = stackMove.cardStack[:stackMove.cardStack.index(topCard)]
                                            break
                                    print("Moving " + topCard.id)
                                    print("To " + mouseCard.id)
                                    stack.cardStack.extend(moveCards)
                                    selected.empty()
                                    print("I moved a stack")
                                else:
                                    selected.empty()
                                    for card in stack.cardStack[stack.cardStack.index(mouseCard):]:
                                        selected.add(card)
                                    print("I selected something new")
                        return

            if selected.sprites().__len__() == 0:
                print("Nothing is selected")
            else:
                for card in selected.sprites():
                    print(card.id + " is selected")

        elif event.button == 3:
            for stack in spriteGroup:
                if stack.type == "deck":
                    if stack.length() > 1:
                        tempStack = []
                        tempStack = [stack.cardStack[stack.length() - 1]] + stack.cardStack[:(stack.length() - 1)]
                        stack.cardStack = tempStack
                    selected.empty()
                        # It's not switching if I've already played a card
            print("Should be switching")
        elif event.button == 2:
            # Find the foundations
            # Incredibly inefficient algorithm for autocomplete
            madeChanges = True
            while madeChanges:
                madeChanges = False
                for stack in spriteGroup:
                    if stack.type == "foundation" and stack.length() != 0:
                        bottomCard = stack.cardStack[stack.length() - 1]
                        for searchStack in spriteGroup:
                            if searchStack.length() != 0:
                                if searchStack.cardStack[searchStack.length() - 1].value == bottomCard.value + 1 and \
                                        searchStack.cardStack[searchStack.length() - 1].suite == bottomCard.suite \
                                        and searchStack.cardStack[searchStack.length() - 1].faceUp == 1:
                                    moveCards = []
                                    moveCards = [searchStack.cardStack[searchStack.length() - 1]]
                                    # Learn what I fixed here cause it was weird
                                    searchStack.cardStack = searchStack.cardStack[:searchStack.cardStack.index(searchStack.cardStack[searchStack.length() - 1])]
                                    # print("Moving ace " + str(stackMove.suite) + str(mouseCard.suite))
                                    stack.cardStack = stack.cardStack + moveCards
                                    madeChanges = True
                                    # selected.empty()

                    elif stack.type == "foundation":
                        for searchStack in spriteGroup:
                            if searchStack.length() != 0:
                                if searchStack.cardStack[searchStack.length() - 1].value == 0 \
                                        and searchStack.cardStack[searchStack.length() - 1].suite == stack.suite and \
                                        searchStack.cardStack[searchStack.length() - 1].faceUp == 1:
                                    #move the ace
                                    moveCards = []
                                    moveCards = [searchStack.cardStack[searchStack.length() - 1]]
                                    # Learn what I fixed here cause it was weird
                                    searchStack.cardStack = searchStack.cardStack[:searchStack.cardStack.index(searchStack.cardStack[searchStack.length() - 1])]
                                    # print("Moving ace " + str(stackMove.suite) + str(mouseCard.suite))
                                    stack.cardStack = stack.cardStack + moveCards
                                    madeChanges = True
                                    # selected.empty()

            # canComplete = True
            # for stack in spriteGroup:
            #     for card in stack.cardStack:
            #         if card.faceUp == 0:
            #             canComplete = False
            # if canComplete == True:
            #     for stack in spriteGroup:
            #         if stack.type == "foundation":
            #             if stack.length() == 0:
            #


def checkPosition(spriteGroup, position):
    tempCard = None
    for stack in spriteGroup:
        if stack.rect.collidepoint(position) and stack.length() == 0 and stack.type == "tableau":
            tempCard = Card(-1, 0, -1)
            tempCard.rect.x = position[0]
            tempCard.rect.y = position[1]
        if stack.rect.collidepoint(position) and stack.length() == 0 and stack.type == "foundation":
            print("Clicking foundation " + str(stack.suite))
        for card in stack.cardStack:
            if card.rect.collidepoint(position) and (card.faceUp or stack.type == "deck"):
                tempCard = card
    return tempCard


if __name__ == '__main__':
    main()