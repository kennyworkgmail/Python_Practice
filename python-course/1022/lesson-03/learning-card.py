from dataclasses import dataclass

# 定義資料型別 StudyPlan
@dataclass
class StudyPlan:
    """
    定義資料型別 StudyPlan
    """
    
    name: str = ""
    learning_objectives: str = ""
    hours: float = 0.0
    days: float = 0.0
    weeks: float = 0.0
    hours_per_week: float = 0.0
    total_hours: float = 0.0
    
    # 後初始化
    def __post_init__(self):
        """
        後初始化
        """
        
        self.__checkType()
    
    # 檢查初始化的變數是否合規
    def __checkType(self):
        """
        檢查初始化的變數是否合規
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
    
    # 將天數和週數整數化(題目要求)
    def normalize(self):
        """
        將天數和週數整數化(題目要求)
        """
        
        self.days  = int(self.days)
        self.weeks = int(self.weeks)

# 接收使用者輸入並整理
def accessInput():
    """
    接收使用者輸入並整理
    """
    
    inputError = False
    output = StudyPlan()
    # 讓使用者輸入姓名，並去除前後空白
    output.name = input("請輸入姓名：").strip()
    # 讓使用者輸入學習目標，並去除前後空白
    output.learning_objectives = input("本期最想完成的作品：").strip()
    # 讓使用者輸入每天學習幾小時，並檢查輸入是否為數字
    while True:
        try:
            output.hours = input("每天學習幾小時：")
            # 如果輸入不合規，重置輸出顯示
            if inputError:
                inputError = False
                print("\033[F\033[K" * 5, end = "")
                print(f"預計學習幾週：{output.hours}")
            # 無輸入預設為 0
            if(output.hours == ""):
                output.hours = 0
                break
            output.hours = float(output.hours)
            # 一天只能有 0~ 24 小時
            if output.hours < 0 or output.hours > 24:
                inputError = True
                print("\n\033[31m請輸入 0-24 的數字！\033[0m\n")
                continue
            break
        # 輸入不合規
        except ValueError:
            inputError = True
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")
    # 讓使用者輸入每週學習幾天，並檢查輸入是否為數字
    while True:
        # 小時數為 0，亦設為 0
        if output.hours == 0:
            output.days = 0
            print("\033[33m每週學習天數自動填入: 0\033[0m\n")
            break
        try:
            output.days = input("每週學習幾天：")
            # 如果輸入不合規，重置輸出顯示
            if inputError:
                inputError = False
                print("\033[F\033[K" * 5, end = "")
                print(f"預計學習幾週：{output.days}")
            # 無輸入預設為 0
            if(output.days == ""):
                output.days = 0
                break
            output.days = float(output.days)
            # 一週只能有 0 ~ 7 天
            if output.days <= 0 or output.days > 7:
                inputError = True
                print("\n\033[31m請輸入 > 0 且 ≤ 7 的數字！\033[0m\n")
                continue
            break
        # 輸入不合規
        except ValueError:
            inputError = True
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")
    # 讓使用者輸入預計學習幾週，並檢查輸入是否為數字
    while True:
        # 天數或小時數為 0，亦設為 0
        if output.days == 0:
            output.weeks = 0
            print("\033[33m預計學習週數自動填入: 0\033[0m\n")
            break
        try:
            output.weeks = input("預計學習幾週：")
            # 如果輸入不合規，重置輸出顯示
            if inputError:
                inputError = False
                print("\033[F\033[K" * 5, end = "")
                print(f"預計學習幾週：{output.weeks}")
            # 無輸入預設為 0
            if(output.weeks == ""):
                output.weeks = 0
                break
            output.weeks = float(output.weeks)
            # 週數不能 < 0
            if output.weeks <= 0:
                inputError = True
                print("\n\033[31m請輸入正整數！\033[0m\n")
                continue
            break
        # 輸入不合規
        except ValueError:
            inputError = True
            print("\n\033[31m請輸入阿拉伯數字！\033[0m\n")
    
    # 每週預計學習時數
    output.hours_per_week = output.hours * output.days if output.weeks > 0 else 0
    # 預計總學習時數
    output.total_hours    = output.hours * output.days * output.weeks
    # 將每週學習天數、學習週數轉成整數
    output.normalize()

    return output

# 主執行函數
def main():
    """
    重複執行 accessInput() 並輸出顯示
    """
    
    try:
        while True:
            print()
            output = accessInput()
            print("\n" + "-" * 40 + "\n")
            print(f"姓名：\033[32m{output.name}\033[0m")
            print(f"學習目標：\033[32m{output.learning_objectives}\033[0m")
            print(f"預計每週學習時數：\033[32m{output.hours_per_week:.2f}\033[0m 小時")
            print(f"預計總學習時數：\033[32m{output.total_hours:.2f}\033[0m 小時")
            check = input("\n\033[33m是否要退出本程式?\033[0m (y/N): ")
            # 退出程式
            if check.strip().lower() == 'y':
                print("\033[F\033[K" + "-" * 40 + "\n\n\033[32m程式已終止，感謝使用本程式，祝您有美好的一天！\033[0m\n")
                break
            # 繼續學習計畫設計
            else:
                print("\033[F\033[K" + "-" * 40)
                continue
    # Ctrl+C 強迫退出程式
    except KeyboardInterrupt:
        print("\n\n\033[33m程式已中斷，感謝您的使用，期待與您再次相遇！\033[0m\n")

# 主程式 __main__ 進入點
if __name__ == "__main__":
    main()