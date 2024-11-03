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
