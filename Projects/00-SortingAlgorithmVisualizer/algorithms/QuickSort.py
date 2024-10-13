from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
import time

def quickSort(arr, draw_callback, delay, progress_callback, stop_flag):
    quickSortAlgorithm(arr, 0, len(arr) - 1, draw_callback, delay, progress_callback, stop_flag)

def quickSortAlgorithm(arr, s, e, draw_callback, delay, progress_callback, stop_flag):
    if s < e:
        mid = (s + e) // 2
        pivot = arr[mid]
        index = partition(arr, s, e, pivot, draw_callback, delay, progress_callback, stop_flag)
        quickSortAlgorithm(arr, s, index - 1, draw_callback, delay, progress_callback, stop_flag)
        quickSortAlgorithm(arr, index, e, draw_callback, delay, progress_callback, stop_flag)

def partition(arr, left, right, pivot, draw_callback, delay, progress_callback, stop_flag):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            draw_callback(arr)
            progress_callback(left)
            time.sleep(int(delay()))
            left += 1
            right -= 1
    return left