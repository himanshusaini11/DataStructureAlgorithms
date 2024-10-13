from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QApplication
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor
import sys
import random
from algorithms.BubbleSort import bubbleSort

class SortingVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sorting Visualizer')
        self.setGeometry(100, 100, 800, 600)
        
        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        # Start Button
        self.start_button = QPushButton('Start Bubble Sort')
        self.start_button.clicked.connect(self.start_sorting)
        self.layout.addWidget(self.start_button)
        
        # Speed Slider
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(100)
        self.speed_slider.setValue(50)
        self.layout.addWidget(self.speed_slider)
        
        # Placeholder for array visualization
        self.array = []
        self.array_size = 50
        self.generate_array()

    def generate_array(self):
        self.array = [random.randint(1, 100) for _ in range(self.array_size)]
        self.update()

    def draw_array(self, array):
        self.array = array
        self.update()  # Trigger a repaint of the window

    def start_sorting(self):
        delay = self.speed_slider.value() / 1000.0
        bubbleSort(self.array, self.draw_array, delay)

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width() / len(self.array)
        for i, value in enumerate(self.array):
            x = int(i * width)
            y = int(self.height() - (value / max(self.array) * self.height()))
            painter.setBrush(QColor(0, 0, 255))
            painter.drawRect(x, y, int(width) - 2, self.height())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SortingVisualizer()
    window.show()
    sys.exit(app.exec())

