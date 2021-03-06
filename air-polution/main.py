import tkinter as tk
from tkinter import messagebox
import threading
import lib.gui.view.window as Window
import lib.gui.model.mongo as Mongo
import lib.math as Math
import lib.air as Air

win = Window.gen()
interval = Math.interval()
MongoAir = Mongo.air()
info = Air.info()

win.setTitle('PM2.5趨勢監測器')
win.addWidget(signal='combobox', name='comboYear', x=10, y=10)
win.addWidget(signal='label', name='labelYear', text='年', x=70, y=10)
win.addWidget(signal='combobox', name='comboMonth', x=100, y=10)
win.addWidget(signal='label', name='labelMonth', text='月', x=160, y=10)
win.addWidget(signal='combobox', name='comboDay', x=190, y=10)
win.addWidget(signal='label', name='labelDay', text='日', x=250, y=10)
win.addWidget(signal='combobox', name='comboStation', x=280, y=10)
win.addWidget(signal='button', name='buttonSelect', text='查詢', x=380, y=8)
win.draw(data=[])

win.widget['comboYear'].configure(width=5)
win.widget['comboMonth'].configure(width=5)
win.widget['comboDay'].configure(width=5)
win.widget['comboStation'].configure(width=8)

win.widget['comboYear']['value'] = interval.get(low=88, high=105)
win.widget['comboMonth']['value'] = interval.get(low=1, high=12)
win.widget['comboDay']['value'] = interval.get(low=1, high=31)
win.widget['comboStation']['value'] = info.getStation()


def handler():
    win.widget['buttonSelect']['text'] = '處理中...'
    win.widget['buttonSelect']['state'] = 'disabled'
    year = str(1911 + int(win.widget['comboYear'].get()))
    month = win.widget['comboMonth'].get().zfill(2)
    day = win.widget['comboDay'].get().zfill(2)
    station = win.widget['comboStation'].get()

    try:
        timeseries = MongoAir.timeseries(
            station=station, date=year + '/' + month + '/' + day, item='PM2.5')
        win.draw(data=timeseries)
    except:
        messagebox.showinfo('Warning', '無資料回傳')

    win.widget['buttonSelect']['text'] = '查詢'
    win.widget['buttonSelect']['state'] = 'normal'


win.addEventListener('buttonSelect', '<Button-1>',
                     lambda e: threading.Thread(target=handler).start())
win.run()
