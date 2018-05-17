from cv2 import *
import numpy as np
from Modificaciones import Modificaciones
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mp

class Video(object):
    # por default la ruta del sonido es la misma del video
    #se carga el video en con opencv para poder editarlo
    def __init__(self, ruta):
        self.vid=cv2.VideoCapture(ruta)
        self.fps=np.ceil(self.vid.get(cv2.CAP_PROP_FPS))
        self.modificaciones=[]
        self.musica=ruta
        
    #crea una nueva modificacion y la anade a la lista
        
    def anadirModificacion(self,segIni,segFin,posx,posy,img):
        segIni=np.int(segIni*self.fps)
        segFin=np.int(segFin*self.fps)
        self.modificaciones.append(Modificaciones(img,segIni,segFin,posx,posy))
    #retorna el frame armado  y si es necesario modificado de acuerdo a si existe o no modificacion en ese segundo 
    def mostrarFrame(self,segundo,set):
        segundo=np.int(segundo*self.fps)
        num=self.buscarModificacion(segundo)
        if(set==True):
            self.vid.set(1,segundo)
        ret, frame = self.vid.read()
        if(ret==True):
            if(num>=0):
                m=self.modificaciones[num]
                frame[m.posy:m.posy+m.height,m.posx:m.posx+m.width]=m.im
            
            return  (ret,frame)
        else:
            return (False,-1)
    #retorna el indice de la modificacion que tiene el frame en ese segundo 
    def buscarModificacion(self,segundo):
        for i in range(len(self.modificaciones)):
            if(self.modificaciones[i].pertenece(segundo)):
                return i
            i+=1
        return -1
    #pone el video en un segundo especifico
    def setVideoF(self,segundo):
        segundo=np.int(segundo*self.fps)
        self.vid.set(1,segundo)
    
    def guardarVideoModificado(self,rut):
        
        width = self.vid.get(3)
        height = self.vid.get(4)
        fourcc = VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter("./temp/video.avi",fourcc, self.fps, (int(width),int(height)))
        self.setVideoF(0)
        i=0;
        while(True):
            ret, frame = self.mostrarFrame(i,False)
            if(ret==True):
                out.write(frame)
            else:
                break
            i+=(1/self.fps)
        out.release()
        
        videoclip = VideoFileClip("./temp/video.mp4")
        background_music = mp.AudioFileClip(self.musica).set_duration(videoclip.duration)
        new_clip = videoclip.set_audio(background_music)
        new_clip.write_videofile("final_cut.mp4")
        
        del videoclip
        
    #actualiza la direccion del sonido para poner de fondo
    def setMusica(self, ruta):
        self.musica= ruta
        
    
        
    