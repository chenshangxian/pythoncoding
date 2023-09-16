import turtle

# 初始化设置
myTurtle = turtle.Turtle()
myTurtle.speed(0)  # 设置最快的绘制速度
myTurtle.setheading(90)
def my_square(size):
    """该函数用于绘制一个正方形"""
    for _ in range(4):
        myTurtle.forward(size)
        myTurtle.right(270)

# 正方形的初始尺寸
size = 10

# 画100个正方形
for _ in range(100):
    my_square(size)
    size += 10  # 每次增加10单位的大小
    myTurtle.penup()  # 提起画笔
    myTurtle.goto(0, 0)  # 返回初始位置
    myTurtle.pendown()  # 放下画笔继续画

turtle.done()