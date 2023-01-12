import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def getZ(x, y, d):
    r = numpy.sqrt(x ** 2 + y ** 2)
    return numpy.cos(r) * (d - r)


def main():
    # Define the range of values for x and y
    x = numpy.linspace(-7, 7)
    y = numpy.linspace(-7, 7)

    # Create a 2D grid of x and y values
    X, Y = numpy.meshgrid(x, y)

    # Define the value of d
    d = 20

    # Calculate the function values for each point in the grid
    Z = getZ(X, Y, d)

    # Create a 3D plot
    fig = plt.figure()
    graph = fig.add_subplot(111, projection='3d')
    graph.plot_surface(X, Y, Z)

    # Set axis labels and plot title
    graph.set_xlabel("X")
    graph.set_ylabel("Y")
    graph.set_zlabel("Z")
    graph.set_title("Visualization of Z = cos(r) * (d - r)")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
