import sys
from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType("main.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcularIMC)

    # Área de los Slots
    def calcularIMC(self):
        peso = float(self.txtPeso.text())
        altura = float(self.txtAltura.text())
        imc = peso / (altura ** 2)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Tu IMC es: " + str(imc))
        msg.setWindowTitle("IMC")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

