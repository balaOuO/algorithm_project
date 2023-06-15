import pygame
import json

# 定義電梯類別
class Elevator:
    def __init__(self, x, y):
        # load setting
        with open('config.json') as f:
            config = json.load(f)

        window_width = int(config["window_width"])
        window_height = int(config["window_height"])
        floor_size = int(config["floor"])
        floor_height = int(config["floor_height"])
        elevator_width = int(config["elevator_width"])
        elevator_height = int(config["elevator_height"])
        speed = float(config["elevator_speed"])

        del(config)
        del(f)

        self.x = x
        self.y = y
        self.width = elevator_width
        self.height = elevator_height
        self.state = -1 * speed
        self.stop = [(window_height // (floor_size)) * (i + 1) - floor_height for i in range(floor_size)]
        self.stop.reverse()
        #for i in self.stop()
        #self.color = (255, 0, 0)
        # 其他初始化屬性

    def control(self, screen):
        if(self.y + self.height <= self.stop[4]):
            self.state = 0
        self.y += self.state
        pygame.draw.rect(screen, (255, 0, 0) if self.state == 0 else (0, 255, 0), (self.x, self.y, self.width, self.height))
        # 繪製電梯圖形

    def move(self, direction):
        # 電梯移動的邏輯
        pass

    def open_doors(self):
        # 開啟電梯門的邏輯
        pass

    def close_doors(self):
        # 關閉電梯門的邏輯
        pass

    # 其他相關方法