# Copyright (c) 2022 Shuhei Nitta. All rights reserved.
import random
import math


def random_walk(x=0, y=0, d=1, step=100):
    for _ in range(step):
        theta = 2 * math.pi * random.random()
        x += d * math.cos(theta)
        y += d * math.sin(theta)
    return x, y


if __name__ == "__main__":
    results = [random_walk() for _ in range(100)]
    distances = [math.hypot(x, y) for (x, y) in results]
    avg = sum(distances) / len(distances)
    print("Average:", avg)
