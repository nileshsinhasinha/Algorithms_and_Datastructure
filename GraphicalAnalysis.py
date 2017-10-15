"To graphically analyze any algorithms on input"
def singlegraph(x_axis, y_axis, y_label,title):
    "To graphically analyze any algorithms on input for single Graph"
    import matplotlib.pyplot as plt
    plt.plot(x_axis, y_axis)
    plt.xlabel("Inputs-->N")
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
