from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindows import Window

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())