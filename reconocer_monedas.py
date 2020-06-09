import numpy as np
import cv2
  
original = cv2.imread('monedas2.jpg')#ruta de la imagen
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)#convertir la imagen a blanco y negro
gauss = cv2.GaussianBlur(gray, (5,5), 0) #aplicar effecto gauss
umbral = cv2.Canny(gauss, 50, 200) #definimos un umbral, cambiar valores depente la imagen
  
cv2.imshow('Color',original)    #mostrar imagen original
cv2.imshow('Escala de grises', gray) #mostrar en escala de grises
#cv2.imshow("suavizado", gauss)
cv2.imshow("umbral", umbral) # mostrar imagen en blanco y negro

(contornos,_) = cv2.findContours(umbral.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
print("He encontrado {} objetos".format(len(contornos)))
 
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)

  
cv2.waitKey(0)
cv2.destroyAllWindows()
