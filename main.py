"""
* Taitotalo Python 30.11.2022
* main.py
* description
* Created by Samu Reinikainen
"""

from main_form import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.select_src.clicked.connect(self.selectSource)
        self.ui.select_dst.clicked.connect(self.selectDest)

    def selectSource(self):
        folderPath = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        qtw.QMessageBox.Information(self, 'Succes', str(folderPath))
        self.ui.source_folder.text = folderPath

    def selectDest(self):
        folderPath = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.source_dest.text = folderPath



# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()