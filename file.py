import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def pack_circles(rectangle_width, rectangle_height, circle_radius):
    circles = []
    
    x = circle_radius
    while x < rectangle_width:
        y = circle_radius
        while y < rectangle_height:
            circles.append((x, y, circle_radius))
            y += 2 * circle_radius
        x += 2 * circle_radius

    return circles

def visualize_circles(rectangle_width, rectangle_height, circle_radius):
    circles = pack_circles(rectangle_width, rectangle_height, circle_radius)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, rectangle_width)
    ax.set_ylim(0, rectangle_height)

    for circle in circles:
        circle_obj = Circle((circle[0], circle[1]), circle[2], fill=False, edgecolor='blue')
        ax.add_patch(circle_obj)

    plt.show()

rectangle_width = 10
rectangle_height = 6
circle_radius = 1

visualize_circles(rectangle_width, rectangle_height, circle_radius)
