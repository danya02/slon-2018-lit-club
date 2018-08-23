#!/usr/bin/python3
import sys
try:
    lang = sys.argv[1]
except IndexError:
    lang = None

import os
text = '{main}'
while '{' in text:
    if '}' not in text:
        raise ValueError('Open tag without close tag.')
    before,sep,after = text.partition('{')
    topic,sep,after = after.partition('}')
    topic+='.txt'
    if os.path.sep in (lang+os.path.sep+topic if lang else topic):
        try:
            os.makedirs(os.path.dirname((lang+os.path.sep+topic if lang else topic)))
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass
    if not lang:
        try:
            with open(topic) as o:
                inset = o.read()
        except FileNotFoundError:
            inset = '####{}####'.format(topic)
            with open(topic,'w') as o:
                o.write(inset)
    else:
        try:
            with open(lang+os.path.sep+topic) as o:
                inset = o.read()
        except FileNotFoundError:
            try:
                with open(topic) as o:
                    inset = o.read()
            except FileNotFoundError:
                inset = '####{}####'.format(topic)
                with open(topic,'w') as o:
                    o.write(inset)
            inset+=f'({lang+os.path.sep+topic})'
            with open(lang+os.path.sep+topic,'w') as o:
                o.write(inset)

    if inset[-1]=='\n':
        inset = inset[:-1]
    inset = inset.replace('\n\n','\t'*64).replace('\n',' ').replace('\t'*64,'\n\n')
    text = before+inset+after
with open('output'+(f'.{lang}' if lang else '')+'.txt','w') as o:
    o.write(text)
