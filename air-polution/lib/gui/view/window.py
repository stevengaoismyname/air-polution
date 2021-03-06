import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class gen:
	def __init__(self, **kwargs):
		self.win = tk.Tk()
		self.widget = {}
		self.graph = _Graphics(master=self.win)
		return super().__init__(**kwargs)

	def setTitle(self, title):
		self.win.title(title)

	def addWidget(self, signal, name, text='', x=10, y=10):
		widget = _Widget(signal=signal, win=self.win, text=text, x=x, y=y)
		self.widget[name] = widget.gen()

	def draw(self, data):
		self.graph.clear()
		self.graph.draw(data)
		self.graph.setCanvas(pady=50)

	def addEventListener(self, key, signal, callback):
		self.widget[key].bind(signal, callback)

	def run(self, width=500, height=300):
		self.win.geometry(str(width) + 'x' + str(height))
		self.win.mainloop()

class _Widget:
	def __init__(self, **kwargs):
		self.win = kwargs['win']
		self.signal = kwargs['signal']
		self.text = kwargs['text']
		self.x = kwargs['x']
		self.y = kwargs['y']

	def gen(self):
		method = ['label', 'button', 'combobox']
		if self.signal == method[0]:
			return self._Label(self.text, self.x, self.y)
		elif self.signal == method[1]:
			return self._Button(self.text, self.x, self.y)
		elif self.signal == method[2]:
			return self._Combobox(self.text, self.x, self.y)

	def _Label(self, text, x, y):
		label = tk.Label(self.win, text=text)
		label.place(x=x, y=y)
		return label

	def _Button(self, text, x, y):
		button = tk.Button(self.win, text=text)
		button.place(x=x, y=y)
		return button

	def _Combobox(self, text, x, y):
		combobox = ttk.Combobox(self.win, text=text)
		combobox.place(x=x, y=y)
		return combobox

class _Graphics:
	def __init__(self, **kwargs):
		self.fig = Figure()
		self.canvas = FigureCanvasTkAgg(self.fig, master=kwargs['master'])
		
	def draw(self, data):
		self.subplot = self.fig.add_subplot(111)
		self.subplot.plot(data)

	def setCanvas(self, padx=0, pady=0):
		self.canvas.draw()
		self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill='x', padx=padx, pady=pady)

	def getCanvas(self, master, padx=0, pady=0):
		return self.canvas

	def clear(self):
		self.fig.clear()