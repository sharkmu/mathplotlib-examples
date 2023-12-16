import matplotlib.pyplot as plt
import numpy as np

# example datas
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# fonts
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

def line_diagram():
    plt.plot(xpoints, ypoints)
    plt.show()

line_diagram()

def line_diagram_o():
    plt.plot(xpoints, ypoints, 'o')
    plt.show()

line_diagram_o()

def line_diagram_marker():
    plt.plot(xpoints, ypoints, marker='x') # You can also use these: o * . , x X + P s D d p H h v ^ < > 1 2 3 4 | _
    plt.show()

line_diagram_marker()

def title_diagram():
    
    plt.title("This is a funny diagram")
    plt.xlabel("This is a wonderful X axis", fontdict = font2)
    plt.ylabel("This is a happy Y axis")

    plt.plot(xpoints, ypoints, ls = ":") # <-- linestyle
    plt.show()

title_diagram()

def save_figure_diagram():
    plt.title("This is a funny diagram")
    plt.xlabel("This is a wonderful X axis", fontdict = font2)
    plt.ylabel("This is a happy Y axis")
    plt.plot(xpoints, ypoints, ls = ":") # <-- linestyle
    plt.savefig('my_figure.png')
    plt.show()

save_figure_diagram()