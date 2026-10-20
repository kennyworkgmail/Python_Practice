for num in range(3):
    print(num)
else:
    print("迴圈結束")


for i in range(9):
    for j in range(9):
        print(f"{i + 1} * {j + 1} = {(i + 1) * (j + 1)}")

"""
經典99乘法表
1 * 1 = 1   2 * 1 = 2   3* 1 = 3

7 * 9 = 63  8 * 9 = 72  9 * 9 = 81   
用for迴圈
"""

for i in range(0, 9, 3):
    for j in range(1, 10):
        print(f"{i + 1} * {j} = {(i + 1) * j:>2d}", end = "\t")
        print(f"{i + 2} * {j} = {(i + 2) * j:>2d}", end = "\t")
        print(f"{i + 3} * {j} = {(i + 3) * j:>2d}")