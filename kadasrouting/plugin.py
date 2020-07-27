# -*- coding: utf-8 -*-
import os
import logging

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QWidgetAction, QCheckBox

from qgis.utils import iface

from qgis.core import QgsPluginLayerRegistry, QgsApplication

from kadas.kadasgui import KadasPluginInterface

from kadasrouting.utilities import icon, pushWarning
from kadasrouting.core.shortestpathlayer import ShortestPathLayerType
from kadasrouting.gui.shortestpathbottombar import ShortestPathBottomBar
from kadasrouting.gui.reachibilitybottombar import ReachibilityBottomBar
from kadasrouting.gui.tspbottombar import TSPBottomBar
from kadasrouting.gui.tristateaction import TriStateAction

logfile = os.path.join(os.path.expanduser("~"), ".kadas", "kadas-routing.log")
try:
    os.mkdir(os.path.dirname(logfile))
except FileExistsError:
    pass
logging.basicConfig(filename=logfile,level=logging.DEBUG)


class RoutingPlugin(QObject):

    def __init__(self, iface):
        QObject.__init__(self)
        
        self.iface = KadasPluginInterface.cast(iface)
        self.shortestPathBar = None
        self.reachibilityBar = None
        self.tspBar = None

    def initGui(self):
        # Routing menu
        self.shortestAction = QAction(icon("routing.png"), self.tr("Routing"))
        self.shortestAction.setCheckable(True)
        self.shortestAction.toggled.connect(self.showShortest)
        self.iface.addAction(self.shortestAction, self.iface.PLUGIN_MENU, self.iface.GPS_TAB)

        # Test
        self.cbx = QCheckBox('Tristate')
        self.cbxAction = QWidgetAction(self.iface)
        self.cbxAction.setDefaultWidget(self.cbx)
        # self.cbxAction.setCheckable(True)
        # self.cbxAction.toggled.connect(self.showShortest)
        self.iface.addAction(self.cbxAction, self.iface.PLUGIN_MENU, self.iface.GPS_TAB)

        # Reachibility menu
        self.reachabilityAction = QAction(icon("reachibility.png"), self.tr("Reachability"))
        self.reachabilityAction.setCheckable(True)
        self.reachabilityAction.toggled.connect(self.showReachibility)
        self.iface.addAction(self.reachabilityAction, self.iface.PLUGIN_MENU, self.iface.ANALYSIS_TAB)

        # TSP menu
        self.tspAction = QAction(icon("tsp.png"), self.tr("TSP"))
        self.tspAction.setCheckable(True)
        self.tspAction.toggled.connect(self.showTSP)
        self.iface.addAction(self.tspAction, self.iface.PLUGIN_MENU, self.iface.ANALYSIS_TAB)

        # Navigation
        # self.navigationAction = TriStateAction(self.iface)
        # self.navigationAction.setCheckable(True)
        # # self.tspAction.toggled.connect(self.showTSP)
        # self.iface.addAction(self.navigationAction, self.iface.PLUGIN_MENU, self.iface.GPS_TAB)

        reg = QgsApplication.pluginLayerRegistry()
        reg.addPluginLayerType(ShortestPathLayerType())

    def unload(self):
        self.iface.removeAction( self.shortestAction, self.iface.PLUGIN_MENU, self.iface.GPS_TAB)

    def showShortest(self, show=True):
        if show:
            if self.shortestPathBar is None:
                self.shortestPathBar = ShortestPathBottomBar(self.iface.mapCanvas(), self.shortestAction)
            self.shortestPathBar.show()
        else:
            if self.shortestPathBar is not None:
                self.shortestPathBar.hide()

    def showReachibility(self, show=True):
        if show:
            if self.reachibilityBar is None:
                self.reachibilityBar = ReachibilityBottomBar(self.iface.mapCanvas(), self.reachabilityAction)
            self.reachibilityBar.show()
        else:
            if self.reachibilityBar is not None:
                self.reachibilityBar.hide()


    def showTSP(self, show=True):
        if show:
            if self.tspBar is None:
                self.tspBar = TSPBottomBar(self.iface.mapCanvas(), self.tspAction)
            self.tspBar.show()
        else:
            if self.tspBar is not None:
                self.tspBar.hide()
