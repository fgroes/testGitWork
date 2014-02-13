from PySide import QtGui
import sys


class MainWindow(QtGui.QMainWindow):
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		self.show()

	def initUI(self):
		self.setWindowTitle('basic window')



def main():
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
