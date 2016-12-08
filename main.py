import sys, random
from PyQt4.QtGui import QApplication, QMainWindow, QVBoxLayout
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
import numpy as np

from spectrum_sensing import Ui_MainWindow
# generate with 'pyuic4 -x spectrum_sensing.ui -o spectrum_sensing.py'

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
	FigureCanvasQTAgg as FigureCanvas,
	NavigationToolbar2QT as NavigationToolbar)

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class MplCanvas(FigureCanvas):
	"""Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
	def __init__(self, parent=None, width=9, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		# We want the axes cleared every time plot() is called
		self.axes.hold(False)

		self.compute_initial_figure()
		FigureCanvas.__init__(self, fig)

		self.setParent(parent)
		# Create the navigation toolbar, tied to the canvas
		self.mpl_toolbar = NavigationToolbar(self, self)

		expanding = QtGui.QSizePolicy.Expanding
		FigureCanvas.setSizePolicy(self, expanding, expanding)
		FigureCanvas.updateGeometry(self)

	def compute_initial_figure(self):
		self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
		self.axes.set_xlabel('Epochs')
		self.axes.set_ylabel('Loss')

	def update_figure(self):
		# Build a list of 4 random integers between 0 and 10 (both inclusive)
		l = [ random.randint(0, 10) for i in range(4) ]
		self.axes.plot([0, 1, 2, 3], l, 'r')
		self.draw()

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self, ):
		super(Main, self).__init__()
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setWindowTitle("application main window")
		self.setupUi(self)
		self.setupConnections()

	def setupConnections(self):
		self.dc = MplCanvas(self.epoch_loss_plot)
		QtCore.QObject.connect(self.train_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.train)

	def train(self):
		self.dc.update_figure()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())