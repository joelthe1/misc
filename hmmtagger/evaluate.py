import re
import codecs

def separate(token):
    patt = re.compile(r'(.*)\/(.*)')
    res = patt.match(token)
    #TODO: if res: for safety
    word = res.group(1)
    tag = res.group(2)
    return {'word': word, 'tag': tag}

total_tags = 0
corr_tags = 0
with codecs.open('hmmoutput.txt', 'r', 'utf-8') as rfile, codecs.open('input/fixed_inp_ruberic.txt', 'r', 'utf-8') as rubericfile:
    for inp_line in rfile.readlines():
        ruberic_line = rubericfile.readline()

        inp_line_split = inp_line.strip().split(' ')
        ruberic_line_split = ruberic_line.strip().split(' ')
        total_tags += len(ruberic_line_split)
        for index, inp_token in enumerate(inp_line_split):
            inp = separate(inp_token)
            rub = separate(ruberic_line_split[index])
            if inp['word'] != rub['word']:
                print('Word mismatch. Errored out.')
                exit()
            if inp['tag'] == rub['tag']:
                corr_tags += 1

print('Accuracy is:', corr_tags/total_tags)
