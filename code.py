import pygame as pg
from random import randint

pg.init()

# Создаем класс окружности
class Circle:

    # Определяем конструктор
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.x_speed = 3
        self.rad = rad
        self.color = color

    # Метод отрисовки
    def draw(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)

    # Метод автоматического движения
    def move(self):
        self.x += self.x_speed
        
    # Метод для изменения направления движения при соударении со стенкой
    def change_of_dir(self, w_sc):
        if self.x > w_sc:
            self.x_speed *= -1
        if self.x < 0:
            self.x_speed *= -1
        
h_sc = 500
w_sc = 500

FPS = 120
# Создаем окно
win = pg.display.set_mode((w_sc, h_sc))
clock = pg.time.Clock()

list_of_circles = []
# Нужно создать ОБЪЕКТ окружности
for i in range(100):
    y = i * 5
    x = i * 5
    list_of_circles.append(Circle(x, y, 20, (randint(0, 255), randint(0, 255), randint(0, 255))))

# Главный цикл программы
while True:
    # Проверка на нажатие крестика
    win.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    # Отрисовываем созданый объект
    # Двигаем объект
    # Проверяем соударение со стенкой

    for i in range(100):
        list_of_circles[i].draw(win)
        list_of_circles[i].move()
        list_of_circles[i].change_of_dir(w_sc)
 
    pg.display.update()
    clock.tick(FPS)