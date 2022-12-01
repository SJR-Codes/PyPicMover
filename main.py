"""
* Taitotalo Python 30.11.2022
* main.py
* description
* Created by Samu Reinikainen
"""

from main_form import Ui_Form
from view_log import Ui_Form as Log_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class LogWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Log_Form()
        self.ui.setupUi(self)
        #close button function
        self.ui.btnClose.clicked.connect(self.appClose)

    def appClose(self):
        self.close()

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dirty = False
        self.logWindow = None  # No external window yet.

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

        self.ui.btnViewLog.clicked.connect(self.showLog)

    def selectSource(self):
        self.folderPathSource = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        #qtw.QMessageBox.information(self, 'Succes', str(folderPath))
        self.ui.source_folder.setPlainText(self.folderPathSource)

    def selectDest(self):
        self.folderPathDest = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.dest_folder.setPlainText(self.folderPathDest)

    def valuesChanged(self):
        self.dirty = True

    def showLog(self):
        if self.logWindow is None:
            self.logWindow = LogWindow()
        self.logWindow.show()

    def appClose(self):
        ok = True

        if self.dirty:
            # dlg = qtw.QMessageBox(self)
            # dlg.setWindowTitle("Unsaved changes!")
            # dlg.setText("Really close? Unsaved changes will be lost!")
            # dlg.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No)
            # dlg.setIcon(qtw.QMessageBox.Warning)
            # buttonClicked = dlg.exec()

            buttonClicked = qtw.QMessageBox.warning(
                self,
                "Unsaved changes!",
                "Really close? Unsaved changes will be lost!",
                buttons = qtw.QMessageBox.Yes | qtw.QMessageBox.No,
                defaultButton = qtw.QMessageBox.Yes,
            )

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