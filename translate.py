def translated_buffer(langueage='ru', text='HELLO'):
    print(f"History:")
        
    while True:
        translated = GoogleTranslator(source='auto', target=langueage).translate(text)
        if translated != pyperclip.paste():
            text = pyperclip.paste()
            translated = GoogleTranslator(source='auto', target=langueage).translate(text)
            pyperclip.copy(translated)
            print(f"{text} - {translated}")

  