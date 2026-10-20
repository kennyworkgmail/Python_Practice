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

# 客服系統呼叫
def system():
    # 多次呼叫客服系統
    while True:
        try:
            print("\n====客服系統====")
            print("1. 呼叫客服")
            print("2. 文字聯系")
            print("3. 留下資料")
            print("4. 離開系統")
            print("================")
            command = input("輸入 1-4 選擇功能，或按 q 離開: ")
            # 根據對應指令操作
            match command.strip().lower():
                # 呼叫客服
                case '1':
                    print("\n\033[32m正在為您呼叫客服，請稍後...\033[0m")
                    time.sleep(2)     # 模擬等待客服接聽
                    print("\033[F\033[K" * 2, end="")  # 清除上一行輸出
                    print("\n\033[33m當前客服忙線中，請稍後再試或改選其他選項。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                # 文字聯系
                case '2':
                    print("\n\033[32m正在轉接文字聯絡系統，請稍後...\033[0m")
                    time.sleep(0.5)     # 模擬等待客服接聽
                    print("\033[F\033[K" * 2, end="")  # 清除上一行輸出
                    user_message = input("\n請輸入內容: ")
                    time.sleep(2)     # 模擬等待客服接洽
                    print("\n\033[33m當前客服忙線中，我們已收到您的需求，將盡快予您回覆。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                # 留下資料
                case '3':
                    print("\n\033[32m正在轉接資料庫系統，請稍後...\033[0m")
                    time.sleep(0.5)     # 模擬轉接服務
                    print("\033[F\033[K" * 2, end="")  # 清除上一行輸出
                    phone = input("\n請輸入電話號碼: ")
                    email = input("請輸入電子郵件: ")
                    time.sleep(0.25)     # 模擬三方交握等待時間
                    print("\n\033[33m我們已紀錄您的聯絡方式，將盡快與您聯絡。\033[0m")
                    time.sleep(0.25)     # 轉接回主選單延遲
                # 離開系統
                case '4' | 'q':
                    print("\n\033[32m*** 感謝使用本系統，祝您有美好的一天！ ***\033[0m\n")
                    break
                # 指令錯誤
                case _:
                    raise ValueError("輸入錯誤，請重新輸入！")
        # 輸入指令不合規
        except ValueError as ve:
            time.sleep(1)
            print(f"\n\033[31m{ve}\033[0m")
        # Ctrl+C 強迫退出程式
        except KeyboardInterrupt:
            print("\n\n\033[33m客服系統已中止，感謝您的使用，期待與您再次相遇！\033[0m\n")
            break

# 主執行函數
def main():
    system()

# 主程式 __main__ 進入點
if __name__ == "__main__":
    main()