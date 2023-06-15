import pygame

class Floor:
    def __init__(self, x, y, height, width, floor_number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.floor_number = floor_number
        # 其他初始化屬性

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        # 繪製樓層圖形

    # 其他相關方法