# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

from datetime import datetime
from database import Database
from PySide6 import QtGui
from functools import partial
from PySide6.QtGui import *
import time

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')

        # pal=self.ui.palette()
        # pal.setColor(str(QPalette.placeholderText), str(QColor("gray")))
        # self.ui.setPalette(pal)

        self.ui.setWindowTitle("Message")
        self.ui.setWindowIcon(QtGui.QIcon('message.png'))
        # scrollArea = QScrollArea()
        # self.ui.gridLayout_message.addWidget(scrollArea)

        self.ui.show()

        self.row = 0
        self.dark=False
        self.ui.btn_dark.setIcon(QtGui.QIcon('sun.png'))
        self.ui.btn_delete.setIcon(QtGui.QIcon('images.jpeg'))
        self.ui.btn_send.clicked.connect(self.addnewmessage)
        self.ui.btn_delete.clicked.connect(self.removeallmessage)
        self.read_message()
        self.ui.btn_dark.clicked.connect(self.my_dark)
        # scrollArea = QScrollArea()
        # self.ui.gridLayout_message.addWidget(scrollArea)
        # self.ui.scroll()
        # if self.ui.btn.clicked.connect(self.removemessage):
        self.start_time = time.time()

    def read_message(self):
        messages = Database.my_select()
        print(messages)
        self.row = len(messages)
        for i,message in enumerate(messages):
            label_1 = QLabel()
            label_1.setText(message[1] + ":" + message[2])
            label_1.setStyleSheet('color:red')
            self.ui.gridLayout_messagee.addWidget(label_1,i,1)


            label = QLabel()
            label.setText(message[3])
            label.setStyleSheet('color:red')
            self.ui.gridLayout_messagee.addWidget(label, i, 2)

            btn=QPushButton()
            btn.setIcon(QtGui.QIcon('images.jpeg'))

            btn.clicked.connect(partial(self.removemessage,btn,message[0],label,label_1))

            self.ui.gridLayout_messagee.addWidget(btn,i,0)

    def addnewmessage(self):
        name = self.ui.lineEdit_name.text()
        text = self.ui.lineEdit_message.text()
        time = '{0:20%y-%m-%d \n %H:%M}'.format(datetime.now())
        messages = Database.my_select()
        print('f', messages[0][3])
        for message in messages:
            id = message[0]
            # if name == message[1] and

        if name !="" and text !="":
            response=Database.my_insert(name,text)
            if response==True:
                label = QLabel()
                label.setText(name + ":" + text)
                label.setStyleSheet('color:red')
                self.ui.gridLayout_messagee.addWidget(label, self.row, 1)

                label_1 = QLabel()
                label_1.setText(time)
                label_1.setStyleSheet('color:red')
                self.ui.gridLayout_messagee.addWidget(label_1, self.row, 2)

                btn = QPushButton()
                btn.setIcon(QtGui.QIcon('images.jpeg'))
                btn.clicked.connect(partial(self.removemessage,btn,id,label,label_1))
                self.ui.gridLayout_messagee.addWidget(btn, self.row, 0)
                self.row += 1

                self.ui.lineEdit_name.setText("")
                self.ui.lineEdit_message.setText("")

                msg_box = QMessageBox()
                msg_box.setText('your message sent successfully!')
                msg_box.exec_()
            else:
                msg_box = QMessageBox()
                msg_box.setText('Database Error.')
                msg_box.exec_()
        else:
            msg_box = QMessageBox()
            msg_box.setText('Error: fields are empty!')
            msg_box.exec_()

    def removeallmessage(self):
        Database.all_delete()
        while self.ui.gridLayout_messagee.count():
            item = self.ui.gridLayout_messagee.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        # if self.ui.gridLayout_message.count() > 2:
        #     while self.ui.gridLayout_m
        print('za')
        # self.ui.gridLayout_message.
        print('z')
        # self.read_message()
        # self.ui.gridLayout_message.item().widget().deleteLater()
        # if response == True:
        #     btn
    def removemessage(self,btn,i,label,label_1):
        x=Database.my_delete(i)
        if x:
            btn.hide()
            label.hide()
            label_1.hide()
            msg_box = QMessageBox()
            msg_box.setText('Deleted.')
            msg_box.exec_()

        # x=Database.my_select()
        # print(x)
        # self.read_message()
        # self.ui.gridLayout_message.item(i).widget().deleteLater()


    def my_dark(self):
        if not self.dark:
            self.ui.setStyleSheet("background-color:black")
            self.dark=not self.dark
            self.ui.btn_dark.setIcon(QtGui.QIcon('month.png'))
        else:
            self.ui.setStyleSheet("background-color:white")
            self.dark = not self.dark
            self.ui.btn_dark.setIcon(QtGui.QIcon('sun.png'))

if __name__ == "__main__":
    app = QApplication([])
    window = Main()

    from PySide6.QtCore import QFile,QTextStream
    # app = QApplication(sys.argv)
    file=QFile(":/dark.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream=QTextStream(file)

    app.setStyleSheet(stream.readAll())
    # window.show()
    sys.exit(app.exec_())
