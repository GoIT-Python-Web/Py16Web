import random

width = 10
height = 5


def is_inside(w, h, x, y) -> bool:
    return y <= (h / w) * x


def area_monte_carlo(width, height, num_experiments):
    avg_area = 0

    for _ in range(num_experiments):
        points = [(random.uniform(0, width), random.uniform(0, height)) for _ in range(15_000)]
        inside_points = [point for point in points if is_inside(width, height, point[0], point[1])]  # filter

        N = len(points)
        M = len(inside_points)
        area = (M / N) * (width * height)
        avg_area += area
    avg_area /= num_experiments
    return avg_area


if __name__ == '__main__':
    S = (width * height) / 2
    Sm = area_monte_carlo(width, height, 100000)
    print(f"Area of triangle = {S}")
    print(f"Area of triangle: Monte Carlo = {Sm}")
