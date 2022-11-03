import turtle


def draw(length, depth):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        draw(length/2, depth-1)
        t.fd(length/2)
        draw(length/2, depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw(length/2, depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)


window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
draw(400, 4)
window.exitonclick()
