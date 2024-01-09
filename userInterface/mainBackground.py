import sqlite3
import string
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import QtWidgets, QtGui
from PyQt5 import QtWidgets
from mainFrame import Ui_ManagementApp
import TOOLS
import addMenuBackground
import addGroceryBackground
import editGroceryBackground
import random

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
        # self.showMenuPic()

    # this is the section for the menue iinterfaces
    def addMenu(self):
        self.closeWin()
        newWinAdd = addMenuBackground.AddMenu(self)
        newWinAdd.show()

    def delMenu(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM menues WHERE name=?', (self.menuName.text(),))
        conn.commit()
        self.showMenu()

    def showMenu(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name FROM menues')
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # 为每个g_name创建按钮，并添加到布局中
        for mName in cursor.fetchall():
            btn = QtWidgets.QPushButton(mName[0])
            btn.clicked.connect(self.displayMenu)
            layout.addWidget(btn)

        # 设置容器widget的布局
        container.setLayout(layout)

        # 将容器widget作为scrollArea的widget
        self.scrollForMenu.setWidget(container)

        conn.close()

    def displayMenu(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        button = self.sender()
        menu_name = str(button.text())
        self.menuName.setText(menu_name)
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
        self.menuMethod.setText(allinfo)

    def showMenuPic(self):
        scene = QtWidgets.QGraphicsScene()  # 加入 QGraphicsScene
        img = QtGui.QPixmap('hello.jpg')  # 加入图片
        scene.addPixmap(img)  # 將图片加入 scene
        self.methodPic.setScene(scene)


    # this is the functions used for groceries
    def addGroceries(self):
        self.closeWin()
        newWinAdd = addGroceryBackground.AddGroceryFrame(self)
        newWinAdd.show()

    def editGroceries(self):
        self.closeWin()
        selected_gro_name = self.getGroName()  # 获取当前选中的 gro_name
        newWinEdit = editGroceryBackground.EditGroceryFrame(selected_gro_name, self)
        newWinEdit.show()

    def deleteGroceries(self):
        conn = sqlite3.connect('user_data_ia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM groceries WHERE g_name=?', (self.groceryName.text(),))
        conn.commit()
        self.showGro()

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
            ing=[]
            ingNum=[]
            validMenu = []
            #This gets the menu names
            cursor.execute('SELECT name FROM menu_ingredients GROUP BY name')
            #looping all menus for comparing
            for mNames in cursor.fetchall():
                # getting the ingredients needed for the menu
                cursor2.execute('SELECT ingredient, ingredient_num FROM menu_ingredients WHERE name = ?',
                               (str(mNames),))
                x=0
                #sorting into ingredient and ingredient nums
                for alling in cursor2.fetchall():
                    if x%2==0:
                        ing.append(alling)
                    else:
                        ingNum.append(alling)
                    x=x+1
                cursor.execute('SELECT g_name FROM groceries GROUP BY g_name')
                avGro = cursor.fetchall()
                #loop all available grocery names
                for j in range(len(avGro)):
                    #loops all ingredients needed
                    for a in range(len(ing)):
                        #if the name is found
                        if avGro[j] == ing[a]:
                            cursor.execute('SELECT SUM(g_num) FROM groceries GROUP BY g_name WHERE g_name = ?',
                                           (ing[a]))
                            storageNum = int(cursor.fetchone())
                            if storageNum == int(ingNum[a]):
                                validMenu.append(mNames[i])
            if len(mNames)<3:
                error=False
                return error
            else:
                return mNames
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''
    def refreshRec(self):
        try:
            names=self.getRec()
            if names == False:
                noRec = (
                    'There is no recommendations available currently, please purchase more groceries or add menus')
                TOOLS.messageBox(self, noRec)
            else:
                container = QtWidgets.QWidget()
                layout = QtWidgets.QVBoxLayout()

                allBtns = self.scrollArea_3.children()
                for child in allBtns:
                    if isinstance(child, QtWidgets.QPushButton):
                        child.deleteLater()
                rec = random.sample(names, 3)
                for a in range(len(rec)):
                    btn = QtWidgets.QPushButton(rec[a])
                    btn.clicked.connect(self.displayMenu)
                    layout.addWidget(btn)
                container.setLayout(layout)
                self.scrollArea_3.setWidget(container)
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''
    def applyRec(self):
        pass

    def closeWin(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainFrame()
    mainWin.show()
    sys.exit(app.exec_())
