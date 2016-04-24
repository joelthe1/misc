import codecs
import sys
import re

num_pat = re.compile(r' G[0-9]+')
bracket_open_pat = re.compile(r'{VAR[0-9]:')
bracket_pat = re.compile(r'[{}\[\]]')
space_pat = re.compile(r' {2,}')
special_pat = re.compile(r'ινα τι')
eng_pat = re.compile(r'[A-Z0-9]')

path = sys.argv[1]
corpus = []
with codecs.open(path, 'r', 'utf-8') as rfile, codecs.open('input/ubs4/fixed_inp_ubs4.txt', 'w', 'utf-8') as wfile:
    for line in rfile.readlines():
        splitline = line.strip().split('\t')
        if len(splitline) < 5 or '49N' in  splitline[0] or splitline[0].startswith('#'):
            continue
        try:
            v = splitline[5]
        except IndexError:
            continue
        line = num_pat.sub('', splitline[5])
        line = bracket_open_pat.sub('', line)
        line = bracket_pat.sub('', line)
        line = space_pat.sub(' ', line)
        line = special_pat.sub('ινατι', line)
        line = line.strip()
        segs = line.split(' ')
        tagged_segs = []
        if segs[0] == '':
            continue
        if len(segs)%2 != 0:
            if ':' in segs[-1]:
                segs = segs[:-1]
            else:
                for i in range(0, len(segs)-1):
                    if eng_pat.match(segs[i][:1]) is not None and eng_pat.match(segs[i+1][:1]) is not None:
                        segs.remove(segs[i])
                        break
        if len(segs)%2 != 0:
            print('errored', splitline, segs,'\n')
        for i in range(0, len(segs)-1, 2):
            tagged_segs.append(segs[i]+'/'+segs[i+1])
        corpus.append(' '.join(tagged_segs))
    wfile.write('\n'.join(corpus))
