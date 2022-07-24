from langdetect import detect
from googletrans import Translator,constants

text = input("Enter the text:")
print(detect(text))

print(' ')

translator = Translator()
translation = translator.translate(text)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

