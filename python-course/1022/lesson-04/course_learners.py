"""

完成一個程式：

- 每位學員使用一個 Dictionary。
- 清除姓名與學習目標前後的空白。
- 缺少學習目標時，使用「未提供目標」。
- 將每天時數轉成 `float`，每週天數轉成 `int`。
- 計算每位學員的 `weekly_hours`。
- 保留原始 `raw_learners`，不要直接修改。
- 使用函式處理一位學員。
- 使用另一個函式處理多位學員。
- 最後逐筆印出整理後的 `learners`。

"""

raw_learners = [
    {
        "name": "  阿哲",
        "hours_per_day": "1.5",
        "days_per_week": 4,
        "goal": "完成 Python 作品",
    },
    {
        "name": "小玲 ",
        "hours_per_day": "2",
        "days_per_week": 3,
        "goal": "  熟悉資料處理  ",
    },
    {
        "name": "小安",
        "hours_per_day": "1",
        "days_per_week": 2,
    },
]

learners = []

def process_learner(raw_learner):
    clean_learner = {}
    clean_learner["name"] = raw_learner["name"].strip()
    clean_learner["hours_per_day"] = float(raw_learner["hours_per_day"])
    clean_learner["days_per_week"] = int(raw_learner["days_per_week"])
    clean_learner["goal"] = raw_learner.get("goal", "未提供目標").strip()
    clean_learner["weekly_hours"] = clean_learner["hours_per_day"] * clean_learner["days_per_week"]
    return clean_learner

def process_learners(raw_learner):
    for raw_learner in raw_learners:
        clean_learner = process_learner(raw_learner)
        learners.append(clean_learner)

def main():
    process_learners(raw_learners)

    for learner in learners:
        print(learner)

if __name__ == "__main__":
    main()