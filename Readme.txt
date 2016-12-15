README

Files:
ANN.py: was the first neural net we built but we switched to newNet.py to work out bugs in the net.
newNet.py: the current neural net module
window.py: the GUI module, contains the setup of the window elements
main.py: initializes the GUI window and Neural Net and connects their functionality

Install Dependencies:
pip install numpy matplotlib pyqt4

If on Windows and PyQt4 is still not working, you can download WinPython_3.5 which comes with numpy and PyQt4. The entire python environment is contained in one downloadable folder:
https://sourceforge.net/projects/winpython/files/WinPython_3.5/3.5.2.3/WinPython-64bit-3.5.2.3.exe/download
Open 'WinPython Command Prompt.exe', cd into this folder, and then run.

Run:
'python main.py' to start the GUI and load the neural net.
'python newNet.py [#input, #hidden, #output]' if you just want to run the neural net from the command line without the GUI

Train:
Set the parameters and press the train button.