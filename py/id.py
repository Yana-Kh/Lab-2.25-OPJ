#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from time import sleep


def check_sum(x):
    y = (5-2*x) / (6 - 5*x + x**2)
    print(f"The result check-function is: {y}")


def s_sum(x):
    n = 1
    term = (1 / (2 ** n) + 1 / (3 ** n)) * (x ** (n - 1))
    epsilon = 1e-7
    ssum = term

    while abs(term) >= epsilon:
        n += 1
        term = (1 / (2 ** n) + 1 / (3 ** n)) * (x ** (n - 1))
        ssum += term

    print(f"The sum S is: {ssum}")


def main():
    x = -0.8

    proc1 = Process(target=check_sum, args=(x,))
    proc2 = Process(target=s_sum, args=(x,))

    proc1.start()
    proc2.start()

    sleep(0.1)

    proc1.terminate()
    proc2.terminate()


if __name__ == "__main__":
    main()