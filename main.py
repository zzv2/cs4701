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

class MplCanvas(FigureCanvas):
	"""Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)

		# We want the axes cleared every time plot() is called
		self.axes.hold(False)

		self.compute_initial_figure()
		FigureCanvas.__init__(self, fig)
		self.setParent(parent)

		FigureCanvas.setSizePolicy(self,
									QtGui.QSizePolicy.Expanding,
									QtGui.QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)


class DynamicMplCanvas(MplCanvas):
	"""A canvas that updates itself every second with a new plot."""
	def __init__(self, *args, **kwargs):
		MplCanvas.__init__(self, *args, **kwargs)
		timer = QtCore.QTimer(self)
		QtCore.QObject.connect(timer,
								QtCore.SIGNAL("timeout()"),
								self.update_figure)
		timer.start(1000)

	def compute_initial_figure(self):
		self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

	def update_figure(self):
		# Build a list of 4 random integers between 0 and 10 (both inclusive)
		l = [ random.randint(0, 10) for i in range(4) ]
		self.axes.plot([0, 1, 2, 3], l, 'r')
		self.draw()

class Main(QMainWindow, Ui_MainWindow):
	def __init__(self, ):
		# QMainWindow.__init__(self)
		# self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		# self.setWindowTitle("application main window")
		super(Main, self).__init__()
		self.setupUi(self)

	def addDmpl(self):
		self.dc = DynamicMplCanvas(self.epoch_loss_plot)

	# def addmpl(self, fig):
		# self.canvas = FigureCanvas(fig)
		# self.setCentralWidget(self.canvas)

		# self.epoch_loss_plot = QtGui.QWidget(self.centralwidget)
		# self.epoch_loss_plot.setMinimumSize(QtCore.QSize(0, 300))
		# self.epoch_loss_plot.setObjectName(_fromUtf8("epoch_loss_plot"))


		# l = QVBoxLayout(self.epoch_loss_plot)
		# sc = MyStaticMplCanvas(self.epoch_loss_plot, width=5, height=4, dpi=100)
		# l.addWidget(sc)
		# dc = MyDynamicMplCanvas(self.epoch_loss_plot, width=5, height=4, dpi=100)
		# l.addWidget(dc)

		# self.epoch_loss_plot.setFocus()
		# self.epoch_loss_plot.addWidget(self.canvas)
		# self.canvas.draw()



if __name__ == "__main__":

	# app = QtGui.QApplication(sys.argv)
	# MainWindow = QtGui.QMainWindow()
	# ui = Ui_MainWindow()
	# ui.setupUi(MainWindow)
	# MainWindow.show()
	# sys.exit(app.exec_())

	# fig1 = Figure()
	# ax1f1 = fig1.add_subplot(111)
	# ax1f1.plot(np.random.rand(5))

	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.addDmpl()
	main.show()
	sys.exit(app.exec_())