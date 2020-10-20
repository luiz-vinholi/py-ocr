import pytesseract as tesseract
import numpy
import cv2

from PIL import Image
from pytesseract import Output
from typing import Any, Tuple


def treat_image():
  image = Image.open('./src/images/cpfl.jpeg').convert('RGB')
  image = numpy.asarray(image).astype(numpy.uint8)
  image = cv2.detailEnhance(image, sigma_s=100, sigma_r=1)

  image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]
  
  treated_image = Image.fromarray(thresh)
  treated_image.save('./src/images/treated-cpfl.jpeg')

  image = Image.fromarray(image)

  return image, treated_image


def main():
  original_image, treated_image = treat_image()

  data = tesseract.image_to_data(
    treated_image,
    lang='por',
    output_type=Output.DICT,
  )

  texts_data = [
    {
      'top': data['top'][index],
      'left': data['left'][index],
      'width': data['width'][index],
      'height': data['height'][index],
      'confidence': data['conf'][index],
      'text': data['text'][index],
    } for index, text in enumerate(data['text'])
      if text.strip() and text == 'TOTAL'
  ]

  for text_data in texts_data:
    areas = (
      text_data['left'],
      text_data['top'],
      text_data['left'] + text_data['width'] + 70,
      text_data['top'] + text_data['height'] + 20,
    )

    cropped_image = original_image.crop(areas)
    cropped_image.save('./src/images/')
    data = tesseract.image_to_data(
      cropped_image,
      lang='por',
      output_type=Output.DICT,
    )
    print(data)
    
  print(texts_data)
  

if __name__ == '__main__':
  main()