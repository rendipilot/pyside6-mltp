import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.load_main_ui()
        
    def load_main_ui(self):
        ui_file = QFile("ui/main.ui")
        ui_file.open(QFile.ReadOnly)
        widget = self.loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(widget)
    
    def load_second_ui(self):
        ui_file = QFile("ui/second.ui")
        ui_file.open(QFile.ReadOnly)
        widget = self.loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())