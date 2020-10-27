from typing import Any, Dict, List
import pytesseract as tesseract

from pytesseract import Output

Keywords = List[Dict[str, Any]]


class OCRService:
    def __init__(self, image, lang='por'):
        data = tesseract.image_to_data(
            image,
            lang=lang,
            output_type=Output.DICT,
        )

        self.data = [
            {
                'top': data['top'][index],
                'left': data['left'][index],
                'width': data['width'][index],
                'height': data['height'][index],
                'confidence': data['conf'][index],
                'text': data['text'][index],
            } for index, text in enumerate(data['text'])
            if text.strip()
        ]

    def get_data_from_keywords(self, keywords: Keywords):
        print(keywords)
