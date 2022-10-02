import os
from filter import Filter
a_dir = './seq2seq/rawdata/a/'
q_dir = './seq2seq/rawdata/q/'

for a in os.listdir(a_dir):
    name = a.split('.')[0]
    try:
        string = ''
        with open(a_dir+a, 'r') as f:
            string += f.read()
        flt = Filter(string)
        if flt.filter_for_space():
            os.remove(a_dir+a)
            print(f'{name}--(a)removed')
            os.remove(q_dir+name+'.txt')
            print(f'{name}--(q)removed')
    
    except:
        continue

for q in os.listdir(q_dir):
    name = q.split('.')[0]
    try:
        string = ''
        with open(q_dir+q, 'r') as f:
            string += f.read()
        flt = Filter(string)
        if flt.filter_for_space():
            os.remove(q_dir+q)
            print(f'{name}--(q)removed')
            try:        
                for a in os.listdir(a_dir):
                    a_name = a.split('.')[0]
                    
                    if name == a_name:
                        os.remove(a_dir+a)
                        print(f'{name}--(a)removed')
            except:
                continue
    
    except:
        print(f'{name}--read_failed')
    
print('all empty files were deleted')

    
