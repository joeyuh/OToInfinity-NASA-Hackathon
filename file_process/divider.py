import os

rootdir = './dataset/'
pooldir = './pdf_pool/'
keydir = './seq2seq/rawdata/a/'
for filename in os.listdir(rootdir):
    suffix = filename.split('.')[-1]
    if suffix == 'pdf':
        os.rename(rootdir+filename, pooldir+filename)

for filename in os.listdir(pooldir):
    name = filename+'.txt'
    os.rename(rootdir+name,keydir+name)

