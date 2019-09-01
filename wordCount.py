import string
import sys
def main(argv):
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    word_list = {}
    temp = 0
    PunctuationTranslator = str.maketrans(string.punctuation,' '*len(string.punctuation))

    with open(inputfile) as file:
        for line in file:
            line =line.translate(PunctuationTranslator)
            line = line.lower()
            values = line.split()
            for i in values:
                if i in word_list:
                    temp = word_list[i]
                    word_list[i] = temp + 1
                else:
                    word_list[i] = 1
    OutFile = open(outputfile, "w+")
    for i in sorted(word_list.keys()):
        curLine = i+" "+ str(word_list[i])
        OutFile.write(curLine + '\n')
    OutFile.close()

main(sys.argv)
