import sqlite3

class Person:
    def __init__(self, id_num=-1, first="", last="", age=-1):
        self.id_num = id_num
        self.first = first
        self.last = last
        self.age = age
        self.conn = sqlite3.connect('mydata.db')
        self.cursor = self.conn.cursor()

    def loadP(self, id_num):
        self.cursor.execute(f"""
        SELECT * FROM persons WHERE id = {id_num}
        """)

        results = self.cursor.fetchone()

        self.id_num = id_num
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insertP(self):
        self.cursor.execute(f"""
        INSERT INTO persons VALUES ({self.id_num}, '{self.first}', '{self.last}', {self.age})
        """)
        self.conn.commit()
        self.conn.close()

# conn = sqlite3.connect('mydata.db')

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons (
#     id INTEGER PRIMARY KEY,
#     f_name TEXT,
#     l_name TEXT,
#     age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
# (1, 'Paul', 'Smith', 24),
# (2, 'Mark', 'Smuth', 20),
# (3, 'Mike', 'Smith', 28)
# """)

# cursor.execute("""
# SELECT * FROM persons
# WHERE l_name = 'Smith'
# """)

# p1 = Person()
# p1.loadP(1)
# print(p1.first)
# print(p1.last)
# print(p1.age)

# p1 = Person(7, "John", "Doe", 26)
# p1.insertP()

# conn.commit()
# conn.close()

conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM persons")

results = cursor.fetchall()

print(results)

conn.close()