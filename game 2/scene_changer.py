HEIGHT = 500
WIDTH = 900

button_width = 150
button_height = 100

points = [(WIDTH / 2 - button_width / 2, HEIGHT / 2 - button_height / 2),
          (WIDTH / 2 - button_width / 2, HEIGHT / 2 + button_height / 2),
          (WIDTH / 2 + button_width / 2, HEIGHT / 2)]

x0 = points[0][0]
ku = (points[0][1] - points[2][1]) / (points[0][0] - points[2][0])
kd = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0])
lu = points[2][1] - points[2][0] * ku
ld = HEIGHT / 2 + HEIGHT / 2 - lu

def click_analys(x, y):
    if (y - ku*x - lu > 0) and (y - kd * x - ld < 0) and (x > x0):
        return True
    return False