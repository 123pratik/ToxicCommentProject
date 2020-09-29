import re
def processed(text):
    processed_text = ""
    for word in text.split():
        processed_word = re.sub('[^a-z A-Z]+', ' ', word)
        processed_text += processed_word
        processed_text += " "
    processed_text = processed_text.strip()
    return processed_text

if __name__ == '__main__':
    print('')
