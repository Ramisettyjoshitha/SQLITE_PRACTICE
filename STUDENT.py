import sqlite3
conn=sqlite3.connect('student.db')
c=conn.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS students(
          rollno INTEGER PRIMARY KEY,
          name TEXT,
          marks INTEGER,
          department TEXT
          )
""")
c.execute("DELETE FROM students")
many_students=[
    (153,'junnu',95,'CSE'),
    (155,'josh',45,'AIML'),
    (143,'GOKUL',98,'AIDS'),
    (144,'GITHA',90,'CSE'),
    (200,'HONEY',88,'ECE'),
    (300,'TANU',100,'AIML')]
c.executemany("INSERT INTO studentS VALUES (?,?,?,?)"
              ,many_students)
c.execute("SELECT*FROM students")
records=c.fetchall()
for i in records:
    print(i)
print("students from cse")
c.execute("SELECT*FROM students WHERE department='CSE'")
print(c.fetchall())
print("students above  and equal to90")
c.execute("SELECT*FROM students WHERE marks>=90")
print(c.fetchall())
c.execute("UPDATE students SET marks='85' WHERE name='josh'")
c.execute("SELECT*FROM students WHERE name='josh'")
print(c.fetchone())
print("AFTER DELETED")
c.execute("DELETE FROM students WHERE name='junnu'")
c.execute("SELECT*FROM students")
for j in c.fetchall():
    print(j)
print("DESCENDING ORDER")
c.execute("SELECT rowid,* FROM students ORDER BY marks DESC")
print(c.fetchall())
print("TOP 3")
c.execute("SELECT rowid,*FROM students ORDER BY marks DESC LIMIT 3")
print(c.fetchall())
conn.commit()
conn.close()


