# -*- coding: utf-8 -*-
'''
create a desktop app with a single CheckBox button to start SiafiWeb
'''

import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
                             QCheckBox)
from driver import create_driver

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUi()
        
    def initializeUi(self):
        self.setGeometry(0, 0, 1980, 1020)
        self.setWindowTitle("Graviola")
        
        self.setUpMainWindow()
        self.show()
        
    def setUpMainWindow(self):
        systems_label = QLabel('Which systems should be started?', self)
        systems_label.move(40, 60)
        
        siafiweb_cb = QCheckBox('SiafiWeb', self)
        siafiweb_cb.move(40, 90)
        siafiweb_cb.toggled.connect(self.siafiweb_driver)

    def siafiweb_driver(self, checked):
        if checked:
            self.siafiweb_driver = create_driver()
                    
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

