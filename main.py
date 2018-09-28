from PIL import Image, ImageFilter,ImageDraw
# Script pega uma imagem de entrada, guarda a imagem e a partir dela cria-se outra imagem identica de menor tamanho e com marca d'agua
im = Image.open("porshe.jpg")
print ('Dimensões: ',im.size, im.mode)
im=im.resize((1200,593)) # Redimensionar a foto em um tamanho menor
img = ImageDraw.Draw(im)
texto = "Marca da agua"
pos = 50,50
img.text(pos, texto) # Escrever na foto a partir da posição pos
im.save("porshe2.jpg")
