#!/usr/bin/python3
import os
text = '{main}'
while '{' in text:
    if '}' not in text:
        raise ValueError('Open tag without close tag.')
    before,sep,after = text.partition('{')
    topic,sep,after = after.partition('}')
    topic+='.txt'
    if os.path.sep in topic:
        try:
            os.makedirs(os.path.dirname(topic))
        except FileExistsError:
            pass
    try:
        with open(topic) as o:
            inset = o.read()
    except FileNotFoundError:
        inset = '####{}####'.format(topic)
        with open(topic,'w') as o:
            o.write(inset)
    if inset[-1]=='\n':
        inset = inset[:-1]
    text = before+inset+after
with open('output.txt','w') as o:
    o.write(text)
