from PySide import QtGui
import sys


class MainWindow(QtGui.QMainWindow):
	
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		self.show()

	def initUI(self):
		self.setWindowTitle('basic window')
		self.menu = self.menuBar()
		self.fileMenu = self.menu.addMenu('&File')
		exitAction = QtGui.QAction('&Exit', self)
		exitAction.triggered.connect(QtGui.qApp.quit)
		self.fileMenu.addAction(exitAction)


def main():
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
