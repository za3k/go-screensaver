import sys
print(sys.version)

from pprint import pprint
import time, subprocess, os
import cv2
import numpy as np
import PIL

WIDTH, HEIGHT = 1080, 720

DOT_SIZE = 20
GRID_SPACING = 30
assert GRID_SPACING*19 + DOT_SIZE < min(WIDTH, HEIGHT)

def set_pixel(im, x, y, rgb):
    r,g,b = rgb
    im[x][y][:] = b,g,r

def draw_dot(im, x, y, rgb):
    for i in range(DOT_SIZE):
        for j in range(DOT_SIZE):
            set_pixel(im, x+i, y+j, rgb)

def draw_filled_circle(im, row, col, is_black):
    x, y = row*GRID_SPACING, col*GRID_SPACING
    if is_black:
        draw_dot(im, x, y, (0, 0, 0))
    else:
        draw_dot(im, x, y, (255, 0, 0))
    
def board_to_image(b):
    im = np.full((HEIGHT,HEIGHT,3), 255, dtype=np.uint8)

    # Draw a Go board

    # Draw stones
    for row_num, row in enumerate(b):
        # row_num=4, row=[black, white, blank, blank, white, black, blank]
        for col_num, square in enumerate(row):
            # col_num=5, square="white"
            if square == "black":
                draw_filled_circle(im, row_num, col_num, is_black=True)
            if square == "white":
                draw_filled_circle(im, row_num, col_num, is_black=False)

    # Draw numbers in stones (TODO)
    return im

def wait_a_bit():
    time.sleep(0.25)

def play_game(moves):
    board = [['blank']*19 for _ in range(19)]
    turn = 'black'
    for move in moves:
        board[move[1]][move[0]] = turn
        turn = {"black": "white", "white": "black"}[turn]
        cv2.imshow('image', board_to_image(board))
        cv2.waitKey(1)
        wait_a_bit()
    cv2.destroyAllWindows()

MOVES=[[15,3],[3,15],[15,15],[3,3],[5,2],[4,2],[5,3],[3,5],[9,2],[16,2],[15,2],[16,3],[16,4],[17,4],[17,5],[17,3],[16,5],[15,1],[14,1],[16,1],[18,1],[17,0],[15,0],[18,2],[18,4],[17,1],[16,13],[13,16],[13,15],[14,16],[14,15],[15,16],[16,16],[16,17],[17,16],[12,15],[12,14],[11,15],[11,14],[10,15],[11,8],[16,9],[17,10],[16,10],[17,11],[12,10],[10,10],[13,8],[14,10],[14,9],[15,10],[15,9],[15,7],[16,11],[13,11],[13,10],[14,11],[13,6],[11,6],[12,11],[10,12],[16,12],[17,12],[13,12],[14,12],[14,13],[13,13],[12,12],[15,13],[13,4],[11,3],[15,6],[16,7],[16,6],[17,6],[14,7],[17,8],[15,5],[15,4],[14,4],[12,7],[13,7],[12,9],[13,9],[15,8],[12,5],[14,5],[14,6],[11,5],[13,2],[13,1],[12,2],[12,3],[14,2],[12,1],[11,2],[11,1],[10,2],[10,1],[10,3],[10,4],[9,3],[8,2],[8,3],[6,5],[8,5],[7,6],[8,6],[8,7],[9,7],[8,8],[9,4],[7,4],[10,5],[11,4],[10,6],[9,5],[10,7],[8,4],[11,7],[10,8],[12,6],[12,8],[13,3],[7,3],[7,16],[2,13],[2,14],[3,13],[2,7],[2,2],[3,2],[2,3],[2,4],[3,1],[4,1],[2,1],[1,4],[5,1],[3,0],[2,0],[4,0],[0,3],[1,3],[1,2],[0,0],[4,4],[3,4],[4,7],[2,10],[2,6],[3,6],[1,7],[2,8],[1,9],[2,9],[1,11],[1,10],[1,14],[1,15],[1,13],[5,16],[2,16],[2,15],[4,16],[4,15],[5,17],[6,17],[5,15],[6,16],[3,16],[5,14],[6,15],[7,14],[6,14],[6,13],[5,13],[7,15],[4,14],[5,12],[4,13],[6,11],[7,12],[6,12],[9,17],[9,16],[11,17],[12,17],[10,16],[9,15],[10,14],[9,14],[9,13],[5,8],[4,8],[4,9]]
if __name__ == "__main__":
    play_game(MOVES)    
