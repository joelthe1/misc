import codecs
import sys

path = sys.argv[1]
sentence = []
corpus = []
with codecs.open(path, 'r', 'utf-8') as rfile, codecs.open('output/fixed_inp_ruberic.txt', 'w', 'utf-8') as wfile:
    for line in rfile.readlines():
        splitline = line.strip().split('\t')
        if 'Eph' not in  splitline[0]:
            continue
        seg = '/'.join(splitline[1:3])
        print(splitline[0])
        if '.' in splitline[1]:
            sentence.append(seg)
            corpus.append(' '.join(sentence))
            sentence = []
            continue
        sentence.append(seg)
    wfile.write('\n'.join(corpus))
