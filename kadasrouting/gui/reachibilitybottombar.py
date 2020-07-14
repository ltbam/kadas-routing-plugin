import os
import logging

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget

from kadas.kadasgui import (
    KadasBottomBar, 
    KadasPinItem, 
    KadasItemPos, 
    KadasMapCanvasItemManager, 
    KadasLayerSelectionWidget
    )
from kadasrouting.gui.locationinputwidget import LocationInputWidget, WrongLocationException
from kadasrouting import vehicles
from kadasrouting.utilities import iconPath, pushMessage, pushWarning

from qgis.utils import iface
from qgis.core import (
    Qgis,
    QgsProject,
    QgsCoordinateReferenceSystem,
    )

WIDGET, BASE = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'reachibilitybottombar.ui'))

class ReachibilityBottomBar(KadasBottomBar, WIDGET):

    def __init__(self, canvas, action):
        KadasBottomBar.__init__(self, canvas, "orange")
        self.setupUi(self)
        self.setStyleSheet("QFrame { background-color: orange; }")
        self.action = action
        self.canvas = canvas

        self.btnClose.setIcon(QIcon(":/kadas/icons/close"))
        self.btnClose.setToolTip('Close reachibility dialog')

        self.action.toggled.connect(self.actionToggled)
        self.btnClose.clicked.connect(self.action.toggle)

        self.btnCalculate.clicked.connect(self.calculate)

        self.originSearchBox = LocationInputWidget(canvas, locationSymbolPath=iconPath('pin_origin.svg'))
        self.layout().addWidget(self.originSearchBox, 2, 1)

        self.comboBoxVehicles.addItems(vehicles.vehicles)

        self.comboBoxReachibiliyMode.addItems(
            ['Isochrone', 'Isodistance']
        )

        # Handling HiDPI screen, perhaps we can make a ratio of the screen size
        # size = QDesktopWidget().screenGeometry()
        # if size.width() >= 3200 or size.height() >= 1800:
        #     self.setFixedSize(self.size() / 1.5)

    def createLayer(self, name):
        pushMessage('create layer')

    def calculate(self):
        pushMessage('Calculating reachibility')

    # def clearPins(self):
    #     """Remove all pins from the map
    #     Not removing the point stored.
    #     """
    #     # remove origin pin
    #     self.originSearchBox.removePin()
    #     # remove destination poin
    #     self.destinationSearchBox.removePin()
    #     # remove waypoint pins
    #     for waypointPin in self.waypointPins:
    #         KadasMapCanvasItemManager.removeItem(waypointPin)

    # def addPins(self):
    #     """Add pins for all stored points."""
    #     self.originSearchBox.addPin()
    #     self.destinationSearchBox.addPin()
    #     for waypoint in self.waypoints:
    #         self.addWaypointPin(waypoint)

    def actionToggled(self, toggled):
        pushMessage('action toggle')
        # if toggled:
        #     self.addPins()
        # else:
        #     self.clearPins()