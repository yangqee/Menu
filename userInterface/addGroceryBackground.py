import sqlite3
import sys

from addGroceryFrame import Ui_AddGroceryFrame
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainBackground
from userInterface import TOOLS


class AddGroceryFrame(QMainWindow, Ui_AddGroceryFrame):

    def __init__(self, parent=None):
        super(AddGroceryFrame, self).__init__(parent)
        self.setupUi(self)
        self.conn = sqlite3.connect('user_data_ia.db')
        self.cursor = self.conn.cursor()

        self.addGroceryBtn.clicked.connect(self.addGro)
        self.backBtn.clicked.connect(self.back)

    def addGro(self):

        gro_name = self.groceryNameEntry.toPlainText()
        gro_num = self.groceryNumEntry.toPlainText()
        expdate = self.expiryDateEdit.date()
        gro_expdate = expdate.toString('yyyy-MM-dd')
        a = self.saveGro(gro_name, gro_num, gro_expdate)


        if a > 0:
            successfulSave = 'Save Successful! \nthis grocery is now saved please enjoy!'
            TOOLS.messageBox(self, successfulSave)
            self.back()
        else:
            wentWrong = 'Something went wrong'
            TOOLS.messageBox(self, wentWrong)

    def saveGro(self, gro_name, gro_num, gro_expdate):

        # check if there is an entry
        self.cursor.execute('SELECT * FROM groceries WHERE g_name=?', (gro_name,))
        existing_name = self.cursor.fetchone()


        if existing_name != None:
            existName = 'Saving failed\nSorry, it seems like this name is already used by another entry'
            TOOLS.messageBox(self, existName)
            return 0
        else:
            self.cursor.execute('INSERT INTO groceries (g_name, g_num, g_expdate) VALUES(?,?,?)',
                                (gro_name.lower(), gro_num, gro_expdate))
            self.conn.commit()
            return 1

    def back(self):
        self.close()
        # mainWin = mainBackground.MainFrame(self)
        # mainWin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    addGroceryWin = AddGroceryFrame()
    addGroceryWin.show()

    sys.exit(app.exec_())
