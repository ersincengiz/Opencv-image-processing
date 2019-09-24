from PIL import Image
import pytesseract
import  cv2


originalImage = cv2.imread('C:\\Users\\asus\\Desktop\\tesseract-python-master\\17.png',cv2.IMREAD_UNCHANGED)
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black white image', blackAndWhiteImage)

r = 100.0 / blackAndWhiteImage.shape[1]
dim = (100, int(blackAndWhiteImage.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(blackAndWhiteImage, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)


cv2.imwrite('C:\\Users\\asus\\Desktop\\tesseract-python-master\\18.png',resized)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open("C:\\Users\\asus\\Desktop\\tesseract-python-master\\27.png")

text = pytesseract.image_to_string(im, lang = 'eng')

print(text)


