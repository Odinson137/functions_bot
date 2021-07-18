import pyperclip
from deep_translator import GoogleTranslator

def translated_buffer(langueage='ru', text='HELLO'):
    print(f"History:")
    copy_text = pyperclip.paste()
        
    while True:
        translated = GoogleTranslator(source='auto', target=langueage).translate(text)
        if translated != copy_text:
            text = copy_text
            translated = GoogleTranslator(source='auto', target=langueage).translate(text)
            pyperclip.copy(translated)
            print(f"{text} - {translated}")

  
