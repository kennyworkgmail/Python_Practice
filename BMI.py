# 請使用者輸入身高(cm)與體重(kg)，計算並印出 BMI 值與體位判斷
# 雲端編輯2
# 本地端編輯3
height = float(input("請輸入身高(cm): "))
weight = float(input("請輸入體重(kg): "))
bmi = weight / (height / 100) ** 2
if bmi < 18.5:
    print("體位：過輕")
elif bmi < 22:
    print("體位：適中")
elif bmi < 27:
    print("體位：過重")
else:
    print("體位：肥胖")
print("BMI 值：{:.2f}".format(bmi))
# 本地端編輯1
# 本地端編輯2
