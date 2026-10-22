def calculate_total_hours(hours_per_day, days):
    """
    說明 calculate_total_hours 怎麼使用
    hours_per_day 是多少工時
    """
    
    total_hours = hours_per_day * days
    return total_hours

def myfunc1(args1="預設值"):
    print(args1)

def myfunc2(args1, args2):
    # 如果傳入的參數沒有預設值，代表是必要參，呼叫時不能省略
    print("args1", args1)
    print("args2", args2)

# 主程式進入點
# hours_per_day = float(input("每天學習幾小時："))
# days = int(input("學習幾天："))

# total_hours = calculate_total_hours(hours_per_day, days)

# print("--- 執行結果 ---")
# print(f"總學習時數：{total_hours:.1f} 小時")

myfunc1()
myfunc1("指定內容")
# myfunc2()
myfunc2("參數1", "參數2")
myfunc2(args2 = "參數1", args1 = "參數2")