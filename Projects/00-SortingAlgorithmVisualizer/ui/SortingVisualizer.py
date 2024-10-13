# Form implementation generated from reading ui file 'SortingVisualizer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer

import random
from algorithms.BubbleSort import bubbleSort
from algorithms.SelectionSort import selectionSort
from algorithms.InsertionSort import insertionSort
from algorithms.MergeSort import mergeSort
from algorithms.QuickSort import quickSort
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import time

start_time = time.time()

class SortingVisualizer(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SortingVisualizer, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer(self)  # Initialize the timer
        self.elapsed_time = 0
        self.timer.timeout.connect(self.update_lcd)
        self.stop_flag = False  # Flag to stop the sorting process

        
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1057, 501)
        font = QtGui.QFont()
        font.setPointSize(13)
        dialog.setFont(font)
        dialog.setAutoFillBackground(False)
        dialog.setSizeGripEnabled(False)
        
        # LCD Display for time(s).
        self.lcdNumber = QtWidgets.QLCDNumber(parent=dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(780, 70, 241, 71))
        self.lcdNumber.setToolTip("")
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        
        
        self.label = QtWidgets.QLabel(parent=dialog)
        self.label.setGeometry(QtCore.QRect(790, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Apply the same font to all buttons
        #button_font = QtGui.QFont()
        #button_font.setPointSize(13)
        button_style = """
                            QPushButton {
                                font-size: 14pt;
                                color: white;
                                background-color: royalblue;
                                border-radius: 5px;
                                padding: 5px;
                            }
                            QPushButton:hover {
                                background-color: darkblue;
                            }
                            """
        stop_button_style = """
                            QPushButton {
                                font-size: 14pt;
                                color: white;
                                background-color: darkred;
                                border-radius: 5px;
                                padding: 5px;
                            }
                            QPushButton:hover {
                                background-color: red;
                            }
                            """
        # Bubble Sort button.
        self.pushButton_BubbleSort = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_BubbleSort.setGeometry(QtCore.QRect(40, 40, 100, 32))
        self.pushButton_BubbleSort.setFont(font)
        self.pushButton_BubbleSort.setToolTip("Click here to start Bubble Sort algorithm.")
        self.pushButton_BubbleSort.setObjectName("pushButton_BubbleSort")
        self.pushButton_BubbleSort.setStyleSheet(button_style)
        self.pushButton_BubbleSort.clicked.connect(self.start_bubble_sort)
        
        # Selection Sort button.
        self.pushButton_SelectionSort = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_SelectionSort.setGeometry(QtCore.QRect(40, 80, 100, 32))
        self.pushButton_SelectionSort.setToolTip("Click here to start Selection Sort algorithm.")
        self.pushButton_SelectionSort.setObjectName("pushButton_SelectionSort")
        self.pushButton_SelectionSort.setStyleSheet(button_style)
        self.pushButton_SelectionSort.clicked.connect(self.start_selection_sort)
        
        # Insertion Sort.
        self.pushButton_InsertionSort = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_InsertionSort.setGeometry(QtCore.QRect(40, 120, 100, 32))
        self.pushButton_InsertionSort.setToolTip("Click here to start Insertion Sort algorithm.")
        self.pushButton_InsertionSort.setObjectName("pushButton_InsertionSort")
        self.pushButton_InsertionSort.setStyleSheet(button_style)
        self.pushButton_InsertionSort.clicked.connect(self.start_insertion_sort)
        
        # Merge Sort.
        self.pushButton_MergeSort = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_MergeSort.setGeometry(QtCore.QRect(40, 160, 100, 32))
        self.pushButton_MergeSort.setToolTip("Click here to start Merge Sort algorithm.")
        self.pushButton_MergeSort.setObjectName("pushButton_MergeSort")
        self.pushButton_MergeSort.setStyleSheet(button_style)
        self.pushButton_MergeSort.clicked.connect(self.start_merge_sort)
        
        # Quick Sort.
        self.pushButton_QuickSort = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_QuickSort.setGeometry(QtCore.QRect(40, 200, 100, 32))
        self.pushButton_QuickSort.setToolTip("Click here to start Quick Sort algorithm.")
        self.pushButton_QuickSort.setObjectName("pushButton_QuickSort")
        self.pushButton_QuickSort.setStyleSheet(button_style)
        self.pushButton_QuickSort.clicked.connect(self.start_quick_sort)
        
        # Stop button to terminate the algorithm.
        self.pushButton_Stop = QtWidgets.QPushButton(parent=dialog)
        self.pushButton_Stop.setGeometry(QtCore.QRect(330, 460, 301, 32))
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.pushButton_Stop.setStyleSheet(stop_button_style)
        self.pushButton_Stop.clicked.connect(self.stop_sorting)
        
        # Graph visualizer
        self.graphicsView = QtWidgets.QGraphicsView(parent=dialog)
        self.graphicsView.setGeometry(QtCore.QRect(170, 50, 601, 401))
        self.graphicsView.setObjectName("graphicsView")

        # Set up Matplotlib FigureCanvas
        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)
        
        # Create a QGraphicsScene and add the canvas
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.addWidget(self.canvas)
        
        
        # Progress bar.
        self.progressBar = QtWidgets.QProgressBar(parent=dialog)
        self.progressBar.setGeometry(QtCore.QRect(170, 20, 601, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        
        # Slider to control the delay between two steps.
        self.verticalSlider = QtWidgets.QSlider(parent=dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(70, 260, 22, 160))
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setProperty("value", 0)
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBothSides)
        self.verticalSlider.setTickInterval(1000)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_SpeedSlider = QtWidgets.QLabel(parent=dialog)
        self.label_SpeedSlider.setGeometry(QtCore.QRect(60, 430, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_SpeedSlider.setFont(font)
        self.label_SpeedSlider.setToolTip("Slide up to increase the delay between two steps.")
        self.label_SpeedSlider.setObjectName("label_SpeedSlider")
        
        self.verticalSlider.valueChanged.connect(self.update_delay)

        
        # Text box to display any usefull information if required.
        self.textBrowser = QtWidgets.QTextBrowser(parent=dialog)
        self.textBrowser.setGeometry(QtCore.QRect(795, 180, 241, 291))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        
        # Placeholder for array visualization
        self.array = []
        self.array_size = 50
        self.generate_array()

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Sorting Visualizer"))
        self.label.setText(_translate("dialog", "Time in seconds"))
        self.pushButton_BubbleSort.setText(_translate("dialog", "Bubble Sort"))
        self.pushButton_SelectionSort.setText(_translate("dialog", "Selection Sort"))
        self.pushButton_InsertionSort.setText(_translate("dialog", "Insertion Sort"))
        self.pushButton_MergeSort.setText(_translate("dialog", "Merge Sort"))
        self.pushButton_QuickSort.setText(_translate("dialog", "Quick Sort"))
        self.pushButton_Stop.setText(_translate("dialog", "STOP"))
        self.label_SpeedSlider.setText(_translate("dialog", "Slider"))
        
    def generate_array(self):
        self.original_array = [random.randint(1, 100) for _ in range(self.array_size)]
        self.array = self.original_array.copy()
        self.update()
    
    def reset_array(self):
        self.array = self.original_array.copy()
        self.draw_array(self.array)

        
    def draw_array(self, array):
        self.figure.clear()  # Clear the previous plot
        ax = self.figure.add_subplot(111)
        ax.bar(range(len(array)), array, color='blue')
        self.canvas.draw()  # Redraw the canvas to reflect changes
        QtWidgets.QApplication.processEvents()  # Ensure UI stays responsive
        
    def update_delay(self):
        self.delay = self.verticalSlider.value() / 1000

        
    def start_bubble_sort(self):
        self.elapsed_time = 0
        self.timer.start(100)  # Update every 100 ms
        #delay = self.verticalSlider.value() / 1000
        self.update_delay()
        self.progressBar.setMaximum(len(self.array) - 1)  # Set the maximum value to the number of steps
        self.reset_array()
        bubbleSort(self.array, self.draw_array, lambda: self.verticalSlider.value() / 1000, self.update_progress, lambda: self.stop_flag)
        self.timer.stop()  # Stop the timer when sorting is complete
        
    def start_selection_sort(self):
        self.elapsed_time = 0
        self.timer.start(100)  # Update every 100 ms
        delay = self.verticalSlider.value() / 1000
        self.progressBar.setMaximum(len(self.array) - 1)  # Set the maximum value to the number of steps
        self.reset_array()
        selectionSort(self.array, self.draw_array, lambda: self.verticalSlider.value() / 1000, self.update_progress, lambda: self.stop_flag)
        self.timer.stop()  # Stop the timer when sorting is complete
        
    def start_insertion_sort(self):
        self.elapsed_time = 0
        self.timer.start(100)  # Update every 100 ms
        delay = self.verticalSlider.value() / 1000
        self.progressBar.setMaximum(len(self.array) - 1)  # Set the maximum value to the number of steps
        self.reset_array()
        insertionSort(self.array, self.draw_array, lambda: self.verticalSlider.value() / 1000, self.update_progress, lambda: self.stop_flag)
        self.timer.stop()  # Stop the timer when sorting is complete
        
    def start_merge_sort(self):
        self.elapsed_time = 0
        self.timer.start(100)  # Update every 100 ms
        delay = self.verticalSlider.value() / 1000
        self.progressBar.setMaximum(len(self.array) - 1)  # Set the maximum value to the number of steps
        self.reset_array()
        mergeSort(self.array, self.draw_array, lambda: self.verticalSlider.value() / 1000, self.update_progress, lambda: self.stop_flag)
        self.timer.stop()  # Stop the timer when sorting is complete
        
    def start_quick_sort(self):
        self.elapsed_time = 0
        self.timer.start(100)  # Update every 100 ms
        delay = self.verticalSlider.value() / 1000
        self.progressBar.setMaximum(len(self.array) - 1)  # Set the maximum value to the number of steps
        self.reset_array()
        quickSort(self.array, self.draw_array, lambda: self.verticalSlider.value() / 1000, self.update_progress, lambda: self.stop_flag)
        self.timer.stop()  # Stop the timer when sorting is complete

        
    def update_lcd(self):
        self.elapsed_time += 0.1  # Increment time by 0.1 seconds
        self.lcdNumber.display(f"{self.elapsed_time:.1f}")
        
    def update_progress(self, value):
        self.progressBar.setValue(value)
        
    def stop_sorting(self):
        self.stop_flag = True
        time.sleep(0.1)  # Small delay to ensure the current sorting process stops
        

