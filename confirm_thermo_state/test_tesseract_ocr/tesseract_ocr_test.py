import cv2
import pytesseract

# Spécifiez le chemin de Tesseract si ce n'est pas dans votre PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Charger l'image
image_path = r"C:\Users\15142\OneDrive - USherbrooke\S7\STAGE-T5\VISION\IMAGE_TEST\keyboard\small.png"
image = cv2.imread(image_path)

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Appliquer un seuillage pour améliorer la qualité de l'image pour OCR
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Utiliser Tesseract pour faire l'OCR
text = pytesseract.image_to_string(thresh, lang='eng')  # Assurez-vous de spécifier la langue appropriée

# Afficher le texte extrait
print(text)