from mainWindowUI import MainWindowUI
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
