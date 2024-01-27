import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "main.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnSaludar.clicked.connect(self.saludar)

    # Área de los Slots
    def saludar(self):
        nombre = self.txtNombre.text()
        edad = int(self.txtEdad.text())
        cadena = "Hola " + nombre + " de " + str(edad) + " años :D!"

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
