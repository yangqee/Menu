# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addMenuFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddMenuFrame(object):
    def setupUi(self, AddMenuFrame):
        AddMenuFrame.setObjectName("AddMenuFrame")
        AddMenuFrame.resize(480, 640)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(163, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(122, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        AddMenuFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        AddMenuFrame.setFont(font)
        self.nameMenu = QtWidgets.QLabel(AddMenuFrame)
        self.nameMenu.setGeometry(QtCore.QRect(30, 30, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameMenu.sizePolicy().hasHeightForWidth())
        self.nameMenu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.nameMenu.setFont(font)
        self.nameMenu.setObjectName("nameMenu")
        self.menuNameEnter = QtWidgets.QTextEdit(AddMenuFrame)
        self.menuNameEnter.setGeometry(QtCore.QRect(30, 50, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuNameEnter.sizePolicy().hasHeightForWidth())
        self.menuNameEnter.setSizePolicy(sizePolicy)
        self.menuNameEnter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menuNameEnter.setObjectName("menuNameEnter")
        self.ingredientsLab = QtWidgets.QLabel(AddMenuFrame)
        self.ingredientsLab.setGeometry(QtCore.QRect(30, 80, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingredientsLab.sizePolicy().hasHeightForWidth())
        self.ingredientsLab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.ingredientsLab.setFont(font)
        self.ingredientsLab.setObjectName("ingredientsLab")
        self.ingredientEnter = QtWidgets.QTextEdit(AddMenuFrame)
        self.ingredientEnter.setGeometry(QtCore.QRect(30, 100, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingredientEnter.sizePolicy().hasHeightForWidth())
        self.ingredientEnter.setSizePolicy(sizePolicy)
        self.ingredientEnter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ingredientEnter.setPlaceholderText("")
        self.ingredientEnter.setObjectName("ingredientEnter")
        self.ingredientFormatLab = QtWidgets.QLabel(AddMenuFrame)
        self.ingredientFormatLab.setGeometry(QtCore.QRect(30, 120, 420, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingredientFormatLab.sizePolicy().hasHeightForWidth())
        self.ingredientFormatLab.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(187, 187, 187))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 219, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.ingredientFormatLab.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.ingredientFormatLab.setFont(font)
        self.ingredientFormatLab.setWordWrap(True)
        self.ingredientFormatLab.setObjectName("ingredientFormatLab")
        self.methodTxtLab = QtWidgets.QLabel(AddMenuFrame)
        self.methodTxtLab.setGeometry(QtCore.QRect(30, 160, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodTxtLab.sizePolicy().hasHeightForWidth())
        self.methodTxtLab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.methodTxtLab.setFont(font)
        self.methodTxtLab.setObjectName("methodTxtLab")
        self.methodEnter = QtWidgets.QTextEdit(AddMenuFrame)
        self.methodEnter.setGeometry(QtCore.QRect(30, 180, 420, 100))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodEnter.sizePolicy().hasHeightForWidth())
        self.methodEnter.setSizePolicy(sizePolicy)
        self.methodEnter.setAutoFillBackground(False)
        self.methodEnter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.methodEnter.setPlaceholderText("")
        self.methodEnter.setObjectName("methodEnter")
        self.methodPicLab = QtWidgets.QLabel(AddMenuFrame)
        self.methodPicLab.setGeometry(QtCore.QRect(30, 350, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.methodPicLab.sizePolicy().hasHeightForWidth())
        self.methodPicLab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.methodPicLab.setFont(font)
        self.methodPicLab.setObjectName("methodPicLab")
        self.finishAddBtn = QtWidgets.QPushButton(AddMenuFrame)
        self.finishAddBtn.setGeometry(QtCore.QRect(70, 550, 120, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 62, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 62, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 219, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.finishAddBtn.setPalette(palette)
        self.finishAddBtn.setObjectName("finishAddBtn")
        self.estiTimeLab = QtWidgets.QLabel(AddMenuFrame)
        self.estiTimeLab.setGeometry(QtCore.QRect(30, 290, 330, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estiTimeLab.sizePolicy().hasHeightForWidth())
        self.estiTimeLab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.estiTimeLab.setFont(font)
        self.estiTimeLab.setObjectName("estiTimeLab")
        self.estiTimeEnter = QtWidgets.QTextEdit(AddMenuFrame)
        self.estiTimeEnter.setGeometry(QtCore.QRect(30, 310, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estiTimeEnter.sizePolicy().hasHeightForWidth())
        self.estiTimeEnter.setSizePolicy(sizePolicy)
        self.estiTimeEnter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.estiTimeEnter.setPlaceholderText("")
        self.estiTimeEnter.setObjectName("estiTimeEnter")
        self.importPicBtn = QtWidgets.QPushButton(AddMenuFrame)
        self.importPicBtn.setGeometry(QtCore.QRect(30, 380, 300, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 219, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.importPicBtn.setPalette(palette)
        self.importPicBtn.setObjectName("importPicBtn")
        self.backBtn = QtWidgets.QPushButton(AddMenuFrame)
        self.backBtn.setGeometry(QtCore.QRect(270, 550, 140, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 62, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 62, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 219, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.backBtn.setPalette(palette)
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi(AddMenuFrame)
        QtCore.QMetaObject.connectSlotsByName(AddMenuFrame)

    def retranslateUi(self, AddMenuFrame):
        _translate = QtCore.QCoreApplication.translate
        AddMenuFrame.setWindowTitle(_translate("AddMenuFrame", "Add Menu Frame"))
        self.nameMenu.setText(_translate("AddMenuFrame", "Name of Menu"))
        self.ingredientsLab.setText(_translate("AddMenuFrame", "Ingredients Used"))
        self.ingredientFormatLab.setText(_translate("AddMenuFrame", "Format must be: (NAME_space_NUMBER_space_NAME_space_NUMBER)"))
        self.methodTxtLab.setText(_translate("AddMenuFrame", "Menu Method (text steps)"))
        self.methodPicLab.setText(_translate("AddMenuFrame", "Menu Picture"))
        self.finishAddBtn.setText(_translate("AddMenuFrame", "Finish Add"))
        self.estiTimeLab.setText(_translate("AddMenuFrame", "Estimated Time to Cook (in hours)"))
        self.importPicBtn.setText(_translate("AddMenuFrame", "Import Picture"))
        self.backBtn.setText(_translate("AddMenuFrame", "Back to Menu"))
