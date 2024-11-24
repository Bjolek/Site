import sqlite3
class DBmanager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        Create table if not exists Quiz (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT
        );
        """)

        cursor.execute("""

        Create table if not exists Question (
            id INT PRIMARY KEY,
            quize_id INT,
            content TEXT
        );
        """)
        cursor.execute("""

        Create table if not exists Options (
            id INT PRIMARY KEY,
            question_id INT,
            content TEXT,
            is_correct BOOLEAN
        );
        """)
        self.connection.commit()


    def add_quize (self, id, title, description):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Quiz(id, title, description) VALUES (?,?,?)",[id, title, description])
        self.connection.commit()
        cursor.close()

    def add_question(self, id, quize_id, content):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Question(id, quize_id, content) VALUES (?,?,?)", [id, quize_id, content])
        self.connection.commit()
        cursor.close()

    def get_quizzes(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Quiz")
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_questions(self,quize_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Question WHERE quize_id = ?",[quize_id])
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_options(self,quize_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Options WHERE question_id = ?",[quize_id])
        res = cursor.fetchall()
        cursor.close()
        return res


