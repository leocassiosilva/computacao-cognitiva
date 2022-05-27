# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread(
    '/home/leocassio/PycharmProjects/computacao-cognitiva/atividades/Processamento_imagem/imgs/entrada/entrada.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1])
