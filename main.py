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

        self.dirty = False

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #select buttons for directory select functions
        self.ui.select_src.clicked.connect(self.selectSource)
        self.ui.select_dst.clicked.connect(self.selectDest)

        #text input changes
        self.ui.source_folder.textChanged.connect(self.valuesChanged)
        self.ui.dest_folder.textChanged.connect(self.valuesChanged)

        #close button function
        self.ui.btnClose.clicked.connect(self.appClose)

    def selectSource(self):
        self.folderPathSource = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        #qtw.QMessageBox.information(self, 'Succes', str(folderPath))
        self.ui.source_folder.setPlainText(self.folderPathSource)

    def selectDest(self):
        self.folderPathDest = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.dest_folder.setPlainText(self.folderPathDest)

    def valuesChanged(self):
        self.dirty = True

    def appClose(self):
        ok = True

        if self.dirty:
            dlg = qtw.QMessageBox(self)
            dlg.setWindowTitle("Unsaved changes!")
            dlg.setText("Really close? Unsaved changes will be lost!")
            dlg.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No)
            dlg.setIcon(qtw.QMessageBox.Question)
            buttonClicked = dlg.exec()

            if buttonClicked == qtw.QMessageBox.Yes:
                ok = True
            else:
                ok = False

        if ok:
            self.close()



# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    app = qtw.QApplication([])

    widget = MainWindow()
    widget.show()

    app.exec_()