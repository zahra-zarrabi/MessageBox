from sqlite3 import connect
from datetime import datetime

class Database:

    @staticmethod
    def my_insert(name,text):
        try:
            my_con = connect("MessageBox.db")
            my_cursor = my_con.cursor()
            time='{0:20%y-%m-%d \n %H:%M}'.format(datetime.now())
            my_cursor.execute(f"INSERT INTO messages(name,text,time)VALUES('{name}','{text}','{time}')")
            my_con.commit()
            my_cursor.close()
            return True
        except:
            return False

    @staticmethod
    def my_select():
        try:
            my_con=connect("MessageBox.db")
            my_cursor=my_con.cursor()
            my_cursor.execute("SELECT * FROM messages")
            result=my_cursor.fetchall()
            my_cursor.close()
            return result
        except:
            return []

    @staticmethod
    def my_delete(id):
        try:
            my_con = connect("MessageBox.db")
            my_cursor = my_con.cursor()
            my_cursor.execute(f"DELETE FROM messages WHERE id={id}")
            my_con.commit()
            my_cursor.close()
            return True
        except:
            return False

    @staticmethod
    def all_delete():
        my_con = connect("MessageBox.db")
        my_cursor = my_con.cursor()
        my_cursor.execute("DELETE FROM messages")
        my_con.commit()
        my_cursor.close()

    @staticmethod
    def my_update(self):
        pass