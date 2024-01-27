import sys
from PyQt5 import uic, QtWidgets
from decimal import Decimal

Ui_MainWindow, QtBaseClass = uic.loadUiType("main.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        base = Decimal(self.txtBase.text())
        altura = Decimal(self.txtAltura.text())

        area = (base * altura) / 2

        msj = QtWidgets.QMessageBox()
        msj.setWindowTitle("Resultado")
        msj.setIcon(QtWidgets.QMessageBox.Information)
        msj.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msj.setText("El área es: " + str(area))
        msj.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())