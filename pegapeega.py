from random import *
from turtle import *
from time import sleep
t = Turtle()
t.color("black")
t.shape("turtle")
t.speed(10)
t.penup()
def rand_move():
    t.goto(randint(-200,200),randint(-200,200))

t.points = 0

def cth(x,y):
    t.write ("A!", font =('arial'  ,15, 'normal'))
    t.points += 1
    print(t.points)
    rand_move()






while t.points<3:
    t.onclick(cth)
    rand_move()
    sleep(1)
t.write ("ты победил", font =('arial'  ,15, 'normal'))
t.hideturtle()
# Определи функцию-обработчик catch(x, y), которая обработает клик по черепашке 
# (успешные клики копятся в свойстве t.points)

# Создай подписку на событие «клик по объекту-черепашке»

# Создай цикл, работающий пока кликов t.points меньше 3