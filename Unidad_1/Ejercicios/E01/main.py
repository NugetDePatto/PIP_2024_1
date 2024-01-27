import sys
from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType("main.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnSaludar.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        msj = QtWidgets.QMessageBox()
        msj.setText("Hola a tonotos!")
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

