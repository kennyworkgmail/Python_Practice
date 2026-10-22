from operator import index

import mysql.connector

connection = mysql.connector.connect(
    host="10.167.215.60",
    port=3306,
    user="python_course",
    password="0000",
    database="python_course",
)

print("MariaDB 連線成功")

cursor = connection.cursor(dictionary=True)

cursor.execute(
    "SELECT COUNT(*) AS total FROM learners"
)

row = cursor.fetchone()

if row is None:
    print("沒有查到資料")
else:
    print(row["total"])

cursor.execute(
    """
    SELECT id, name, weekly_hours, goal
    FROM learners
    ORDER BY id
    """
)

rows = cursor.fetchall()

if rows is None:
    print("沒有查到資料")
else:
    for row in rows:
        print(row["name"])
    for row in rows:
        if index == 1:
            tuple_keys = tuple(row.keys())
        tuple_values = tuple(row.values())
        print(tuple_keys)
        print(tuple_values)
        # for key, value in row.items():
        #     print(tuple([key, value]))



connection.close()