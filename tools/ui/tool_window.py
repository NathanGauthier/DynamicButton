import os
import six
import sys



from Qt import QtCompat, QtWidgets, QtCore

from PySide2.QtWidgets import QApplication, QPushButton

from tools import datas
from engine import getEngine

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


ui_path = Path(__file__).parent / 'qt' / 'Window.ui'

UserRole = QtCore.Qt.UserRole




class ToolWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)




        for f in datas.get_files():
            addListWidgetItem(self.listItems, f, os.path.basename(f))

        for f in getEngine().implement:

            button = QPushButton(f)
            button.clicked.connect(self.buttonClicked)
            self.verticalLayout.addWidget(button)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        print(sender.text())

        item = self.listItems.currentItem()
        path = item.data(UserRole)



        function = getattr(getEngine(), sender.text() )(path)












def addListWidgetItem(listWidget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    listWidget.addItem(item)
    return item


#def open(filepath):
    #pm.openFile(filepath, force=True)





if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()

