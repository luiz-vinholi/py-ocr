import pytesseract as tesseract

from pytesseract import Output

from handlers.image import Image


def main():
    image = Image('./src/images/cpfl.jpeg').treat()

    data = tesseract.image_to_data(
        image.treated_image,
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
            text_data['left'] + text_data['width'],
            text_data['top'] + text_data['height'] + 20,
        )

        cropped_image = image.this_image.crop(areas)
        cropped_image.save('./src/images/cropped-cpfl.jpeg')
        data = tesseract.image_to_data(
            cropped_image,
            lang='por',
            output_type=Output.DICT,
        )
        print(data)

    print(texts_data)


if __name__ == '__main__':
    main()
