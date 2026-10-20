a = 10
b = 20

if a < b:
    print("a > b")
    print(f"{a} 大於 {b}")
    print("區塊語法都會被執行")
    
    print("空一行後相同縮排")

if a < b:
    print("a < b 成立")
elif a == b:
    print("a == b 成立")
elif a > b:
    print("a > b 成立")
else:
    print("都不成立")

if a < b and a == 30 and b == 5:
    print("複合條件")


if a < b :
    if a == 30 :
     print("巢狀式條件")