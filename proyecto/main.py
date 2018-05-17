from Video import *
from cv2 import *



if __name__== '__main__':
    vide=Video("direccion del video a modificar")
    im=cv2.imread("direccion de imagen para cargar",cv2.IMREAD_COLOR)
    #recibe segundo de inicio, segundo de terminacion, posicion en fila, posicion en columna y la imagen
    #cabe resaltar que se le pueden meter tantas imagenes se quieran para modificar el video 
    vide.anadirModificacion(4,8,60,60,im)
    vide.anadirModificacion(15,20,120,120,im)
    #recibe direccion para cargar la cancion
    vide.setMusica("mrdm.mp3")
    #guarda el video modificado
    vide.guardarVideoModificado("./plytchingon.mp4")
