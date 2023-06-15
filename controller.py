import pygame
import time 
import json
from floor import Floor
from Elevator import Elevator

# load setting
with open('config.json') as f:
    config = json.load(f)

window_width = int(config["window_width"])
window_height = int(config["window_height"])
floor_size = int(config["floor"])
floor_height = int(config["floor_height"])
elevator_width = int(config["elevator_width"])
elevator_height = int(config["elevator_height"])

del(config)
del(f)

def main():
    # 初始化Pygame
    pygame.init()

    # 設定遊戲視窗
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Elevator Simulator")

    # 創建電梯物件
    elevator = Elevator(width = elevator_width, 
                        height = elevator_height, 
                        x = 700,  
                        y = 500)
    # 創建樓層物件
    floor = [Floor( x = 0, 
                    y = (window_height // (floor_size)) * (i + 1) - floor_height , 
                    height = floor_height,
                    width = window_width, 
                    floor_number = i + 1) for i in range(floor_size)]



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))  # 清空畫面
        elevator.draw(screen)
        for i in floor:
            i.draw(screen)
        pygame.display.update()

    pygame.quit()

main()