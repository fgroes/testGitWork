from PySide import QtCore, QtGui
import sys


class TableModel(QtCore.QAbstractTableModel):

	def __init__(self, parent=None, *args):
		super(TableModel, self).__init__(parent, *args)
		
	def setTable(self, table):
		self.table = table

	def rowCount(self, parent):
		return self.table.rowCount

	def columnCount(self, parent):
		return self.table.columnCount

	def data(self, index, role):
		if not index.isValid():
			return None
		elif role != QtCore.Qt.DisplayRole:
			return None
		return self.table.getData(index.row(), index.column())

	def headerData(self, index, orientation, role):
		if role != QtCore.Qt.DisplayRole:
			return None
		result = None
		if (orientation == QtCore.Qt.Horizontal):
			result = self.table.getHeader(index)
		elif (orientation == QtCore.Qt.Vertical):
			result = index + 1
		return result
		

class Table(object):

	def __init__(self, header):
		self.header = header
		self.data = []

	def addRow(self, row):
		if (len(row) == len(self.header)):
			self.data.append(row)

	def getData(self, row, column):
		return self.data[row][column]

	def getHeader(self, column):
		return self.header[column]

	def getColumnCount(self):
		return len(self.header)

	columnCount = property(getColumnCount)

	def getRowCount(self):
		return len(self.data)

	rowCount = property(getRowCount)


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
		centralWidget = QtGui.QWidget()
		self.fileMenu.addAction(exitAction)
		self.centralLayout = QtGui.QVBoxLayout()
		self.centralLayout.addWidget(QtGui.QPushButton('Test'))
		self.tableView = QtGui.QTableView()
		self.setTable()
		self.tableView.setModel(self.tableModel)
		self.centralLayout.addWidget(self.tableView)
		centralWidget.setLayout(self.centralLayout)
		self.setCentralWidget(centralWidget)

	def setTable(self):
		table = Table(['Name', 'Age'])
		table.addRow(['fritz', '31'])
		table.addRow(['dominik', '28'])
		table.addRow(['andi', '26'])
		table.addRow(['franz', '34'])
		self.tableModel = TableModel()
		self.tableModel.setTable(table)


def main():
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
