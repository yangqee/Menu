import os.path
import shutil
import sqlite3

from addMenuFrame import Ui_AddMenuFrame
import sys
import TOOLS
import mainBackground
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class AddMenu(QMainWindow, Ui_AddMenuFrame):
    destination_path = ''

    def __init__(self, parent=None):
        super(AddMenu, self).__init__(parent)
        self.setupUi(self)
        # creating the database connection
        self.conn = sqlite3.connect('user_data_ia.db')
        self.cursor = self.conn.cursor()
        self.finishAddBtn.clicked.connect(self.finishAdd)
        self.importPicBtn.clicked.connect(self.uploadFile)

        self.backBtn.clicked.connect(self.back)


    def finishAdd(self):

        ingredientName = []
        ingredient_num = []

        # saving the different information into varibles
        menuName = self.menuNameEnter.toPlainText()
        methodTxt = self.methodEnter.toPlainText()
        estiTime = self.estiTimeEnter.toPlainText()
        ingredients = self.ingredientEnter.toPlainText()


        # saving ingredient name and numbers separatly
        splitIng = ingredients.split()
        for i in range(len(splitIng)):
            if i % 2 == 0:
                ingredientName.append(splitIng[i])
            elif splitIng[i].isdigit():
                ingredient_num.append(splitIng[i])
            else:
                notaNUM = (
                    'Error in ingredients entry!\nIt seems like you did not the number of ingredients, please follow the format!')
                TOOLS.messageBox(self, notaNUM)
        a = self.saveMenu(menuName, methodTxt, estiTime)
        if a > 0:
            self.saveMenuIng(menuName, ingredientName, ingredient_num)
            successfulSave = 'Save Successful! \nthis menu is now saved please enjoy!'
            TOOLS.messageBox(self, successfulSave)
            self.back()
        else:
            wentWrong='Something went wrong'
            TOOLS.messageBox(self,wentWrong)

    def saveMenu(self, menuName, methodTxt, estiTime):

        # check if there is an entry
        self.cursor.execute('SELECT * FROM menues WHERE name=?', (menuName,))
        existing_name = self.cursor.fetchone()
        if existing_name:
            existName = 'Saving failed\nSorry, it seems like this name is already used by another menu'
            TOOLS.messageBox(self, existName)
            return 0
        elif self.destination_path == '':
            self.cursor.execute('INSERT INTO menues (name, method, estimate_time) VALUES(?,?,?)',
                                (menuName.lower(), methodTxt, estiTime))
            self.conn.commit()
            return 1

        else:
            self.cursor.execute('INSERT INTO menues (name, method, method_pic, estimate_time) VALUES(?,?,?,?)',
                                (menuName.lower(), methodTxt, self.destination_path, estiTime))
            self.conn.commit()
            return 1


    def saveMenuIng(self, menuName, ingredientName, ingredient_num):
        for i in range(len(ingredientName)):
            self.cursor.execute('INSERT INTO menu_ingredients (name, ingredient, ingredient_num) VALUES(?,?,?)',
                                (menuName.lower(), ingredientName[i].lower(), ingredient_num[i]))
            self.conn.commit()

    # def uploadFile(self):
    #     try:
    #         file_path, _ = QFileDialog.getOpenFileName(self, 'Choose your desired file')
    #         if file_path:
    #             fileName, file_extension = os.path.splitext(os.path.basename(file_path))
    #             if file_extension.lower() in ('.jpg', '.png'):
    #                 self.destination_path = os.path.join('.\\methodpics\\', fileName + file_extension)
    #                 shutil.copy(file_path, self.destination_path)
    #                 if os.path.exists(self.destination_path):
    #                     pass
    #                     #THIS IS A BUGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
    #                     # uploadSuc = 'Upload Success!'
    #                     # TOOLS.messageBox(self, uploadSuc)
    #                     # return self.destination_path
    #                 else:
    #                     uploadFail = 'Upload Failed'
    #                     TOOLS.messageBox(self, uploadFail)
    #                     return ''
    #             else:
    #                 wrongFile = 'Wrong file type!\nPlease upload a .jpg or a .png file'
    #                 TOOLS.messageBox(self, wrongFile)
    #     except Exception as e:
    #         errorMsg = f"An error occurred: {str(e)}"
    #         TOOLS.messageBox(self, errorMsg)
    #         return ''
    def uploadFile(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Choose your desired file')
            if file_path:
                fileName, file_extension = os.path.splitext(os.path.basename(file_path))
                if file_extension.lower() in ('.jpg', '.png'):
                    destination_dir = os.path.join('.', 'methodpics')  # 跨平台路径
                    # 确保目标目录存在
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)

                    self.destination_path = os.path.join(destination_dir, fileName + file_extension)
                    shutil.copy(file_path, self.destination_path)
                    if os.path.exists(self.destination_path):
                        uploadSuc = 'Upload Success!'
                        TOOLS.messageBox(self, uploadSuc)
                        return self.destination_path
                    else:
                        uploadFail = 'Upload Failed'
                        TOOLS.messageBox(self, uploadFail)
                        return ''
                else:
                    wrongFile = 'Wrong file type!\nPlease upload a .jpg or a .png file'
                    TOOLS.messageBox(self, wrongFile)
        except Exception as e:
            errorMsg = f"An error occurred: {str(e)}"
            TOOLS.messageBox(self, errorMsg)
            return ''

    def back(self):
        self.close()
        mainWin=mainBackground.MainFrame(self)
        mainWin.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = AddMenu()
    mainWin.show()
    sys.exit(app.exec_())
