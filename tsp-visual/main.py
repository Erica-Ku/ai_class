import pygame
import gfx
import threading
from util import *
from algo_info import ALGO_INFO, DIVIDERS

# 0. 알고리즘 만들기?
# 1. 좌표
# 2. Loop 만들기
def loop():
    # 알고리즘 정보 가져오기
    for i in range(len(ALGO_INFO)):
        print(ALGO_INFO[i])

    while True:
        gfx.check_events()
        gfx.draw_text_center(surface, "Hello", font, 50, 50)
        gfx.draw_dividers(surface, DIVIDERS)
        for i in range(len(ALGO_INFO)):
            if i < len(sims):
                pass
        pygame.display.update()
        surface.fill(BLACK)
    
    # 무한반복
    # 알고리즘 배치
    # 그리기 => 점, 선, 텍스트
    # draw_point(x, y) => 값 반환X
    # draw_line(x, y) => 값 반환X
    # draw_text(x, y) => 값 반환X

    # 애니메이션 만들기
    # p를 직접 랜덤으로 만들기 => 답이 있는 랜덤
    # 포팅

pygame.init()
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
font = pygame.font.SysFont("Consolas", FONT_HEIGHT)
cities = make_cities(20)
list_of_cities_list = []
sims = []
threads = []

for i in range(len(ALGO_INFO)):
    list_of_cities_list.append(displace(cities, *ALGO_INFO[i]["displacement"]))

for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]["depends"] == -1:
        sims.append(ALGO_INFO[i]["sim"](list_of_cities_list[i]))
        threads.append(threading.Thread(target = sims[i].find))
        threads[i].daemon = True


if __name__=="__main__":
    pygame.display.set_caption("TSP - Visualizer")
    # loop()