import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('imagem_com_duas_maos.jpg')

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
p
# Aplicar a detecção de bordas com o algoritmo Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Aplicar a transformada de Hough para detectar linhas retas na imagem
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Calcular o ângulo médio das linhas detectadas
angles = [np.arctan2(y2-y1, x2-x1) for x1,y1,x2,y2 in lines[:,0]]
median_angle = np.median(angles)

# Rotacionar a imagem para alinhar as linhas com os eixos da imagem
rotation_matrix = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), median_angle*180/np.pi, 1)
rotated = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]))

# Separar as duas áreas de interesse na imagem
crop1 = rotated[100:500, 100:400]
crop2 = rotated[100:500, 450:750]

# Executar a função determine_poker_hand em cada uma das imagens recortadas
hand1 = determine_poker_hand(recognize_cards(crop1))
hand2 = determine_poker_hand(recognize_cards(crop2))

# Comparar as duas mãos e determinar a mão mais forte
if hand1 > hand2:
    print("A primeira mão é a mais forte. Valor: ", hand1)
else:
    print("A segunda mão é a mais forte. Valor: ", hand2)
