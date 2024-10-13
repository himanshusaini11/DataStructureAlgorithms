from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
import time

def selectionSort(arr, draw_callback, delay, progress_callback, stop_flag):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if stop_flag():  # Check if the stop button has been pressed
                return
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                draw_callback(arr)
                QApplication.processEvents()  # Allow UI to update
                progress_callback(j)
                time.sleep(int(delay()))
                
    #return arr
