import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from loginFrame import Ui_loginFrame
import TOOLS
import re

from userInterface import mainBackground


class LoginFrame(QMainWindow, Ui_loginFrame):
    def __init__(self, parent=None):
        super(LoginFrame, self).__init__(parent)
        self.setupUi(self)
        # connecting the database and create table
        self.connectDataBase()

        # adding the login button signal
        # self.loginBtn.clicked.connect(lambda: self.login(cursor))
        self.loginBtn.clicked.connect(self.login)
        # adding the register button signal
        # self.registerBtn.clicked.connect(lambda: self.register(cursor, conn))
        self.registerBtn.clicked.connect(self.register)

    def connectDataBase(self):
        # creating the database connection
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()

        # creating the database
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS menues(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            method TEXT NOT NULL,
            method_pic VARCHAR(100) ,
            estimate_time TIME NOT NULL            
            )
            ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu_ingredients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            ingredient VARCHAR(100) NOT NULL,
            ingredient_num INTEGER NOT NULL
            )
            ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS groceries(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            g_name VARCHAR(100) NOT NULL,
            g_num INTEGER NOT NULL,
            g_expdate DATE NOT NULL
            )
            ''')
        conn.commit()
        return (cursor, conn)

    # the algorithm for login
    # def login(self, cursor):
    def login(self):
        username = self.username_text.toPlainText()
        password = self.password_text.toPlainText()

        # reconnect
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()

        # check if there is this user
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()

        if user:

            notice = 'Login successful!\nWelcome {}, happiness is in every bite! Do not forget, your password is {}'.format(
                username, password)
            TOOLS.messageBox(self,notice)
            self.close()
            mainWin = mainBackground.MainFrame(self)
            mainWin.show()
        else:
            wrongLogin = 'Login failed\n Wrong username or password'
            TOOLS.messageBox(self,wrongLogin)

    # the algorithm for registering
    # def register(self, cursor, conn):
    # def register(self):
    #     # reconnect
    #     conn2 = sqlite3.connect('user_data_ia.db')
    #     cursor2 = conn2.cursor()
    #
    #     r_username = self.username_text.toPlainText()
    #     r_password = self.password_text.toPlainText()
    #     # check if there is an entry
    #     cursor2.execute('SELECT * FROM users WHERE username=?', (r_username,))
    #     existing_user = cursor2.fetchone()
    #
    #     if existing_user:
    #         existUser = 'Register failed\nThis username is already used'
    #         TOOLS.messageBox(existUser)
    #     else:
    #         a, b = self.isValidPass(r_password)
    #         # adding the new account into the data base
    #         if (a, b) == (True, 0):
    #             cursor2.execute('INSERT INTO users (username, password) VALUES(?,?)', (r_username, r_password))
    #             conn2.commit()
    #             if cursor2.rowcount > 0:
    #                 regSuc = 'Register success\nYour account as been successfully created please login'
    #                 TOOLS.messageBox(self, regSuc)
    #             else:
    #                 regSuc = 'Something wrong with your db'
    #                 TOOLS.messageBox(self, regSuc)
    #         elif (a, b) == (False, 1):
    #             regError = 'Password Invalid\nThe password must be 6 characters or more'
    #             TOOLS.messageBox(self,regError)
    #         else:
    #             regError2 = 'Password Invalid\nThe password must be a combination of numbers and letters'
    #             TOOLS.messageBox(self,regError2)
    def register(self):
        try:
            # reconnect
            conn = sqlite3.connect('user_data_ia.db')
            cursor = conn.cursor()

            r_username = self.username_text.toPlainText()
            r_password = self.password_text.toPlainText()
            # check if there is an entry
            cursor.execute('SELECT * FROM users WHERE username=?', (r_username,))
            existing_user = cursor.fetchone()

            if existing_user:
                existUser = 'Register failed\nThis username is already used'
                TOOLS.messageBox(self,existUser)
            else:
                a, b = self.isValidPass(r_password)
                # adding the new account into the data base
                if (a, b) == (True, 0):
                    cursor.execute('INSERT INTO users (username, password) VALUES(?,?)', (r_username, r_password))
                    conn.commit()
                    if cursor.rowcount > 0:
                        regSuc = 'Register success\nYour account as been successfully created please login'
                        TOOLS.messageBox(self, regSuc)
                    else:
                        regSuc = 'Something wrong with your db'
                        TOOLS.messageBox(self, regSuc)
                elif (a, b) == (False, 1):
                    regError = 'Password Invalid\nThe password must be 6 characters or more'
                    TOOLS.messageBox(self, regError)
                else:
                    regError2 = 'Password Invalid\nThe password must be a combination of numbers and letters'
                    TOOLS.messageBox(self, regError2)
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
    def isValidPass(self, rpassword):
        pattern = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        valid_pattern = bool(re.match(pattern, rpassword))
        invalid_type = 0

        if len(rpassword) < 6:
            valid = False
            invalid_type = 1

        elif valid_pattern is False:
            valid = False
            invalid_type = 2

        else:
            valid = True

        return valid, invalid_type


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWin = LoginFrame()
    loginWin.show()

    sys.exit(app.exec_())
