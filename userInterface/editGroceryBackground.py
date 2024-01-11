import sqlite3

from PyQt5.QtCore import QDate

from editGroceryFrame import Ui_editGroceryFrame
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox
import mainBackground

from userInterface import TOOLS


class EditGroceryFrame(QMainWindow, Ui_editGroceryFrame):
    def __init__(self, gro_name='', parent=None):
        super(EditGroceryFrame, self).__init__(parent)
        self.setupUi(self)
        self.conn = sqlite3.connect('user_data_ia.db')
        self.cursor = self.conn.cursor()
        # creating the database for groceries
        self.cursor.execute('''
                                      CREATE TABLE IF NOT EXISTS groceries(
                                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                                          g_name VARCHAR(100) NOT NULL,
                                          g_num INTEGER NOT NULL,
                                          g_expdate TEXT NOT NULL
                                      )
                                      ''')
        self.conn.commit()
        self.showinfo(gro_name)
        self.editGroceryBtn.clicked.connect(lambda: self.finishEditGro(gro_name))
        self.areThereLeftovers.toggled.connect(self.showLeftOvers)
        self.backBtn.clicked.connect(self.back)


    def finishEditGro(self, or_name):
        gro_name = self.groceryNameEntryed.toPlainText()
        gro_num = self.groceryNumEntryed.toPlainText()
        expdate = self.expiryDateEdited.date()
        gro_expdate = expdate.toString('yyyy-MM-dd')
        gro_num2 = self.leftoverEntry.toPlainText()
        expdate2 = self.expiryDateEditLeftover.date()
        gro_expdate2 = expdate2.toString('yyyy-MM-dd')
        if self.areThereLeftovers.isChecked() == True:
            self.saveEditGro2(gro_name,gro_num,gro_expdate, gro_num2, gro_expdate2,or_name)
        else:
            self.saveEditGro(gro_name, gro_num, gro_expdate,or_name)
        self.cursor.execute('SELECT * FROM groceries WHERE g_name=? ORDER BY id DESC LIMIT 1', (gro_name,))
        info = self.cursor.fetchall()
        if self.areThereLeftovers.isChecked() == True and str(info[0][2]) != gro_num:
            error = 'Saving failed\nSorry, it seems like this entry is not successfully saved'
            TOOLS.messageBox(self, error)
        elif self.areThereLeftovers.isChecked() == True and str(info[0][2]) != gro_num2:
            error = 'Saving failed\nSorry, it seems like this entry is not successfully saved'
            TOOLS.messageBox(self, error)
        else:
            successfulSave = 'Save Successful! \nthis grocery is now saved please enjoy!'
            TOOLS.messageBox(self, successfulSave)
            self.back()

    def saveEditGro(self,gname,gnum,gexpdate,or_name):
        self.cursor.execute('DELETE FROM groceries WHERE g_name=?', (or_name,))
        self.cursor.execute('INSERT INTO groceries (g_name, g_num, g_expdate) VALUES(?,?,?)',
                            (gname.lower(), gnum, gexpdate))
        self.conn.commit()


    def saveEditGro2(self,gname,gnum,gexpdate,gnum2,gexpdate2,or_name):

        self.cursor.execute('DELETE FROM groceries WHERE g_name=?', (or_name,))
        self.cursor.execute('INSERT INTO groceries (g_name, g_num, g_expdate) VALUES(?,?,?)',
                            (gname.lower(), gnum, gexpdate))
        self.cursor.execute('INSERT INTO groceries (g_name, g_num, g_expdate) VALUES(?,?,?)',
                            (gname.lower(), gnum2, gexpdate2))
        self.conn.commit()


    def showinfo(self,gname):
        self.cursor.execute('SELECT * FROM groceries WHERE g_name=? ORDER BY id DESC LIMIT 1', (gname,))
        info = self.cursor.fetchall()
        self.groceryNameEntryed.setText(gname)
        self.groceryNumEntryed.setText(str(info[0][2]))
        qdate = QDate.fromString(info[0][3], "yyyy-MM-dd")
        self.expiryDateEdited.setDate(qdate)


    def savingEdits(self):
        pass
    def back(self):
        self.close()
        # mainWin = mainBackground.MainFrame(self)
        # mainWin.show()

    def showLeftOvers(self):
        if self.areThereLeftovers.isChecked() == True:
            self.numLeftover.setEnabled(True)
            self.leftoverEntry.setEnabled(True)
            self.expiryDateEditLeftover.setEnabled(True)
            self.expiryDateLeftover.setEnabled(True)
        else:
            self.numLeftover.setEnabled(False)
            self.leftoverEntry.setEnabled(False)
            self.expiryDateEditLeftover.setEnabled(False)
            self.expiryDateLeftover.setEnabled(False)

    def renewInfo(self):
        pass

    def leftOverInfo (self):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editGroceryWin = EditGroceryFrame()
    editGroceryWin.show()

    sys.exit(app.exec_())
