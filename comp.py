import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

from compiler import Ui_Comp


class MyCompiler(QWidget, Ui_Comp):
    def __init__(self):
        super().__init__()
        if sys.platform != 'linux':
            QMessageBox.warning(self, "Could Not Open This File", "This File Is  linux file", QMessageBox.Ok)
            exit(1)
        self.setupUi(self)
        self.lang = ''
        self.file = ''
        self.path = ''
        self.name = ''
        self.file_to_compile = ''
        self.language_selector.currentTextChanged.connect(self.selectLangauge)
        self.select_file.clicked.connect(self.getFile)
        self.compile_file.clicked.connect(self.compile)
        self.run_file.clicked.connect(self.run)
        self.setWindowIcon(QIcon('bg.png'))

    def selectLangauge(self):
        self.lang = self.language_selector.currentText()
        print(self.lang)

    def getFile(self):
        self.file, _ = QFileDialog.getOpenFileName(self, 'Open A File ', )
        self.file = str(self.file)
        self.file_path_entry.setText(self.file)
        self.path = self.file.split('/')[:-1]
        self.path = '/'.join(self.path)
        print('Path=', self.path)
        self.name = self.file.split('/')[-1]
        print('name= ', self.name)

    def compile(self):
        try:
            print('compiling', self.name.split('.')[1])
        except:
            pass
        if self.file == '' and self.file_path_entry.text() != '':
            self.file = str(self.file_path_entry.text())
        if self.file:
            if self.name.split('.')[1] == 'c':
                self.language_selector.setCurrentText("C")
                txt = 'gcc ' + self.file + ' -o ' + self.path + '/' + self.name.split('.')[0]
                os.system(txt)
            if self.name.split('.')[1] == 'py':
                self.language_selector.setCurrentText("Python")
                t = '"' + self.file + '"'
                txt = sys.executable + ' ' + t
                os.system(txt)
            if self.name.split('.')[1] == 'pas':
                self.language_selector.setCurrentText("Pascal")
                txt = 'fpc ' + self.file
                os.system(txt)
            if self.name.split('.')[1] == 'java':
                self.language_selector.setCurrentText("java")
                txt = "javac " + self.file
                os.system(txt)
        elif self.file == '':
            QMessageBox.warning(self, "Invalid File", "Please choose a file directory and then Press Compile",
                                QMessageBox.Ok)

    def run(self):
        if self.file == '' and self.file_path_entry.text() != '':
            self.file = self.file_path_entry.text()
        if self.file:
            if self.name.split('.')[1] == 'c':
                self.language_selector.setCurrentText("C")
                txt = 'gcc ' + self.file + ' -o ' + self.path + '/' + self.name.split('.')[0]
                txtpp = txt + ' && ' + self.path + '/' + self.name.split('.')[0]
                os.system(txtpp)

            if self.name.split('.')[1] == 'py':
                self.language_selector.setCurrentText("Python")
                t = '"' + self.file + '"'
                txt = sys.executable + ' ' + t
                os.system(txt)

            if self.name.split('.')[1] == 'pas':
                self.language_selector.setCurrentText("Pascal")
                txt = 'fpc ' + self.file
                txtpp = txt + ' && ' + self.path + '/' + self.name.split('.')[0]
                os.system(txtpp)

        else:
            QMessageBox.warning(self, "Invalid File", "Please choose a file directory and then Press Run",
                                QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.desktop()
    win = MyCompiler()
    win.show()
    app.exec_()
