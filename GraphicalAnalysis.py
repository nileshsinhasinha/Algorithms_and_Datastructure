"To graphically analyze any algorithms on input"
def singlegraph(x_axis, y_axis):
    "To graphically analyze any algorithms on input for single Graph"
    import matplotlib.pyplot as plt
    plt.plot(x_axis, y_axis)
    plt.xlabel("Inputs-->N")
    plt.ylabel("Time-->ms")
    plt.title("Time Complexity")
    plt.show()
