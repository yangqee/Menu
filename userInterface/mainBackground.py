import sqlite3
import string
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.uic.properties import QtCore
from PyQt6.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser, QLabel
from PyQt6 import QtWidgets, QtGui
from PyQt5 import QtWidgets
from mainFrame import Ui_ManagementApp
import TOOLS
import addMenuBackground
import addGroceryBackground
import editGroceryBackground
import random

# Enter for textbox and picture display are not fixed
class MainFrame(QMainWindow, Ui_ManagementApp):
    def __init__(self, parent=None):
        super(MainFrame, self).__init__(parent)
        self.setupUi(self)
        self.showMenu()
        self.showGro()
        self.addMenuBtn.clicked.connect(self.addMenu)
        self.deleteMenuBtn.clicked.connect(self.delMenu)
        self.addGroceryBtn.clicked.connect(self.addGroceries)
        self.editGroceryBtn.clicked.connect(self.editGroceries)
        self.deleteGroceryBtn.clicked.connect(self.deleteGroceries)
        self.refreshRecBtn.clicked.connect(self.refreshRec)
        self.applyRecBtn.clicked.connect(self.applyRec)
    #     self.searchBox_M.installEventFilter(self)
    #
    #
    # def eventFilter(self, obj, event):
        # if obj is self.searchBox_M and event.type() == Qt.Type.KeyPress:
        #     if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
        #         self.onEnterPressed()
        #         return True
    #     if event.type() == QtCore.QEvent.KeyPress and obj is self.searchBox_M:
    #         if event.key() == QtCore.Qt.Key_Return and self.searchBox_M.hasFocus():
    #             self.onEnterPressed()
    #     #         return True
    #     return super().eventFilter(obj, event)
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
    #         self.searchMenu()
    #     else:
    #         super().keyPressEvent(event)


    def onEnterPressed(self):
        self.searchMenu()

    # this is the section for the menue iinterfaces
    def addMenu(self):
        self.closeWin()
        newWinAdd = addMenuBackground.AddMenu(self)
        newWinAdd.show()

    def delMenu(self):
        if self.menuName.text() == 'Menu Name':
            TOOLS.messageBox(self, 'Please select a menu to delete')
            self.closeWin()
            mainWin = MainFrame(self)
            mainWin.show()
        else:
            conn = sqlite3.connect('user_data_ia.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM menues WHERE name=?', (self.menuName.text(),))
            conn.commit()

            self.closeWin()
            mainWin = MainFrame(self)
            mainWin.show()

    def showMenu(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name FROM menues')
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # 为每个g_name创建按钮，并添加到布局中
        for mName in cursor.fetchall():
            btn = QtWidgets.QPushButton(mName[0])
            btn.clicked.connect(self.getSender)
            layout.addWidget(btn)

        # 设置容器widget的布局
        container.setLayout(layout)

        # 将容器widget作为scrollArea的widget
        self.scrollForMenu.setWidget(container)

        conn.close()
    def getSender(self):
        button = self.sender()
        menu_name = str(button.text())
        self.displayMenu(menu_name)
    def displayMenu(self,menu_name):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        self.menuName.setText(menu_name)
        cursor.execute('SELECT method, method_pic, estimate_time FROM menues WHERE name = ?', (menu_name,))
        m_info = ''
        mname = menu_name
        for menu_name in cursor.fetchall():
            m_info += 'Method:\n' + str(menu_name[0]) + '\n' + 'Estimated time used to cook: ' + str(
                menu_name[2]) + 'hours'
            self.showMenuPic(menu_name[1])
        cursor.execute('SELECT ingredient, ingredient_num FROM menu_ingredients WHERE name = ?', (mname,))
        i_info = ''
        for mname in cursor.fetchall():
            i_info += ' ' + str(mname[1]) + ' ' + str(mname[0])
        allinfo = m_info + '\nIngredients:\n' + i_info
        self.menuMethod.setText(allinfo)
    def recdisplayMenu(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        button = self.sender()
        menu_name = str(button.text())
        self.recMenuName.setText(menu_name)
        cursor.execute('SELECT method, method_pic, estimate_time FROM menues WHERE name = ?', (menu_name,))
        m_info = ''
        mname = menu_name
        for menu_name in cursor.fetchall():
            m_info += 'Method:\n' + str(menu_name[0]) + '\n' + 'Estimated time used to cook: ' + str(
                menu_name[2]) + 'hours'
            # self.methodPic.show(menu_name[1])
        cursor.execute('SELECT ingredient, ingredient_num FROM menu_ingredients WHERE name = ?', (mname,))
        i_info = ''
        for mname in cursor.fetchall():
            i_info += ' ' + str(mname[1]) + ' ' + str(mname[0])
        allinfo = m_info + '\nIngredients:\n' + i_info
        self.recMenuMethod.setText(allinfo)

    def showMenuPic(self, path):
        try:
            img = QPixmap(path)
            self.methodPic.setPixmap(img)
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''
    # this is the functions used for groceries

    def searchMenu(self):
        sName = self.searchBox_M.text()
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM menues WHERE name=?',
                       (sName.lower(),))
        if cursor.fetchall.isEmpty()== True:
            TOOLS.messageBox(self,'There is no entry found by this search')
        else:
            self.displayMenu(sName)


    def addGroceries(self):
        # self.closeWin()
        newWinAdd = addGroceryBackground.AddGroceryFrame(self)
        newWinAdd.show()


    def editGroceries(self):
        try:
            if self.getGroName() == 'Grocery Name':
                TOOLS.messageBox(self, 'There are no groceries selected for editing')
                self.closeWin()
                mainWin = MainFrame(self)
                mainWin.show()
            else:
                # self.closeWin()
                selected_gro_name = self.getGroName()  # 获取当前选中的 gro_name
                newWinEdit = editGroceryBackground.EditGroceryFrame(selected_gro_name, self)
                newWinEdit.show()

        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''


    def deleteGroceries(self):
        if self.groceryName.text() == 'Grocery Name':
            TOOLS.messageBox(self, 'Please select a grocery to delete')
            self.closeWin()
            mainWin = MainFrame(self)
            mainWin.show()
        else:
            conn = sqlite3.connect('user_data_ia.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM groceries WHERE g_name=?', (self.groceryName.text(),))
            conn.commit()
            self.closeWin()
            mainWin = MainFrame(self)
            mainWin.show()

    def displayGro(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        button = self.sender()
        gro_name = str(button.text())
        self.groceryName.setText(gro_name)
        cursor.execute('SELECT g_num, g_expdate FROM groceries WHERE g_name = ?', (gro_name,))
        g_info = ''
        for gName in cursor.fetchall():
            g_info += 'Number:' + str(gName[0]) + '\n' + 'Expiry Date:' + str(gName[1]) + '\n'
        self.groceryInfo.setText(g_info)
        return gro_name

    def getGroName(self):
        name = self.groceryName.text()
        return name

    def showGro(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()

        cursor.execute('SELECT g_name FROM groceries GROUP BY g_name')
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        allBtns = self.scrollArea_2.children()
        for child in allBtns:
            if isinstance(child, QtWidgets.QPushButton):
                child.deleteLater()

        for gName in cursor.fetchall():
            btn = QtWidgets.QPushButton(gName[0])
            btn.clicked.connect(self.displayGro)
            layout.addWidget(btn)

        container.setLayout(layout)

        self.scrollArea_2.setWidget(container)

        conn.close()

    def getRec(self):
        try:
            conn = sqlite3.connect('user_data_ia.db')
            cursor = conn.cursor()
            cursor2 = conn.cursor()

            validMenu = []

            #This gets the menu names
            cursor.execute('SELECT name FROM menu_ingredients GROUP BY name')
            if cursor.fetchall():
                #looping all menus for comparing
                for mNames in cursor.fetchall():
                    ing = []
                    ingNum = []
                    haveStore = []
                    # getting the ingredients needed for the menu
                    cursor2.execute('SELECT ingredient, ingredient_num FROM menu_ingredients WHERE name = ?',
                                   (mNames[0],))
                    x=0
                    #sorting into ingredient and ingredient nums
                    for alling in cursor2.fetchall():
                        ing.append(alling[0]) #adding the ingredient names
                        ingNum.append(alling[1]) #adding the ingredient numbers
                    cursor.execute('SELECT g_name FROM groceries GROUP BY g_name')
                    avGro = [g[0] for g in cursor.fetchall()]
                    #loop all needed ingredients
                    i=0
                    for j in ing:
                        #loops all groceries
                        for a in avGro:
                            #if the name is found
                            if j.lower() == a.lower(): #finding if there is matching ingredients
                                cursor.execute('SELECT SUM(g_num) FROM groceries WHERE g_name = ? GROUP BY g_name',
                                               (a,)) #getting the total stock of such ingredients
                                storageNum = int(cursor.fetchone()[0])
                                if storageNum > int(ingNum[i]): #ensuring there is stock
                                    haveStore.append(True)
                            i=i+1
                    if len(haveStore)== len(ing):
                        validMenu.append(mNames)#adding the name into list of usable menues

                conn.commit()
                if len(validMenu)== 0: #no menu is usable
                    noRec = ('There is no recommendations available currently, please purchase more groceries or add menus')
                    TOOLS.messageBox(self, noRec)
                    self.closeWin()
                    mainWin = MainFrame(self)
                    mainWin.show()
                else:
                    return validMenu # return the usable list
            else:
                TOOLS.messageBox(self,'There are no menus, please go add some')
                self.closeWin()
                mainWin = MainFrame(self)
                mainWin.show()

        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''
    def refreshRec(self):
        try:
            names=self.getRec()
            if names:
                container = QtWidgets.QWidget()
                layout = QtWidgets.QVBoxLayout()

                allBtns = self.scrollArea_3.children()
                for child in allBtns:
                    if isinstance(child, QtWidgets.QPushButton):
                        child.deleteLater()
                if len(names)<=3: #creating the buttons if there are less than three menus
                    for a in range(len(names)):
                        btn = QtWidgets.QPushButton(names[a][0])
                        layout.addWidget(btn)
                    container.setLayout(layout)
                    self.scrollArea_3.setWidget(container)
                else: #if there is more than three menus then it would randomly choose three to display
                    rec = random.sample(names, 3)
                    for a in range(len(rec)):
                        btn = QtWidgets.QPushButton(rec[a])
                        layout.addWidget(btn)
                    container.setLayout(layout)
                    self.scrollArea_3.setWidget(container)
                btn.clicked.connect(self.recdisplayMenu)
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''
    def applyRec(self):
        try:
            conn = sqlite3.connect('user_data_ia.db')
            cursor = conn.cursor()
            menuName = str(self.recMenuName.text())
            ing=[]
            ingNum=[]
            count=0
            if menuName == 'Menu Name':
                TOOLS.messageBox(self,'Do not click apply without selecting a menu to apply')
                self.closeWin()
                mainWin = MainFrame(self)
                mainWin.show()
            else:
                cursor.execute('SELECT ingredient, ingredient_num FROM menu_ingredients WHERE name = ?',
                               (menuName,))
                for alling in cursor.fetchall():
                    ing.append(alling[0]) #adding the ingredient names
                    ingNum.append(alling[1]) #adding the ingredient numbers
                for i in range(len(ing)):
                    cursor.execute('SELECT g_num FROM groceries WHERE g_name = ? ORDER BY id ASC LIMIT 1',
                                   (ing[i],))
                    gNum= int(cursor.fetchone()[0])-ingNum[i]
                    cursor.execute('UPDATE groceries SET g_num = ? WHERE id=(SELECT id FROM groceries WHERE g_name = ? ORDER BY id ASC LIMIT 1)',
                                   (gNum,ing[i].lower(),))
                    conn.commit()
                    count = count + cursor.rowcount
                if count == len(ing):
                    TOOLS.messageBox(self, 'Updated '+menuName+' successfully.')
                else:
                    TOOLS.messageBox(self, 'Failed to update ' + menuName)


        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''

    def closeWin(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainFrame()
    mainWin.show()
    sys.exit(app.exec_())
