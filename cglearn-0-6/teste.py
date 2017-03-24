from math import sin, cos, pi

def circulo(c):
    angle = 0
    circle_points = 10
    radius = 1.5
    center_x = 5.0
    center_y = 0.0

    for i in range(circle_points-1):
        angle = radius*2*pi*i/circle_points
        px = cos(angle) + center_x
        py = sin(angle) + center_y
        print(px, py, angle, i)

circulo(1)