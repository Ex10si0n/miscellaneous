#! /usr/bin/env python3
import sys
import os
import json
from os.path import join as pjoin

def main():
    usage =\
    '''
Sui-Memo is a simple, fast CLI Memo.
Can be used to quickly mapping English phrase to Chinese meaning.

Usage:
  s [key] [value]        add a mapping [key] -> [value]
  s list                 list all recorded values

 More functions to be developed
    '''

    if len(sys.argv) == 1:
        print(usage)
        return

    output_dir = os.getenv("HOME")
    list_dir = os.listdir(output_dir)

    if len(sys.argv) == 3:
        mapping = {sys.argv[1]: sys.argv[2]}

        if 'mapping.json' in list_dir:
            fr = open(pjoin(output_dir, 'mapping.json'))
            model = json.load(fr)
            fr.close()
            for i in mapping:
                model[i] = mapping[i]
            jsObj = json.dumps(model, ensure_ascii=False)
            with open(pjoin(output_dir, 'mapping.json'), "w") as fw:
                fw.write(jsObj)
                fw.close()
        else:
            os.system('touch ~/mapping.json')
            jsObj = json.dumps(mapping, ensure_ascii=False)
            with open(pjoin(output_dir, 'mapping.json'), "w") as fw:
                fw.write(jsObj)
                fw.close()
        return

    if len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            if 'mapping.json' in list_dir:
                fr = open(pjoin(output_dir, 'mapping.json'), "r")
                model = json.load(fr)
                fr.close()
                for element in model:
                    print('%-70s%s' % (element, model[element]))
            else:
                print('None')

        else:
            print(usage)
            return



if __name__ == '__main__':
    main()
