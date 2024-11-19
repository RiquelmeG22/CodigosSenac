import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

ui_file = 'C:/Users/suporte/Documents/GitHub/CodigosSenac/python/Desktop/pyqt/layout.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

        self.butao_label.setText('Muda o label')
        self.butao_label.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText(self.input.text())
        print("Riquekme")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



