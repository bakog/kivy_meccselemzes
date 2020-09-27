# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from datetime import datetime

class Start(Screen):

    def start_btn(self):
        App.get_running_app().passz_ok = 0
        App.get_running_app().passz_false = 0
        App.get_running_app().csel_ok = 0
        App.get_running_app().csel_false = 0
        App.get_running_app().labdaszerzes = 0
        App.get_running_app().becsuszas = 0
        App.get_running_app().blokk = 0
        App.get_running_app().loves_gol = 0
        App.get_running_app().loves_kapufa = 0
        App.get_running_app().loves_melle = 0
        App.get_running_app().kezdes = datetime.now()
        App.get_running_app().vege = ""
        print(App.get_running_app().passz_ok, App.get_running_app().kezdes)


class Actions(Screen):

    def passz_jo_release(self):
        # App.get_running_app().passz_ok += 1
        Elemzes.passz_ok += 1
        app = App.get_running_app()
        Elemzes.test += 1
        print(Elemzes.test, Elemzes.passz_ok, app)

    def passz_rossz_release(self):
        App.get_running_app().passz_false += 1

    def csel_jo_release(self):
        App.get_running_app().csel_ok += 1

    def csel_rossz_release(self):
        App.get_running_app().csel_false += 1

    def labdaszerzes_release(self):
        App.get_running_app().labdaszerzes += 1

    def becsuszas_release(self):
        App.get_running_app().becsuszas += 1

    def blokk_release(self):
        App.get_running_app().blokk += 1

    def loves_gol_release(self):
        App.get_running_app().loves_gol+= 1

    def loves_kapufa_release(self):
        App.get_running_app().loves_kapufa += 1

    def loves_melle_release(self):
        App.get_running_app().loves_melle += 1

class Statisztika(Screen):
    passz_ok = StringProperty()
    passz_false = StringProperty()
    csel_ok = StringProperty()
    csel_false = StringProperty()
    labdaszerzes = StringProperty()
    becsuszas = StringProperty()
    blokk = StringProperty()
    loves_gol = StringProperty()
    loves_kapufa = StringProperty()
    loves_melle = StringProperty()
    kezdes = ObjectProperty(None)
    vege = ObjectProperty(None)
    passz_number = NumericProperty()
    passz_ok_arany = StringProperty()
    loves_number = NumericProperty()
    csel_number = NumericProperty()
    csel_ok_arany = StringProperty()
    loves_ok_arany = StringProperty()

    def megnez(self):
        print("kiindulo:", Elemzes.passz_ok)
        self.passz_ok = str(Elemzes.passz_ok)

        self.passz_false = str(App.get_running_app().passz_false)
        self.csel_ok = str(App.get_running_app().csel_ok)
        self.csel_false = str(App.get_running_app().csel_false)
        self.labdaszerzes = str(App.get_running_app().labdaszerzes)
        self.becsuszas = str(App.get_running_app().becsuszas)
        self.blokk = str(App.get_running_app().blokk)
        self.loves_gol = str(App.get_running_app().loves_gol)
        self.loves_kapufa = str(App.get_running_app().loves_kapufa)
        self.loves_melle = str(App.get_running_app().loves_melle)
        self.kezdes = App.get_running_app().kezdes
        self.vege = App.get_running_app().vege
        self.passz_number = App.get_running_app().passz_ok + App.get_running_app().passz_false
        self.loves_number = App.get_running_app().loves_gol + App.get_running_app().loves_kapufa + App.get_running_app().loves_melle
        self.csel_number = App.get_running_app().csel_false +App.get_running_app().csel_ok
        try:
            self.csel_ok_arany = str(round(App.get_running_app().csel_ok /(self.csel_number / 100), 2)) + " %"
        except ZeroDivisionError:
            self.csel_ok_arany = "-"
        try:
            self.passz_ok_arany = str(round(App.get_running_app().passz_ok / (self.passz_number / 100), 2)) + " %"
        except ZeroDivisionError:
            self.passz_ok_arany = "-"
        try:
            self.loves_ok_arany = str(round((App.get_running_app().loves_kapufa +App.get_running_app().loves_gol) / (self.loves_number / 100), 2)) + " %"
        except ZeroDivisionError:
            self.loves_ok_arany = "-"

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("elemzes.kv")


class Elemzes(App):

    passz_ok = 0
    passz_false = NumericProperty(0)
    csel_ok = NumericProperty(0)
    csel_false = NumericProperty(0)
    labdaszerzes = NumericProperty(0)
    becsuszas = NumericProperty(0)
    blokk = NumericProperty(0)
    loves_gol = NumericProperty(0)
    loves_kapufa = NumericProperty(0)
    loves_melle = NumericProperty(0)
    kezdes = ObjectProperty(None)
    vege = ObjectProperty(None)
    test = 0

    def build(self):
        return kv


if __name__ == "__main__":
    Elemzes().run()
