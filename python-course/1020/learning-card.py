# ## 輸入

# 1. 姓名。
# 2. 本期最想完成的作品。
# 3. 每天學習幾小時。
# 4. 每週學習幾天。
# 5. 預計學習幾週。

# ## 輸出

# 1. 姓名。
# 2. 學習目標。
# 3. 每週預計學習時數。
# 4. 預計總學習時數。
# 5. 一句學習提醒。

# ## 要求

# - 使用 `input()` 取得資料。
# - 將每天學習時間轉成小數。
# - 將每週學習天數與學習週數轉成整數。
# - 計算每週與總學習時數。
# - 使用 f-string 輸出結果。
# - 變數使用 `snake_case`。
# - 從終端機執行 `learning_card.py`。

from dataclasses import dataclass

@dataclass
class StudyPlan:
    """
    沒什麼額外功能的變數型別
    """
    
    name: str = ""
    learning_objectives: str = ""
    hours: float = 0.0
    days: float = 0.0
    weeks: float = 0.0
    hours_per_week: float = 0.0
    total_hours: float = 0.0
    
    def __post_init__(self):
        """
        後初始化
        """
        
        self.__checkType()
    
    def __checkType(self):
        """
        檢查變數是否合規
        """
        
        # isinstance 同時允許 int 與 float
        if not isinstance(self.name, str) or not isinstance(self.learning_objectives, str):
            raise ValueError("參數輸入錯誤，請重新輸入文字！")
        
        numeric_fields = [
            self.hours, self.days, self.weeks, 
            self.hours_per_week, self.total_hours
        ]
        
        for field in numeric_fields:
            if not isinstance(field, (int, float)):
                raise ValueError("參數輸入錯誤，請重新輸入數字！")
    
    def normalize(self):
        """
        將天數和週數整數化(題目要求)
        """
        
        self.days  = int(self.days)
        self.weeks = int(self.weeks)

def accessInput():
    """
    接收使用者輸入並整理參數
    """
    
    output = StudyPlan()
    output.name = input("請輸入姓名：")                        # 讓使用者輸入姓名
    output.learning_objectives = input("本期最想完成的作品：") # 讓使用者輸入學習目標
    while True:     # 讓使用者輸入每天學習幾小時，並檢查輸入是否為數字
        try:
            output.hours = input("每天學習幾小時：")
            if(output.hours == ""):
                output.hours = 0
                break
            output.hours = float(output.hours)
            if output.hours < 0 or output.hours > 24:
                print("\n\033[31m請輸入 0-24 的數字！\033[0m\n")
                continue
            break
        except ValueError:
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")
    while True:     # 讓使用者輸入每週學習幾天，並檢查輸入是否為數字
        try:
            output.days = input("每週學習幾天：")
            if(output.days == ""):
                output.days = 0
                break
            output.days = float(output.days)
            if output.hours == 0:
                print("\n\033[33m每天學習時數為 0，自動修正為 0！\033[0m\n")
            elif output.days <= 0 or output.days > 7:
                print("\n\033[31m請輸入 > 0 且 ≤ 7 的數字！\033[0m\n")
                continue
            break
        except ValueError:
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")
    while True:     # 讓使用者輸入預計學習幾週，並檢查輸入是否為數字
        try:
            output.weeks = input("預計學習幾週：")
            if(output.weeks == ""):
                output.weeks = 0
                break
            output.weeks = float(output.weeks)
            if output.days == 0:
                print("\n\033[33m每天學習時數為 0，自動修正為 0！\033[0m\n")
            elif output.weeks <= 0:
                print("\n\033[31m請輸入正整數！\033[0m\n")
                continue
            break
        except ValueError:
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")

    output.hours_per_week = output.hours * output.days if output.weeks > 0 else 0 # 計算每週預計學習時數
    output.total_hours    = output.hours * output.days * output.weeks             # 計算預計總學習時數
    output.normalize()                                                            # 將每週學習天數、學習週數轉成整數

    return output

def main():
    """
    主程式
    """
    
    try:
        output = accessInput()

        print("\n" + "-" * 40 + "\n")
        print(f"姓名：\033[32m{output.name}\033[0m")
        print(f"學習目標：\033[32m{output.learning_objectives}\033[0m")
        print(f"預計每週學習時數：\033[32m{output.hours_per_week:.2f}\033[0m 小時")
        print(f"預計總學習時數：\033[32m{output.total_hours:.2f}\033[0m 小時")
    except KeyboardInterrupt:
        print("\n\n\033[33m程式已中止，感謝使用本程式！\033[0m\n")

if __name__ == "__main__":
    main()