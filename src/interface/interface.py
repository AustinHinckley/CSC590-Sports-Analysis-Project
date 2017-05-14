import Tkinter as Tk
import matplotlib.pyplot as plt
from ipywidgets import widgets
from IPython.display import display

# Putting these here because we might need them
import matplotlib
matplotlib.user('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Interface:
    ''' This class will contain the Tkinter objects and various UI-related methods '''
    WINDOW_TITLE = "Baseball Plotmaster 3000"    # Tentative for sure

    def __init__(self, minWidth, minHeight):
        ''' Initialize window and user widgets '''
        self.window = Tk.Tk()
        window.minsize(width=minWidth, height=minHeight)
        window.wm_title(WINDOW_TITLE)
        self._createWidgets()

    def __init__(self):
        self(600, 400)

    def _createWidgets():
        ''' Loads all of the user-interaction widgets into the window '''
        pass

    # Should somehow include event listeners? Maybe?

    def createPlot(dataX, dataY, markerStyle, markerColor):
        ''' Builds a plot from the given data and adds it to the window '''
        # Can maybe use canvas = FigureCanvasTkAgg(<Figure>, master=window)
        # Then do something like canvas.get_tk_widget().pack(...) or canvas._tkcanvas.pack(...)
        pass

    def display():
        ''' Calls mainloop() to show the window '''
        self.window.mainloop()

    def close():
        ''' Closes the interface window and destroys it '''
        self.window.quit()
        self.window.destroy()
