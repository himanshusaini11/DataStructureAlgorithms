from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
import time

def bubbleSort(arr, draw_callback, delay, progress_callback, stop_flag):
    #n = len(arr)
    #total_steps = n * (n - 1) / 2  # Total possible comparisons
    #current_step = 0
    did_swap = True
    
    while did_swap:
        did_swap = False
        for i in range(1, len(arr)):
            if stop_flag():  # Check if the stop button has been pressed
                return
            #current_step += 1
            if arr[i] < arr[i-1]:
                did_swap = True
                arr[i], arr[i-1] = arr[i-1], arr[i]
                draw_callback(arr)
                QApplication.processEvents()  # Allow UI to update
                progress_callback(i)
                #QtCore.QThread.msleep(int(delay()))
                time.sleep(int(delay()))
    #return arr
