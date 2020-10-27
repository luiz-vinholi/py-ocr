import pytesseract as tesseract

from pytesseract import Output

from services.image_service import ImageService
from services.ocr_service import OCRService


def main():
    image = ImageService('./src/images/cpfl.jpeg').treat()

    ocr = OCRService(image.treated_image)

    ocr.get_data_from_keywords([
        {
            'key': 'TOTAL',
            'regex': '[tl1/|][0o][tl1/|][a4][l1|]',
            'value_type': float,
        }
    ])

    # TODO - Crop image and get data values
    # for text_data in ocr.data:
    #     areas = (
    #         text_data['left'],
    #         text_data['top'],
    #         text_data['left'] + text_data['width'],
    #         text_data['top'] + text_data['height'],
    #     )

    #     cropped_image = image.original_image.crop(areas)
    #     cropped_image.save('./src/images/cropped-cpfl.jpeg')
    #     data = tesseract.image_to_data(
    #         cropped_image,
    #         lang='por',
    #         output_type=Output.DICT,
    #     )
    #     print(data)


if __name__ == '__main__':
    main()
