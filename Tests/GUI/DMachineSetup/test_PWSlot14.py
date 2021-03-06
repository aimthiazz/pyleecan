# -*- coding: utf-8 -*-

import sys
from random import uniform
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot14.PWSlot14 import PWSlot14


import pytest


@pytest.mark.GUI
class test_PWSlot14(TestCase):
    """Test that the widget PWSlot14 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW14(H0=0.10, H1=0.11, H3=0.12, W0=0.13, W3=0.14)
        self.widget = PWSlot14(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot14")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_H3.value(), 0.12)
        self.assertEqual(self.widget.lf_W0.value(), 0.13)
        self.assertEqual(self.widget.lf_W3.value(), 0.14)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H0, str(value))
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H0, value)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, value)

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_H3, str(value))
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H3, value)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W0, str(value))
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W0, value)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()  # Clear the field before writing
        value = round(uniform(0, 1), 4)
        QTest.keyClicks(self.widget.lf_W3, str(value))
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W3, value)

    def test_output_txt(self):
        """Check that the Output text is computed and correct
        """
        self.test_obj.slot = SlotW14(H0=0.005, H1=0.01, H3=0.025, W0=0.005, W3=0.02)
        self.widget = PWSlot14(self.test_obj)
        self.assertEqual(
            self.widget.w_out.out_slot_height.text(), "Slot height: 0.03987 m"
        )
