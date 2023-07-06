import sqlite3

db = "MazeGame.db"
t = "MazeGameMetrics"

con = sqlite3.connect(db)
cur = con.cursor()
print("Before: ")
print(cur.execute("SELECT name FROM sqlite_master").fetchall())
cur.execute(str("DROP TABLE "+t))
print("After: ")
print(cur.execute("SELECT name FROM sqlite_master").fetchall())