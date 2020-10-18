import pytesseract as tesseract

from PIL import Image


def main():
  response = tesseract.image_to_data(
    Image.open('./ocr/images/cpfl.jpeg'),
    lang='por',
  )

  print(response)


if __name__ == '__main__':
  main()