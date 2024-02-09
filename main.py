import asyncio
import math


async def task1(a, b):
    c = a * b
    await asyncio.sleep(3)
    print(c)
    print("Task 1 completed")
    print("_______________")


async def task2(a, b):
    c = a + b
    await asyncio.sleep(2)
    print(c)
    print("Task 2 completed")
    print("_______________")


async def task3(a, b):
    c = a % b
    await asyncio.sleep(1)
    print(c)
    print("Task 3 completed")
    print("_______________")


async def task4(a, b):
    c = a - b
    await asyncio.sleep(5)
    print(c)
    print("Task 4 completed")
    print("_______________")


async def task5(a, b):
    c = a ** b
    await asyncio.sleep(4)
    print(c)
    print("Task 5 completed")
    print("_______________")


async def task6(a, b):
    c = math.log(a, b)
    await asyncio.sleep(0)
    print(c)
    print("Task 6 completed")
    print("_______________")


async def task7(a, b):
    c = a // b
    await asyncio.sleep(1)
    print(c)
    print("Task 7 completed")
    print("_______________")


async def task8(a, b):
    c = a + b
    await asyncio.sleep(6)
    print(c)
    print("Task 8 completed")
    print("_______________")


async def task9(a, b):
    c = a * b
    await asyncio.sleep(7)
    print(c)
    print("Task 9 completed")
    print("_______________")


async def task10(a, b):
    c = pow(a, b)
    await asyncio.sleep(8)
    print(c)
    print("Task 10 completed")
    print("_______________")


async def task11(a, b):
    c = a / b
    await asyncio.sleep(9)
    print(c)
    print("Task 11 completed")
    print("_______________")


async def task12(a, b):
    c = pow(a, 2) + pow(b, 2)
    await asyncio.sleep(10)
    print(c)
    print("Task 12 completed")
    print("_______________")


async def task13(a, b):
    c = pow(a, 3) + pow(b, 2)
    await asyncio.sleep(11)
    print(pow(c, 0.5))
    print("Task 13 completed")
    print("_______________")


async def task14(a, b, d, e):
    c = a * b / d + e
    await asyncio.sleep(12)
    print(c)
    print("Task 14 completed")
    print("_______________")


async def task15(a, b):
    c = pow(a, a * b)
    await asyncio.sleep(13)
    print(c)
    print("Task 15 completed")
    print("_______________")


async def task16(a, b):
    c = pow(a, a - b)
    await asyncio.sleep(14)
    print(c)
    print("Task 16 completed")
    print("_______________")


async def task17(a, b):
    c = (a - b) * (a + b)
    await asyncio.sleep(15)
    print(c)
    print("Task 17 completed")
    print("_______________")


async def task18(a, b):
    c = (a - b) / (a + b)
    await asyncio.sleep(16)
    print(c)
    print("Task 18 completed")
    print("_______________")


async def task19(a, b):
    c = pow(a, 2) // pow(b, 2)
    await asyncio.sleep(17)
    print(c)
    print("Task 19 completed")
    print("_______________")


async def task20(a, b):
    c = a * b
    c = c + b + a
    await asyncio.sleep(18)
    print(c)
    print("Task 20 completed")
    print("_______________")


async def main():
    await asyncio.gather(task1(4, 2), task2(1, 2), task3(5, 2), task4(10, 8), task5(5, 5),
                         task6(3, 5193), task7(356, 5), task8("Hello\t", "Elshodbek"), task9("hello\t", 1),
                         task10(3, 6), task11(5555, 49), task12(3, 4), task13(5, 85),
                         task14(5, 55, 13, 9), task15(2, 9), task16(20, 150), task17(45, 20),
                         task18(20, -78), task19(20, 12), task20(15, 23))

asyncio.run(main())
