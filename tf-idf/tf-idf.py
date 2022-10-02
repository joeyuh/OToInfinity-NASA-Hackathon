from math import degrees
import re
import jieba
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter
import os

def keyw_generate():
    pattern = '"(.*?)"'

    raw_words = []
    words = []
    with open('./tf-idf/datasets/word_list','r') as f:
        raw_words = f.readlines()

    #print(raw_words)
    for raw_word in raw_words:
        wd = re.compile(pattern, re.S).findall(raw_word)[-4]
        words.append(wd)

    return words


def networking(string):
    G = nx.Graph()
    
    str = string.split('.')
    # print(str)
    for s in str:
        
    
        ss = re.split(' ',s)
        for sss in ss:
            for yyy in ss:
                
                if yyy != sss:
                    
                    G.add_edge(sss,yyy)
    
    nx.draw(G,pos = nx.spring_layout(G),with_labels= True,node_size = 50)
    plt.savefig('network.png')
    
    degree = list(G.degree())
    degree.sort(key = itemgetter(1),reverse = True)
    
    closenessCentrality = nx.closeness_centrality(G)
    c = sorted(closenessCentrality.items(),key= lambda closenessCentrality:closenessCentrality[1],reverse=True)  #紧密中心性
    
    # print(c)


    return [degree, c]

class Extract:
    def __init__(self, d_c):
        self.degree_sorted = d_c[0]
        self.center_sorted = d_c[1]

    def generate_degree_object_list(self):
        obj = {}
        for dgr in self.degree_sorted:
            obj[dgr[0]] = dgr[1]

        return obj

    def generate_center_object_list(self):
        obj = {}
        for cent in self.center_sorted:
            obj[cent[0]] = cent[1]

        return obj

    
    def filter(self):
        ans = []
        res = {}
        d_obj = self.generate_degree_object_list()
        c_obj = self.generate_center_object_list()
        junk = ['that', 'with', 'by', 'our', 'we', 'as', 'is','from', 'data', 'within', 'also', 'were', 'between', 'We', 'Which','', 'the', 'and', 'of', 'to', 'in', 'a', 'for','or', ',', 'than','another', 'method','on','K', 'm/s','results','at','The','this','et\xa0','This','shown', 'shows', ':','an','0', 'be','Space', '±','~', 'For','are','observed', 'was','In','km','cases', 'line', 'can','range', 'obtained', 'mean', '1','2','3','4','5','6','7','8','9','10','Materials', 'ProcessingNASA-Langley', 'has','al','Research', '\x0cAdvanced',]
        for key in d_obj.keys():
            res[key] = d_obj[key] * c_obj[key]
            if res[key] >= 100 and not key in junk:
                ans.append(key)

        return [ans, res]

def segment(string,terms):

    st = re.findall(f'\w{terms}', string)
    return st
        
    

def read(path):
    str = ""
    with open(path, 'r') as f:
        str = f.read()
    return str

def save(targetdir,filename,content):
    str = ""
    for cont in content:
        str += cont + " "
    with open(targetdir+filename, 'w') as f:
        f.write(str)


if __name__ == '__main__':
    rootdir = "/Users/donglianghan/Desktop/NLP_for_NASA/abstracts/"

    for filename in os.listdir(rootdir):
        try: 
            path = rootdir+filename
            targetdir = "./tf-idf/results/"
            string = read(path)

            strs = segment(string)

            for i in range(len(str)):

                d_c = networking(string)

                ext = Extract(d_c)

                
                res = ext.filter()

            save(targetdir, filename, res)
        
        except:
            os.remove(rootdir+filename)
            continue


    
    
