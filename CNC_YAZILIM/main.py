from serial import Serial
from random import randint
from time import sleep
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from CNC_GUI import Ui_MainWindow
import serial.tools.list_ports
import easygui

class Pencere(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnKes.setEnabled(False)
        self.ui.btnUcYukari.setEnabled(False)
        self.ui.btnUcAsagi.setEnabled(False)
        self.ui.btnYukari.setEnabled(False)
        self.ui.btnAsagi.setEnabled(False)
        self.ui.btnSaga.setEnabled(False)
        self.ui.btnSola.setEnabled(False)
        self.ui.btnHome.setEnabled(False)
        self.ui.btnBaslat.setEnabled(False)
        self.ui.btnDurdur.setEnabled(False)
        self.ui.btnDosyaSec.setEnabled(False)

        self.dosyaAdi = "dosya.txt"
        self.seciliPort = ""
        self.adimHiz = ""
        self.conn = Serial()
        self.comlist = []
        self.komutSayi = 0
        self.komutSira = 0

        self.timer = QTimer() 
        self.timer.timeout.connect(self.listele)
        self.timer.start(500)

        self.CNCTimer = QTimer()
        self.gcode = []
        self.CNCTimer.timeout.connect(self.uygula)

    def getText(self,seciliPort):
        self.seciliPort = seciliPort
    
    def getSpeed(self, adimHiz):
        self.adimHiz = adimHiz
        print(adimHiz)
    
    def listele(self):
        self.comlist = serial.tools.list_ports.comports()
        portListe = []
        for port in self.comlist:
            portListe.append(str(port).split(" ")[0])
        self.ui.cmbPort.clear()
        self.ui.cmbPort.addItems(portListe)

    def gonder(self, veri):
        print(veri)
        self.conn.write(veri.encode("utf8"))

    def gcodeList(self, fname):
        """ fname paratmetresi .gcode dosyasının
        girildiği parametredir.
        Bu fonksiyon tüm satırları sırasıyla bir diziye atar
        ve bu diziyi bize döndürür."""
        dosya  = open(fname,"r")
        kodlar = dosya.readlines()
        dosya.close()
        return kodlar

    def baglan(self):
        
        from serial import Serial
        self.conn.baudrate=9600
        try:
            self.conn.close()
        except:
            pass
        self.conn.setPort(self.seciliPort)
        sleep(1)
        self.conn.open()
        self.conn.close()
        sleep(1)
        self.conn.open()
        self.ui.btnBaglan.setEnabled(False)
        self.ui.btnKes.setEnabled(True)
        self.ui.btnUcYukari.setEnabled(True)
        self.ui.btnUcAsagi.setEnabled(True)
        self.ui.btnYukari.setEnabled(True)
        self.ui.btnAsagi.setEnabled(True)
        self.ui.btnSaga.setEnabled(True)
        self.ui.btnSola.setEnabled(True)
        self.ui.btnHome.setEnabled(True)
        self.ui.btnBaslat.setEnabled(False)
        self.ui.btnDurdur.setEnabled(False)
        self.ui.btnDosyaSec.setEnabled(True)

    def baglantiKes(self):
        from serial import Serial
        self.conn.baudrate=9600
        try:
            self.conn.close()
        except:
            pass
        self.ui.btnBaglan.setEnabled(True)
        self.ui.btnKes.setEnabled(False)
        self.ui.btnUcYukari.setEnabled(False)
        self.ui.btnUcAsagi.setEnabled(False)
        self.ui.btnYukari.setEnabled(False)
        self.ui.btnAsagi.setEnabled(False)
        self.ui.btnSaga.setEnabled(False)
        self.ui.btnSola.setEnabled(False)
        self.ui.btnHome.setEnabled(False)
        self.ui.btnBaslat.setEnabled(False)
        self.ui.btnDurdur.setEnabled(False)
        self.ui.btnDosyaSec.setEnabled(False)
        self.ui.ilerleme.setProperty("value",0)
        self.ui.txtDosya.setText("")
    
    def ucYukari(self):
        self.gonder("G91\nG20\nG00 X0.000 Y0.000 Z" + self.adimHiz + "\n")

    def ucAsagi(self):
        self.gonder("G91\nG20\nG00 X0.000 Y0.000 Z-" + self.adimHiz + "\n")
    
    def yukari(self):
        self.gonder("G91\nG20\nG00 X0.000 Y" + self.adimHiz + " Z0.000\n")

    def asagi(self):
        self.gonder("G91\nG20\nG00 X0.000 Y-" + self.adimHiz + " Z0.000\n")
    
    def sola(self):
        self.gonder("G91\nG20\nG00 X-" + self.adimHiz + " Y0.000 Z0.000\n")
    
    def saga(self):
        self.gonder("G91\nG20\nG00 X" + self.adimHiz + " Y0.000 Z0.000\n")
    
    def home(self):
        self.gonder("G90\nG20\nG00 X0.000 Y0.000 Z0.000\n")
    
    def dosyaSec(self):
        path = easygui.fileopenbox()
        self.ui.txtDosya.setText(path)
        self.dosyaAdi = path
        self.gcode = self.gcodeList(self.dosyaAdi)
        self.komutSayi = len(self.gcode)
        self.komutSira = 0
        self.ui.ilerleme.setProperty("value",0)
        self.ui.btnBaslat.setEnabled(True)
        self.ui.btnDurdur.setEnabled(False)

    def baslat(self):
        self.CNCTimer.start(200)
        self.ui.btnBaslat.setEnabled(False)
        self.ui.btnDurdur.setEnabled(True)
    
    def durdur(self):
        self.CNCTimer.stop()
        self.ui.btnBaslat.setEnabled(True)
        self.ui.btnDurdur.setEnabled(False)

    def uygula(self):
        if(len(self.gcode)==0):
            self.komutSayi = 0
            self.komutSira = 0
            print("BITTI.")
            self.CNCTimer.stop()
            self.ui.txtDosya.setText("")
            self.ui.ilerleme.setProperty("value", 100)
        else:
            self.komutSira += 1
            self.ui.ilerleme.setProperty("value", (100/self.komutSayi)*self.komutSira )
            self.gonder(self.gcode[0])
            self.gcode.remove(self.gcode[self.gcode.index(self.gcode[0])])
            
if __name__ == '__main__':
    while 1:
        app = QApplication([])
        pencere = Pencere()
        pencere.show()
        app.exec_()