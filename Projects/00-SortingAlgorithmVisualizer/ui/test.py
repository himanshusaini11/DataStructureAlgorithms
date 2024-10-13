import matplotlib.pyplot as plt
import random

def bubble_sort(arr, bars, fig):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_plot(arr, bars)
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.01)  # Short pause to update

def update_plot(array, bars):
    for bar, height in zip(bars, array):
        bar.set_height(height)

def animate_sorting():
    array = [random.randint(1, 100) for _ in range(50)]

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(array)), array, color='blue')

    ax.set_ylim(0, 110)  # Set the Y-axis limits to accommodate the array values

    # Start Bubble Sort
    bubble_sort(array, bars, fig)

    plt.show()

# Call the animation function
animate_sorting()

