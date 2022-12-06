import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        left, top = self.left, self.top
        for g in self.board:
            for j in g:
                if j == 0:
                    col = 1
                else:
                    col = 0
                pygame.draw.rect(screen, 'white', (left, top, self.cell_size, self.cell_size), col)
                left += self.cell_size
            top += self.cell_size
            left = self.left

    def get_cell(self, mouse_pos):
        if mouse_pos[0] <= self.left + self.cell_size * self.width and \
                mouse_pos[1] <= self.top + self.cell_size * self.height:
            return (mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size
        else:
            return None

    def on_click(self, cell):
        cell = (cell[1], cell[0])
        for i in range(self.height):
            if self.board[i][cell[1]]:
                self.board[i][cell[1]] = 0
            else:
                self.board[i][cell[1]] = 1
        for j in range(self.width):
            if self.board[cell[0]][j]:
                self.board[cell[0]][j] = 0
                if j == cell[1]:
                    self.board[cell[0]][j] = 1
            else:
                self.board[cell[0]][j] = 1
                if j == cell[1]:
                    self.board[cell[0]][j] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
running = True
board = Board(5, 7)
board.render(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
