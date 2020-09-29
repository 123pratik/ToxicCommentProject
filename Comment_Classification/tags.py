import re
def tagremoval(text):
    comp = re.compile('<.*?>')
    cl_text = re.sub(comp, '', text)
    return cl_text

if __name__ == '__main__':
    print('')