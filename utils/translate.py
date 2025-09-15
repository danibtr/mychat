from deep_translator import GoogleTranslator

def translate_message(msg):
    arabic = GoogleTranslator(source='en', target='ar').translate(msg)
    english = GoogleTranslator(source='ar', target='en').translate(msg)
    return f"{msg} | {arabic} | {english}"
