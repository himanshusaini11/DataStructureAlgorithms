from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
import time

def mergeSort(arr, draw_callback, delay, progress_callback, stop_flag):
    # Define the base case
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr) // 2
        left = mergeSort(arr[ : middle], draw_callback, delay, progress_callback, stop_flag)
        right = mergeSort(arr[middle : ], draw_callback, delay, progress_callback, stop_flag)
        sorted_array = merge(left, right, draw_callback, delay, progress_callback, stop_flag)
        draw_callback(sorted_array)
        time.sleep(int(delay()))
        return sorted_array

def merge(left, right, draw_callback, delay, progress_callback, stop_flag):
    result = []
    i, j = 0, 0
    while (i < len(left) and j < len(right)):
        if stop_flag():
            return
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        draw_callback(result + left[i:] + right[j:])
        progress_callback(len(result))
        time.sleep(int(delay()))
    
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    draw_callback(result)
    return result
