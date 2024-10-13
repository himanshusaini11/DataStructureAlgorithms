from PyQt6.QtWidgets import QApplication
from ui.SortingVisualizer import SortingVisualizer
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())

