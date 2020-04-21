
import cv2
import pytesseract
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

if __name__ == "__main__":
    img = cv2.imread("image/petra.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

    result = pytesseract.image_to_string(threshed)
    for word in result.split("\n"):
        # normalize NIK
        if "NIK" in word:
            nik_char = word.split()
            if "D" in word:
                word = word.replace("D", "0")
            if "?" in word:
                word = word.replace("?", "7")
            if "b" in word:
                word = word.replace("b", "6")

        print(word)
    plt.figure(figsize=(16, 12))
    plt.imshow(threshed)
    plt.show()
