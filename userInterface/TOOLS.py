
from PyQt5.QtWidgets import QMessageBox

def messageBox(self, message):
     self.message= message
     msg_box=QMessageBox()

     msg_box.setWindowTitle('Notice')
     msg_box.setIcon(QMessageBox.Information)
     msg_box.setText(self.message)

     msg_box.addButton(QMessageBox.Ok)

     msg_box.exec_()


