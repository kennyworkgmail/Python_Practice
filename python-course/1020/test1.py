a = 100
b = 100
c = 10
d = a if a > b else b
print(a == b)
print(a is b)
print(a is c)
print(d)

name1 = "小明"
hours = 2
mystr1 = f"{name1}每天學習{hours}小時"
mystr2 = f"{name1}每天學習{hours + 2}小時"   # f-string 可以直接在大括號內做運算
print(f"{name1}每天學習{hours}小時")
print(mystr1)
print(mystr2)

print("abc", "123")
print("abc", "123", sep="~~~", end="@@@")   # sep:分隔符號, end:結尾符號
print("華麗的沒換行")

average = 83.4561
print(f"平均分數: {average:.2f}")
print(f"平均分數: {average:.4f}")
print(f"平均分數: {average:.6f}")

name2 = input("請輸入姓名: ")
print(f"您好! {name2} 歡迎來到Python課程，型別是{type(name2)}")

age = int(input("請輸入年齡: "))
print(f"您的年齡是: {age} 歲，請輸入正整數，型別是{type(age)}")

