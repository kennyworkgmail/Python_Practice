"""

if 練習
1. 設計一個程式,接收使用者輸入考試分數( 0-100 分)
2. 每 10 分為一個級距, A 級為 90 以上(包含 90), B 級為 80 以上, 類推至 E 級, 輸出分數轉換後的等級
3. 不滿 E 級就輸出不及格
4. 使用 if 完成

"""

def score_grade():
    while True:
        try:
            score = float(input("\n請輸入考試分數(0-100): "))
            if score < 0 or score > 100:
                print("\n\033[33m請輸入 0-100 的分數！\033[0m")
                continue
            elif int(score) != score:
                print("\n\033[33m分數應為整數！\033[0m")
                continue
            else:
                int(score)
                print("\n" + "=" * 40)
                print(f"\n您的分數是: {score} 分，評級為: ", end="")
                if score >= 90 and score <= 100:
                    print("\033[32mA\033[0m 級")
                elif score >= 80 and score < 90:
                    print("\033[32mB\033[0m 級")
                elif score >= 70 and score < 80:
                    print("\033[32mC\033[0m 級")
                elif score >= 60 and score < 70:
                    print("\033[33mD\033[0m 級")
                elif score >= 50 and score < 60:
                    print("\033[33mE\033[0m 級")
                else:
                    print("\033[31m不及格！\033[0m")
            continue_input = input("\n是否要繼續輸入分數評級？ (Y/n): ")
            if continue_input.lower() == "n":
                print("\033[F\033[K" * 2 + "\n\033[32m***感謝使用本程式，祝您有美好的一天！***\033[0m\n")
                break
            else:
                print("\033[F\033[K" * 2 + "\n" + "=" * 40) # 清除上一行輸入提示
                continue
        except ValueError:
            print("\n\033[31m請輸入阿拉伯數字！\033[0m")
        except KeyboardInterrupt:
            print("\n\n\033[33m程式已中止，感謝使用本程式！\033[0m\n")
            break

def main():
    score_grade()

if __name__ == "__main__":
    main()