from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    controller = MainController(main_window)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()