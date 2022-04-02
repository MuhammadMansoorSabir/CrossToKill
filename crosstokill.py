import random
import sys

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

arr = []
compmoves = []
draw = []


def printBoard(board):
    print(board[1] + '--' + board[2] + '--' + board[3])
    print('|  |  |')
    print(board[4] + '--' + board[5] + '--' + board[6])
    print('|  |  |')
    print(board[7] + '--' + board[8] + '--' + board[9])
    print('\n')


def entposhum():
    pos = int(input("type a position to insert :  "))  # placing fucnction for human
    if board[pos] == ' ':
        board[pos] = "x"
        # if (board[pos] == 'x'):
        arr.append(pos)
        lent = arr.__len__()
    else:
        print("The position is already filled ")
        entposhum()
    entposmac()

    # x+=1


def entposmac():
    pos1 = random.randint(1, 9)  # placing function for machine
    if board[pos1] == ' ':
        insert(pos1)
    else:
        entposmac()


def insert(pos1):  # insertion for machine
    board[pos1] = 'o'
    compmoves.append(pos1)
    printBoard(board)
    if arr.__len__() == 4:
        print('LETS PLAY')
        humanmove()
    entposhum()


def humanmove():
    chkForWin()
    lp = int(draw.__len__())
    if lp == 20:
        drawfunc()
    mov = int(input("queens(x) placing : " + str(arr) + "\n" + "which queen to move: "))
    # print(mov)
    print("Computer placing :" + str(compmoves))
    # print(board[mov])
    if board[mov] == 'x':
        mov1 = int(input("to which position : "))
        if board[mov1] == ' ':
            if mov == 1 and board[2] == 'o' and mov1 == 3:
                draw.append(1)
                board[mov] = ' '
                board[2] = ' '
                popit(2)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 1 and board[4] == 'o' and mov1 == 7:
                draw.append(1)
                board[mov] = ' '
                board[4] = ' '
                popit(4)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 1 and board[2] != 'o' and mov1 == 3:

                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 1 and board[4] != 'o' and mov1 == 7:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 1 and (mov1 == mov + 3 or mov1 == mov - 3 or mov1 == mov + 1):
                draw.append(1)
                board[1] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 4 and board[5] == 'o' and mov1 == 6:
                draw.append(1)
                board[mov] = ' '
                board[5] = ' '
                popit(5)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 4 and (mov1 == mov + 1 or mov1 == mov + 3 or mov1 == mov - 1):
                draw.append(1)
                board[4] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 7 and board[8] == 'o' and mov1 == 9:
                draw.append(1)
                board[mov] = ' '
                board[8] = ' '
                popit(8)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()
            elif mov == 7 and board[4] == 'o' and mov1 == 1:
                draw.append(1)
                board[mov] = ' '
                board[4] = ' '
                popit(4)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 7 and board[4] != 'o' and mov1 == 1:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 7 and board[8] != 'o' and mov1 == 9:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 7 and (mov1 == mov + 1 or mov1 == mov - 3 or mov1 == mov - 1):
                draw.append(1)
                board[7] = ' '
                board[mov1] = 'x'
                pophum(mov)
                arr.append(mov1)
                printBoard(board)
                macmove()

            elif mov == 9 and board[8] == 'o' and mov1 == 7:
                draw.append(1)
                board[mov] = ' '
                board[8] = ' '
                popit(8)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 9 and board[6] == 'o' and mov1 == 3:
                draw.append(1)
                board[mov] = ' '
                board[6] = ' '
                popit(6)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 9 and board[8] != 'o' and mov1 == 7:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 9 and board[6] != 'o' and mov1 == 7:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 9 and (mov1 == mov - 3 or mov1 == mov - 1):
                draw.append(1)
                board[9] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 6 and board[5] == 'o' and mov1 == 4:
                draw.append(1)
                board[mov] = ' '
                board[5] = ' '
                popit(5)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 6 and (mov1 == mov + 3 or mov1 == mov - 3 or mov1 == mov - 1):
                draw.append(1)
                board[6] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            if mov == 3 and board[2] == 'o' and mov1 == 1:
                draw.append(1)
                board[mov] = ' '
                board[2] = ' '
                popit(2)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()
            elif mov == 3 and board[6] == 'o' and mov1 == 9:
                draw.append(1)
                board[mov] = ' '
                board[6] = ' '
                popit(6)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 3 and board[2] != 'o' and mov1 == 1:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 3 and board[2] != 'o' and mov1 == 1:
                print("cant cross your own queen or only cross to kill oponent")
                humanmove()
            elif mov == 3 and (mov1 == mov + 3 or mov1 == mov - 3 or mov1 == mov - 1):
                draw.append(1)
                board[3] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 2 and (mov1 == mov + 3 or mov1 == mov - 1 or mov1 == mov + 1):
                draw.append(1)
                board[2] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 2 and board[5] == 'o' and mov1 == 8:
                draw.append(1)
                board[mov] = ' '
                board[5] = ' '
                popit(5)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 5 and (mov1 == 8 or mov1 == 4 or mov1 == 6 or mov1 == 2):
                draw.append(1)
                board[5] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 8 and (mov1 == mov - 3 or mov1 == mov - 1 or mov1 == mov + 1):
                draw.append(1)
                board[8] = ' '
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            elif mov == 8 and board[5] == 'o' and mov1 == 2:
                draw.append(1)
                board[mov] = ' '
                board[5] = ' '
                popit(5)
                board[mov1] = 'x'
                printBoard(board)
                pophum(mov)
                arr.append(mov1)
                macmove()

            else:
                chkForWin()
                print("INVALID MOVE")
                humanmove()
        else:
            print("position is not empty and invalid move")
            printBoard(board)
            humanmove()

    else:
        print("NOT YOUR QUEEN POSITION")
        humanmove()


