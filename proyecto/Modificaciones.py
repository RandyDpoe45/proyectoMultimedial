from cv2 import *

class Modificaciones (object):
    def __init__(self,img,segIni,segFin,posx,posy):
        self.im=img
        self.height, self.width, self.channels = self.im.shape
        self.segIni=segIni
        self.segFin=segFin
        self.posy=posy
        self.posx=posx
        
        
    def pertenece(self,segundo):
        if(segundo>=self.segIni and segundo<=self.segFin):
            return True
        