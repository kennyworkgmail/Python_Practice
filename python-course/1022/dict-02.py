learner = {
    "name": "小明",
    "hours_per_week": 8,
    "goal": "學會 Python",
}

raw_learner = {
    "name": "  小明 ",
    "hours_per_day": "2",
    "goal": "",
}

name = raw_learner["name"].strip()
hours_per_day = float("2")
days_per_week = int("5")
weekly_hours = hours_per_day * days_per_week
print(weekly_hours)



for key, value in learner.items():
    print(key, value)