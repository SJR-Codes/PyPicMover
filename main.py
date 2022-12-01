"""
* Taitotalo Python 30.11.2022
* main.py
* description
* Created by Samu Reinikainen
"""

from ui_main_form import Ui_Form as Main_Form
from ui_view_log import Ui_Form as Log_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QPixmap

class LogWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.ui = Log_Form() #use qt designed form
        self.ui.setupUi(self)

        self.ui.select_src.clicked.connect(self.selectImage)

        #close button function
        self.ui.btnClose.clicked.connect(self.appClose)

    def selectImage(self):
        self.imgSource = qtw.QFileDialog.getOpenFileName(self,'Single File','','*.png')
        self.ui.img_source.setPlainText(self.imgSource[0])
        pixmap = QPixmap(self.imgSource[0])
        scaledPixmap = pixmap.scaled(
            self.ui.img_view.width(),
            self.ui.img_view.height(),
            qtc.Qt.AspectRatioMode.KeepAspectRatio,
            qtc.Qt.TransformationMode.SmoothTransformation
        )
        self.ui.img_view.setPixmap(scaledPixmap)

        # Optional, resize window to image size
        #self.resize(pixmap.width(),pixmap.height())

    def appClose(self):
        self.close()

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dirty = False
        self.logWindow = None  # No external window yet.

        self.ui = Main_Form()
        self.ui.setupUi(self)
        
        #select buttons for directory select functions
        self.ui.select_src.clicked.connect(self.selectSource)
        self.ui.select_dst.clicked.connect(self.selectDest)

        #text input changes sets form dirty
        self.ui.source_folder.textChanged.connect(self.valuesChanged)
        self.ui.dest_folder.textChanged.connect(self.valuesChanged)

        #close button function
        self.ui.btnClose.clicked.connect(self.appClose)
        #open log view widget/window button function
        self.ui.btnViewLog.clicked.connect(self.showLog)

    def selectSource(self):
        self.folderPathSource = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        #qtw.QMessageBox.information(self, 'Success', str(folderPath))
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