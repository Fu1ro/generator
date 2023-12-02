from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self, examle)
    def generate(self):
        self.lable.setText('da')
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()