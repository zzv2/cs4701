Readme

Files:
ANN.py: was the first neural net we built but we switched to newNet.py to work out bugs in the net.
newNet.py: the current neural net module
window.ui: GUI in xml format, must be built with pyuic4 to create the python file
window.py: the GUI module, contains the setup of the window elements
main.py: initializes the GUI window and Neural Net and connects their functionality

Install Dependencies:
pip install numpy matplotlib pyqt4

Build UI:
pyuic4 window.ui > window.py

Run:
'python main.py' to start the GUI and load the neural net.
'python newNet.py [#input, #hidden, #output]' if you just want to run the NN from the command line without the GUI