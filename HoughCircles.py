# Rodrigo Luís Zimmermann
import sys
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def main(argv):
    
    # Abri a imagem para a biblioteca openCV
    src = cv2.imread('iris.jpg', cv2.IMREAD_COLOR)
    
    # Criando a escala de cinza para o método HoughCircles
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Descobre o círculo da íris
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 6,
                               param1=30, param2=90,
                               minRadius=5, maxRadius=60)
    
    # Remove íris
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
      center = (i[0], i[1])
      radius = i[2]
      value = i
      cv2.circle(src, center, radius, (255, 255, 255), -1)
    
    # Resultado 1
    cv2_imshow(src)

    # Descobre o círculo da pupila
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 6,
                               param1=30, param2=90,
                               minRadius=130, maxRadius=249)
   
    # Pegando as dimensões da pupila
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
      center = (i[0], i[1])
      radius = i[2]
      value = i

    # Pintando a parte de fora da pupila
    mask = np.zeros_like(src)
    mask = cv2.circle(mask, center, radius, (255, 255, 255), -1)
    result = cv2.bitwise_and(src, mask)
    cv2_imshow(result)

if __name__ == "__main__":
    main(sys.argv[1:])