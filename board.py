import pygame

class Board:
    def __init__(self, x, y, rows, cols, offX, offY, size=80):
        self.rows = rows
        self.cols = cols
        self.x = x
        self.y = y
        self.size = size
        self.list = []
        self.offX = offX
        self.offY = offY
        for i in range(cols):
            rowInList = []
            for j in range(rows):
                rowInList.append([i, j, "white"])
            self.list.append(rowInList)

    def getListOfBoard(self):
        return self.list

    def setListOfBoard(self, newList):
        self.list = newList

    def drawBoard(self, screen):
        boardList = self.getListOfBoard()
        for i in range(self.cols):
            for j in range(self.rows):
                # Vykresluje podle barvy uložené na indexu 2
                pygame.draw.rect(screen, boardList[i][j][2], [self.offX + j * self.size, self.offY + i * self.size, self.size, self.size])

    def drawDefaultBoard(self, screen):
        boardList = self.getListOfBoard()
        for i in range(self.cols):
            for j in range(self.rows):
                color = "white" if (i + j) % 2 == 0 else "black"
                boardList[i][j][2] = color
        self.setListOfBoard(boardList)
        self.drawBoard(screen)

    def drawPiece(self, screen, type, row, col, offX, offY):
        posX = self.x
        posY = self.y
        match type:
            case 3:
                pygame.draw.circle(screen, "red", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 25)
            case 4:
                pygame.draw.circle(screen, "blue", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 25)
            case 6:
                pygame.draw.circle(screen, "red", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 30)
                pygame.draw.circle(screen, "gold", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 27)
                pygame.draw.circle(screen, "red", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 22)
            case 8:
                pygame.draw.circle(screen, "blue", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 30)
                pygame.draw.circle(screen, "gold", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 27)
                pygame.draw.circle(screen, "blue", (posX + col * self.size + 40 + offX, posY + offY + row * self.size + 40), 22)