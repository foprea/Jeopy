from PyQt4.QtCore import *
from PyQt4.QtGui import *
from QuestionEditorWidget import QuestionEditor

class questionGrid(QWidget):
	def __init__(self, rows, cols):
		QWidget.__init__(self)
		
		self.buttons = []
		self.layout = QGridLayout()	
		self.setLayout(self.layout)

		self.setupGui(rows, cols)
	def setupGui(self, rows, cols):	
		#layout.setHorizontalSpacing(5)
		self.layout.setSpacing(10)
		for i in range(rows): #linie i=n
			for j in range(cols): #coloana j=m
				widget = QPushButton()
				self.buttons.append(widget)
			#	widget.setText(str(i * cols + j))
	                        widget.setText(str(self.buttons.index(widget)))

				self.layout.addWidget(widget, i, j)
				widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
	                        self.connect(widget, SIGNAL("clicked()"), lambda clickedWidget = self.buttons.index(widget): self.showQEditor(clickedWidget))

	def addRow(self, rows, cols):
		for j in range(cols):
			widget = QPushButton()
			self.buttons.append(widget)
			#widget.setText(str((rows * cols) - (cols - j))
			widget.setText(str(self.buttons.index(widget)))
			self.layout.addWidget(widget, rows - 1, j)
			widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			widget.show()
		self.updateWidgetIndex(rows, cols) 

	def remRow(self, rows, cols):
		for j in range(cols):
			self.buttons[-1].hide()
			self.layout.removeWidget(self.buttons[-1])
			self.buttons.remove(self.buttons[-1])
                self.updateWidgetIndex(rows, cols)
	
	def addColumn(self, rows, cols):
		for i in range(rows):
			widget = QPushButton()
			self.layout.addWidget(widget, i, cols - 1)
			self.buttons.insert(cols - 1 + i * (cols - 1) + i, widget)
			#widget.setText(str(cols - 1 + i * (cols - 1) + i))
                        widget.setText(str(self.buttons.index(widget)))
			widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			widget.show()
		self.updateWidgetIndex(rows, cols)
			
	def remColumn(self, rows, cols):
		for i in reversed(range(rows)):
			self.buttons[cols + (i * (cols + 1))].hide()
			self.layout.removeWidget(self.buttons[cols + (i * (cols + 1))])
			self.buttons.remove(self.buttons[cols+(i * (cols + 1))])
		self.updateWidgetIndex(rows, cols)

	def showQEditor(self, widget):
		QEditor = QuestionEditor()
		QEditor.show()
		print widget

	def updateWidgetIndex(self, rows, cols):
		for i in range(rows * cols):
			widget = self.buttons[i]
			widget.setText(str(self.buttons.index(widget)))
                        try: 
				self.disconnect(widget, 0, 0, 0)
			except:
				pass
		for i in range(rows * cols):	
			widget = self.buttons[i]
			self.connect(widget, SIGNAL("clicked()"), lambda clickedWidget = self.buttons.index(widget): self.showQEditor(clickedWidget))