def popit(r):
    ind = compmoves.index(r)
    compmoves.pop(ind)
    return


def pophum(r):
    ind = arr.index(r)
    arr.pop(ind)
    return


def macmove():
    chkForWin()
    lp = int(draw.__len__())
    if lp == 20:
        drawfunc()
    t = int(compmoves.__len__())
    for i in range(0, t):
        macm = int(compmoves[i])
        if macm < 9 and macm == 1 and board[macm + 1] == 'x' and board[macm + 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = ' '
            board[macm + 2] = 'o'
            popit(macm)
            pophum(macm + 1)
            # print("1")
            compmoves.append(macm + 2)
            printBoard(board)
            humanmove()
        elif macm < 7 and macm == 1 and board[macm + 3] == 'x' and board[macm + 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 3] = ' '
            board[macm + 6] = 'o'
            popit(macm)
            pophum(macm + 3)
            # print("2")
            compmoves.append(macm + 6)
            printBoard(board)
            humanmove()
        elif macm == 2 and board[macm + 3] == 'x' and board[macm + 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 3] = ' '
            board[macm + 6] = 'o'
            popit(macm)
            # print("3")
            pophum(macm + 3)
            compmoves.append(macm + 6)
            printBoard(board)
            humanmove()
        elif macm == 3 and board[macm + 3] == 'x' and board[macm + 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 3] = ' '
            board[macm + 6] = 'o'
            popit(macm)
            # print("4")
            pophum(macm + 3)
            compmoves.append(macm + 6)
            printBoard(board)
            humanmove()

        elif macm == 3 and board[macm - 1] == 'x' and board[macm - 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = ' '
            board[macm - 2] = 'o'
            popit(macm)
            # print("5")
            pophum(macm - 1)
            compmoves.append(macm - 2)
            printBoard(board)
            humanmove()

        elif macm == 4 and board[macm + 1] == 'x' and board[macm + 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = ' '
            board[macm + 2] = 'o'
            popit(macm)
            pophum(macm + 1)
            # print("6")
            compmoves.append(macm + 2)
            printBoard(board)
            humanmove()

        elif macm == 6 and board[macm - 1] == 'x' and board[macm - 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = ' '
            board[macm - 2] = 'o'
            popit(macm)
            pophum(macm - 1)
            # print("7")
            compmoves.append(macm + 6)
            printBoard(board)
            humanmove()
        elif macm == 6 and board[macm - 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = 'o'
            popit(macm)
            # print("7")
            compmoves.append(macm - 1)
            printBoard(board)
            humanmove()
        elif macm == 6 and board[macm - 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = 'o'
            popit(macm)
            compmoves.append(macm - 1)
            printBoard(board)
            humanmove()
        elif macm == 6 and board[macm + 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 3] = 'o'
            popit(macm)
            # print("7")
            compmoves.append(macm - 1)
            printBoard(board)
            humanmove()
        elif macm == 7 and board[macm + 1] == 'x' and board[macm + 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = ' '
            board[macm + 2] = 'o'
            popit(macm)
            pophum(macm + 1)
            # print("8")
            compmoves.append(macm + 2)
            printBoard(board)
            humanmove()
        elif macm == 7 and board[macm - 3] == 'x' and board[macm - 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = ' '
            board[macm - 6] = 'o'
            popit(macm)
            pophum(macm - 3)
            # print("9")
            compmoves.append(macm - 6)
            printBoard(board)
            humanmove()
        elif macm == 8 and board[macm - 3] == 'x' and board[macm - 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = ' '
            board[macm - 6] = 'o'
            popit(macm)
            pophum(macm - 3)
            # print("10")
            compmoves.append(macm - 6)
            printBoard(board)
            humanmove()
        elif macm == 9 and board[macm - 3] == 'x' and board[macm - 6] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = ' '
            board[macm - 6] = 'o'
            popit(macm)
            # print("11")
            pophum(macm - 3)
            compmoves.append(macm - 6)
            printBoard(board)
            humanmove()

        elif macm == 9 and board[macm - 1] == 'x' and board[macm - 2] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = ' '
            board[macm - 2] = 'o'
            popit(macm)
            pophum(macm - 1)
            # print("12")
            compmoves.append(macm - 2)
            printBoard(board)
            humanmove()

        elif macm == 7 and board[macm + 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = 'o'
            popit(macm)
            compmoves.append(macm + 1)
            # print("14")
            printBoard(board)
            humanmove()

        elif macm == 9 and board[macm - 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = 'o'
            popit(macm)
            compmoves.append(macm - 3)
            # print("16")
            printBoard(board)
            humanmove()
        elif macm == 8 and board[macm - 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = 'o'
            popit(macm)
            compmoves.append(macm - 1)
            # print("17")
            printBoard(board)
            humanmove()
        elif macm == 8 and board[macm + 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = 'o'
            popit(macm)
            compmoves.append(macm + 1)
            # print("18")
            printBoard(board)
            humanmove()
        elif macm == 8 and board[macm - 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = 'o'
            popit(macm)
            compmoves.append(macm - 3)
            # print("19")
            printBoard(board)
            humanmove()
        elif macm == 7 and board[macm + 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = 'o'
            popit(macm)
            # print("20")
            compmoves.append(macm + 1)
            printBoard(board)
            humanmove()
        elif macm == 7 and board[macm - 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = 'o'
            popit(macm)
            # print("21")
            compmoves.append(macm - 3)
            printBoard(board)
            humanmove()
        elif macm == 8 and board[macm - 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 2] = 'o'
            popit(macm)
            compmoves.append(macm - 2)
            printBoard(board)
            humanmove()
        elif macm == 5 and board[macm + 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 1] = 'o'
            popit(macm)
            # print("3")
            compmoves.append(macm + 1)
            printBoard(board)
            humanmove()
        elif macm == 5 and board[macm - 1] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 1] = 'o'
            popit(macm)
            # print("3")
            compmoves.append(macm - 1)
            printBoard(board)
            humanmove()
        elif macm == 5 and board[macm - 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm - 3] = 'o'
            popit(macm)
            # print("3")
            compmoves.append(macm - 3)
            printBoard(board)
            humanmove()
        elif macm == 5 and board[macm + 3] == ' ':
            draw.append(1)
            board[macm] = ' '
            board[macm + 3] = 'o'
            popit(macm)
            # print("3")
            compmoves.append(macm + 3)
            printBoard(board)
            humanmove()


def chkForWin():
    if compmoves.__len__() == 0:
        print("YOU WIN")
        print("computer loses :(")
        sys.exit()
    elif arr.__len__() == 0:
        print("COMPUTER WINS")
        print("You lost :(")
        sys.exit()
    return


def drawfunc():
    print("MATCH DRAWN NO RESULT AFTER 10 MOVES EACH PLAYER")
    sys.exit()


entposhum()
