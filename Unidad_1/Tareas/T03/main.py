import sys
from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType("main.ui")

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcularDistancia)

    # Área de los Slots
    def calcularDistancia(self):
        x1 = float(self.txtX1.text())
        x2 = float(self.txtX2.text())
        y1 = float(self.txtY1.text())
        y2 = float(self.txtY2.text())

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("La distancia entre los puntos es: " + str(distancia))
        msg.setWindowTitle("Distancia entre dos puntos")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

