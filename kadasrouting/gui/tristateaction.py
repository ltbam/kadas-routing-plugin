"""Tri state action.
"""
from PyQt5.QtWidgets import QWidgetAction, QCheckBox, QFrame, QHBoxLayout, QLabel, QAction
from PyQt5.QtCore import Qt

from kadasrouting.utilities import pushMessage

class TriStateAction(QWidgetAction):
    def __init__(self, *args, **kwargs):
        QWidgetAction.__init__(self, *args, **kwargs)
        self.checkBox = QCheckBox()
        self.checkBox.setTristate(True)
        self.widget = QFrame()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.checkBox)
        self.layout.addWidget(QLabel('TriState'))
        self.widget.setLayout(self.layout)
        self.widget.show()

        self.setDefaultWidget(self.widget)
        self.checkBox.stateChanged.connect(self.changed)

        self.checkBox.stateChanged.connect(self.checkBoxStateChanged)
    
    def setCheckState(self, checkState):
        self.checkBox.setCheckState(checkState)
    
    def checkState(self):
        return self.checkBox.checkState()

    def checkBoxStateChanged(state):
        pushMessage('Current state is %s' % state)
