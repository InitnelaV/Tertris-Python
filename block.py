from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 40
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset +=  rows
        self.column_offset += columns

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles =[]
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x=0, offset_y=0):
        tiles = self.get_cell_position()
        for tile in tiles:
            tile_x = offset_x + tile.column * self.cell_size
            tile_y = offset_y + tile.row * self.cell_size
            tile_rect = pygame.Rect(tile_x, tile_y, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)