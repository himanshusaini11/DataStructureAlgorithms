from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
import time

def insertionSort(arr, draw_callback, delay, progress_callback, stop_flag):
    for j in range(1, len(arr)):
        i = j
        while i > 0 and arr[i] < arr[i-1]:
            if stop_flag():  # Check if the stop button has been pressed
                return
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
            draw_callback(arr)
            QApplication.processEvents()  # Allow UI to update
            progress_callback(i)
            #QtCore.QThread.msleep(int(delay()))
            time.sleep(int(delay()))
    #return arr

