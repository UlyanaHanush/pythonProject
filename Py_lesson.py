# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
## if __name__ == "__main__":
#
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('tre Brige')
#     w.show()
#
#     sys.exit(app.exec_())
## from PyQt5.QtGui import QIcon
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('The Br')
#         self.setWindowIcon(QIcon('web.png'))
#
#         self.show()
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
# from PyQt5.QtGui import QFont
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont('SansSerif', 10))
#         btn = QPushButton('Button', self)
#         btn.setToolTip('Tis is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('The Br')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
#
#
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
# from PyQt5.QtCore import QCoreApplication
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         btn = QPushButton('Quit', self)
#         btn.clicked.connect(QCoreApplication.instance().quit)
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('The Br')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('The Br')
#         self.show()
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, 'message', "are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QRadioButton, QLabel)


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(600,600)
        self.ll = QLineEdit(self)
        self.ll.move(10,10)
        self.sth = QPushButton('Button', self)
        self.sth.setGeometry(100,100,75,75)
        self.rb = QRadioButton('Button R', self)
        self.rb.move(50,50)
        self.ql = QLabel('Label', self)
        self.style = 'border:3px solid black'
        self.ql.setStyleSheet(self.style)
        self.ql.setGeometry(200, 200, 80, 80)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())