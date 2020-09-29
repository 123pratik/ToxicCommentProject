import re
def Puncremoval(text): #function to clean the word of any punctuation or special characters
    cl_text = re.sub(r'[?|!|\'|"|#]',r'', text)
    cl_text = re.sub(r'[.|,|)|(|\|/]',r' ',cl_text)
    cl_text = cl_text.strip()
    cl_text = cl_text.replace("\n"," ")
    return cl_text

if __name__ == '__main__':
    print('')
            
            
