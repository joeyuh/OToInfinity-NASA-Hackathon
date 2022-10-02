from filter import Filter
import os 

rootdir = './seq2seq/rawdata/a/'
for filename in os.listdir(rootdir):
    try:
        string = ''
        with open(rootdir+filename, 'r') as f:
            string += f.read()
        flt = Filter(string)
        res = flt.filter_for_comma()

        with open(rootdir+filename, 'w') as f:
            f.write(res)
    except:
        print(f'{filename}--read_error')

