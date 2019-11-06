from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WorkerSignals(QObject):
    """Class penyimpan sinyal untuk Class Worker"""
    # Untuk mengirimkan pesan error yang masuk ke exception
    exception = pyqtSignal(object)
    # Untuk mengirimkan hasil fungsi
    result = pyqtSignal(object)
    # Untuk mengirimkan status selesai proses
    done = pyqtSignal()

class Worker(QRunnable):
    """Class untuk melakukan multithreading"""
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            res = self.function(*self.args, **self.kwargs)
        except Exception as e:
            self.signals.exception.emit(e)
        else:
            self.signals.result.emit(res)
        finally:
            self.signals.done.emit()
