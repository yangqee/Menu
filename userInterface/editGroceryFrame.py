# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editGroceryFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editGroceryFrame(object):
    def setupUi(self, editGroceryFrame):
        editGroceryFrame.setObjectName("editGroceryFrame")
        editGroceryFrame.resize(480, 498)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(editGroceryFrame.sizePolicy().hasHeightForWidth())
        editGroceryFrame.setSizePolicy(sizePolicy)
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
        editGroceryFrame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        editGroceryFrame.setFont(font)
        self.areThereLeftovers = QtWidgets.QRadioButton(editGroceryFrame)
        self.areThereLeftovers.setEnabled(True)
        self.areThereLeftovers.setGeometry(QtCore.QRect(30, 120, 300, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.areThereLeftovers.sizePolicy().hasHeightForWidth())
        self.areThereLeftovers.setSizePolicy(sizePolicy)
        self.areThereLeftovers.setChecked(False)
        self.areThereLeftovers.setAutoRepeat(False)
        self.areThereLeftovers.setObjectName("areThereLeftovers")
        self.nameGroceryed = QtWidgets.QLabel(editGroceryFrame)
        self.nameGroceryed.setGeometry(QtCore.QRect(30, 20, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameGroceryed.sizePolicy().hasHeightForWidth())
        self.nameGroceryed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.nameGroceryed.setFont(font)
        self.nameGroceryed.setObjectName("nameGroceryed")
        self.expiryDateLeftover = QtWidgets.QLabel(editGroceryFrame)
        self.expiryDateLeftover.setEnabled(False)
        self.expiryDateLeftover.setGeometry(QtCore.QRect(30, 200, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiryDateLeftover.sizePolicy().hasHeightForWidth())
        self.expiryDateLeftover.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.expiryDateLeftover.setFont(font)
        self.expiryDateLeftover.setObjectName("expiryDateLeftover")
        self.groceryNumEntryed = QtWidgets.QTextEdit(editGroceryFrame)
        self.groceryNumEntryed.setGeometry(QtCore.QRect(30, 90, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groceryNumEntryed.sizePolicy().hasHeightForWidth())
        self.groceryNumEntryed.setSizePolicy(sizePolicy)
        self.groceryNumEntryed.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.groceryNumEntryed.setObjectName("groceryNumEntryed")
        self.groceryNameEntryed = QtWidgets.QTextEdit(editGroceryFrame)
        self.groceryNameEntryed.setGeometry(QtCore.QRect(30, 40, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groceryNameEntryed.sizePolicy().hasHeightForWidth())
        self.groceryNameEntryed.setSizePolicy(sizePolicy)
        self.groceryNameEntryed.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.groceryNameEntryed.setObjectName("groceryNameEntryed")
        self.expiryDateEditLeftover = QtWidgets.QDateEdit(editGroceryFrame)
        self.expiryDateEditLeftover.setEnabled(False)
        self.expiryDateEditLeftover.setGeometry(QtCore.QRect(30, 220, 110, 22))
        self.expiryDateEditLeftover.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.expiryDateEditLeftover.setObjectName("expiryDateEditLeftover")
        self.numGroceryed = QtWidgets.QLabel(editGroceryFrame)
        self.numGroceryed.setGeometry(QtCore.QRect(30, 70, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numGroceryed.sizePolicy().hasHeightForWidth())
        self.numGroceryed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.numGroceryed.setFont(font)
        self.numGroceryed.setObjectName("numGroceryed")
        self.leftoverEntry = QtWidgets.QTextEdit(editGroceryFrame)
        self.leftoverEntry.setEnabled(False)
        self.leftoverEntry.setGeometry(QtCore.QRect(30, 170, 420, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftoverEntry.sizePolicy().hasHeightForWidth())
        self.leftoverEntry.setSizePolicy(sizePolicy)
        self.leftoverEntry.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftoverEntry.setObjectName("leftoverEntry")
        self.numLeftover = QtWidgets.QLabel(editGroceryFrame)
        self.numLeftover.setEnabled(False)
        self.numLeftover.setGeometry(QtCore.QRect(30, 150, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numLeftover.sizePolicy().hasHeightForWidth())
        self.numLeftover.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.numLeftover.setFont(font)
        self.numLeftover.setObjectName("numLeftover")
        self.expiryDateEd = QtWidgets.QLabel(editGroceryFrame)
        self.expiryDateEd.setGeometry(QtCore.QRect(30, 250, 300, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expiryDateEd.sizePolicy().hasHeightForWidth())
        self.expiryDateEd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.expiryDateEd.setFont(font)
        self.expiryDateEd.setObjectName("expiryDateEd")
        self.expiryDateEdited = QtWidgets.QDateEdit(editGroceryFrame)
        self.expiryDateEdited.setGeometry(QtCore.QRect(30, 270, 110, 22))
        self.expiryDateEdited.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.expiryDateEdited.setObjectName("expiryDateEdited")
        self.editGroceryBtn = QtWidgets.QPushButton(editGroceryFrame)
        self.editGroceryBtn.setGeometry(QtCore.QRect(180, 390, 120, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editGroceryBtn.sizePolicy().hasHeightForWidth())
        self.editGroceryBtn.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(180, 187, 114))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 187, 114))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 187, 114))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.editGroceryBtn.setPalette(palette)
        self.editGroceryBtn.setObjectName("editGroceryBtn")
        self.backBtn = QtWidgets.QPushButton(editGroceryFrame)
        self.backBtn.setGeometry(QtCore.QRect(30, 300, 61, 31))
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

        self.retranslateUi(editGroceryFrame)
        QtCore.QMetaObject.connectSlotsByName(editGroceryFrame)

    def retranslateUi(self, editGroceryFrame):
        _translate = QtCore.QCoreApplication.translate
        editGroceryFrame.setWindowTitle(_translate("editGroceryFrame", "Edit Grocery Frame"))
        self.areThereLeftovers.setText(_translate("editGroceryFrame", "Are there any left overs"))
        self.nameGroceryed.setText(_translate("editGroceryFrame", "Name of Grocery"))
        self.expiryDateLeftover.setText(_translate("editGroceryFrame", "Expiry Date of left overs"))
        self.numGroceryed.setText(_translate("editGroceryFrame", "Number of Grocery"))
        self.numLeftover.setText(_translate("editGroceryFrame", "Number of left overs"))
        self.expiryDateEd.setText(_translate("editGroceryFrame", "Expiry Date"))
        self.editGroceryBtn.setText(_translate("editGroceryFrame", "Finish Edit"))
        self.backBtn.setText(_translate("editGroceryFrame", "Back"))
