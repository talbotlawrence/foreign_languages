#!/usr/bin/python 

# Author: Talbot Lawrence

import json
from googletrans import Translator

def main():
    """ """

    print("Running script now.....")

    try:
        with open('sentences.txt') as f:
           sentences = f.readlines()
    except Exception as e:
        print("Had issues reading the variables from the sentences.txt file: {}".format(e))
    except FileNotFoundError as fnfe:
        print("The file was not found: {}".format(fnfe))


    translator = Translator()

    try:
        with open('italian.txt', 'w') as i:
            for sentence in sentences:
                translation = translator.translate(sentence, dest='it')
                i.write(translation.origin.encode('utf-8').strip())
                i.write("\n")
                i.write(translation.text.encode('utf-8').strip())
                i.write("\n")
                i.write("\n")
    except Exception as e:
        print("Had issues reading the variables from the italian.txt file: {}".format(e))
    except FileNotFoundError as fnfe:
        print("The file was not found: {}".format(fnfe))


if __name__ == '__main__':
    main()
