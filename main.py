import pygame
from board import Board
from pieces.piece import Piece
from pieces.queen import Queen
map = [
    [0, 4, 0, 4, 0, 4, 0, 4],
    [4, 0, 4, 0, 4, 0, 4, 0],
    [0, 4, 0, 4, 0, 4, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 3, 0, 3, 0, 3, 0],
    [0, 3, 0, 3, 0, 3, 0, 3],
    [3, 0, 3, 0, 3, 0, 3, 0],
]
TEAMS = {0: "0", 3: "A", 6: "A", 4: "B", 8: "B"}
TEAM_COLORS = {"A": "red", "B": "blue"}

pygame.init()
boardSize = 840
screen = pygame.display.set_mode((boardSize, boardSize))
clock = pygame.time.Clock()
turnFont = pygame.font.SysFont(None, 32)
winnerFont = pygame.font.SysFont(None, 48)

bx = 80
by = 80
gameBoard = Board(0, 0, 8, 8, bx, by)
running = True
selectedPiece = None
row, col = -1, -1

QUEEN_VALUES = (6, 8)

def draw(map,player):
    isDraw = False
    for row in range(len(map)):
        for col in range(len(map[row])):
            if TEAMS[map[row][col]] == TEAMS[player]:
                selectedPiece = selectPieceAt(map, row, col)
                graph = selectedPiece.jump(map, selectedPiece.row, selectedPiece.col)
                bestJumps = selectedPiece.allJumps(graph, (selectedPiece.row, selectedPiece.col))
                moveOptions = selectedPiece.move(map, selectedPiece.row, selectedPiece.col)
                if(len(bestJumps) > 0 or len(moveOptions) > 0):
                    return isDraw
    isDraw = True
    return isDraw
def gameOver(map,player):
    end = False
    winnerMsg = ""
    piecesA = getAllplayerPieces(map, 3)
    piecesB = getAllplayerPieces(map, 4)
    if len(piecesA) == 0:
        end = True
        winnerMsg = "Player Blue wins!"
    elif len(piecesB) == 0:
        end = True
        winnerMsg = "Player Red wins!"
    elif draw(map,player) == True:
        end = True
        winnerMsg = "Draw!"
    return end, winnerMsg



def getClickedPos(pos, bx, by, size):
    mouseX, mouseY = pos
    col = (mouseX - bx) // size
    row = (mouseY - by) // size
    if row > 7 or col > 7 or col < 0 or row < 0:
        return (-1, -1)
    return int(row), int(col)


def drawPieces(map, gameBoard, screen):
    for row, vals in enumerate(map):
        for col, val in enumerate(vals):
            gameBoard.drawPiece(screen, val, row, col, bx, by)


def selectPieceAt(map, row, col):
    val = map[row][col]
    if val == 0:
        return None
    if val in QUEEN_VALUES:
        return Queen(row, col, val, "alive")
    return Piece(row, col, val, "alive")


def newQueen(map, player, row, col):
    updatedMap = [r[:] for r in map]
    if player == 3 and row == 0:
        updatedMap[row][col] = 6
    if player == 4 and row == 7:
        updatedMap[row][col] = 8
    return updatedMap


def getAllplayerPieces(map, player):
    listOfPlayers = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] != 0 and TEAMS[player] == TEAMS[map[row][col]]:
                listOfPlayers.append((row, col))
    return listOfPlayers


def checkForJumps(listOfPlayers, map):
    canJumpList = []
    for row, col in listOfPlayers:
        piece = selectPieceAt(map, row, col)
        graph = piece.jump(map, piece.row, piece.col)
        bestJumps = piece.allJumps(graph, (piece.row, piece.col))
        if len(bestJumps) > 0:
            canJumpList.append((row, col))
    return canJumpList


def drawTurnIndicator(screen, font, pOneTurn):
    currentTeam = "A" if pOneTurn else "B"
    color = TEAM_COLORS[currentTeam]

    squareSize = 24
    margin = 10
    squareX = boardSize - squareSize - margin
    squareY = margin

    pygame.draw.rect(screen, color, (squareX, squareY, squareSize, squareSize))
    pygame.draw.rect(screen, "black", (squareX, squareY, squareSize, squareSize), 2)

    text = font.render("This player is on turn", True, "black")
    textX = squareX - text.get_width() - 10
    textY = squareY + (squareSize - text.get_height()) // 2
    screen.blit(text, (textX, textY))


def drawWinnerText(screen, font, text):
    rendered = font.render(text, True, "white")
    x = (boardSize - rendered.get_width()) // 2
    y = 10
    screen.blit(rendered, (x, y))


selected = False
moveOptions = []
bestJumps = []
screen.fill("purple")
gameBoard.drawDefaultBoard(screen)
print(map)
pOneTurn = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            clickedRow, clickedCol = getClickedPos(pos, bx, by, 80)
            if clickedRow != -1:
                piece = selectPieceAt(map, clickedRow, clickedCol)
                if piece is not None:
                    currentTeam = "A" if pOneTurn else "B"

                    if TEAMS[piece.player] == currentTeam:
                        selectedPiece = piece

                        listOfPlayers = getAllplayerPieces(map, selectedPiece.player)
                        jumpList = checkForJumps(listOfPlayers, map)

                        if len(jumpList) == 0:

                            selected = True
                        elif (selectedPiece.row, selectedPiece.col) in jumpList:

                            selected = True
                        else:
                            selected = False

    mapBack = gameBoard.getListOfBoard()

    if selectedPiece is not None and gameOver(map,selectedPiece.player)[0] == False:
        graph = selectedPiece.jump(map, selectedPiece.row, selectedPiece.col)
        bestJumps = selectedPiece.allJumps(graph, (selectedPiece.row, selectedPiece.col))
        gameBoard.drawDefaultBoard(screen)
        moveOptions = selectedPiece.move(map, selectedPiece.row, selectedPiece.col)

        if selected:
            if len(bestJumps) > 0:
                for path, newMap in bestJumps:
                    mapBack[path[-1][0]][path[-1][1]][2] = "red"
            else:
                for r, c, newMap in moveOptions:
                    mapBack[r][c][2] = "green"

        gameBoard.setListOfBoard(mapBack)
        gameBoard.drawBoard(screen)

    if selected == True:
        if len(bestJumps) != 0:
            for path, newMap in bestJumps:
                if clickedRow == path[-1][0] and clickedCol == path[-1][1]:
                    map = newMap
                    map = newQueen(map, selectedPiece.player, clickedRow, clickedCol)
                    gameBoard.drawDefaultBoard(screen)
                    selected = False
                    selectedPiece = None
                    if(pOneTurn == True):
                        pOneTurn = False
                    else:
                        pOneTurn = True
        else:
            if len(moveOptions) != 0:
                for newRow, newCol, newMap in moveOptions:
                    if clickedRow == newRow and clickedCol == newCol:
                        map = newMap
                        map = newQueen(map,selectedPiece.player,newRow,newCol)
                        gameBoard.drawDefaultBoard(screen)
                        selected = False
                        selectedPiece = None
                        if (pOneTurn == True):
                            pOneTurn = False
                        else:
                            pOneTurn = True

    drawPieces(map, gameBoard, screen)

    currentPlayer = 3 if pOneTurn else 4
    isGameOver, winnerText = gameOver(map, currentPlayer)
    if isGameOver:
        drawWinnerText(screen, winnerFont, winnerText)
    else:
        drawTurnIndicator(screen, turnFont, pOneTurn)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()