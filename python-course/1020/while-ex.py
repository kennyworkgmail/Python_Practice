"""

設計一個系統選單
====客服系統====
1. 呼叫客服
2. 文字聯系
3. 留下資料
4. 離開系統
================
輸入 1-4 選擇功能,或按 q 離開
================

"""

import time

def system():
    while True:
        try:
            print("\n====客服系統====")
            print("1. 呼叫客服")
            print("2. 文字聯系")
            print("3. 留下資料")
            print("4. 離開系統")
            print("================")
            command = input("輸入 1-4 選擇功能，或按 q 離開: ")
            match command.strip().lower():
                case '1':
                    print("\n\033[32m正在為您呼叫客服，請稍後...\033[0m")
                    time.sleep(2)     # 模擬等待客服接聽
                    print("\n\033[33m當前客服忙線中，請稍後再試或改選其他選項。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                case '2':
                    print("\n\033[32m正在轉接文字聯絡系統，請稍後...\033[0m")
                    time.sleep(0.5)     # 模擬等待客服接聽
                    print("\033[F\033[K" * 2, end="")  # 清除上一行輸出
                    user_message = input("\n請輸入內容: ")
                    time.sleep(2)     # 模擬等待客服接洽
                    print("\n\033[33m當前客服忙線中，我們已收到您的需求，將盡快予您回覆。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                case '3':
                    print("\n\033[32m正在轉接資料庫系統，請稍後...\033[0m")
                    time.sleep(0.5)     # 模擬轉接服務
                    print("\033[F\033[K" * 2, end="")  # 清除上一行輸出
                    phone = input("\n請輸入電話號碼: ")
                    email = input("請輸入電子郵件: ")
                    time.sleep(0.25)     # 模擬三方交握等待時間
                    print("\n\033[33m我們已紀錄您的聯絡方式，將盡快與您聯絡。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                case '4' | 'q':
                    print("\n\033[32m客服系統感謝您的使用，期待下次與您再見！\033[0m\n")
                    break
                case _:
                    raise ValueError("輸入錯誤，請重新輸入！")
        except ValueError as ve:
            time.sleep(1)
            print(f"\n\033[31m{ve}\033[0m")
        except KeyboardInterrupt:
            print("\n\n\033[31m客服系統已中止，感謝您的使用！\033[0m\n")
            break

def main():
    system()

if __name__ == "__main__":
    main()