from operator import truediv
import re

class Filter:
    def __init__(self,string):
        self.string = string
        
    def filter(self):
        junk = ['that', 'with', 'by', 'our', 'we', 'as', 'is','from', 'data', 'within', 'also', 'were', 'between', 'We', 'Which','', 'the', 'and', 'of', 'to', 'in', 'a', 'for','or', ',', 'than','another', 'method','on','K', 'm/s','results','at','The','this','et\xa0','This','shown', 'shows', ':','an','0', 'be','Space', '±','~', 'For','are','observed', 'was','In','km','cases', 'line', 'can','range', 'obtained', 'mean', '1','2','3','4','5','6','7','8','9','10','Materials', 'ProcessingNASA-Langley', 'has','al','Research', '\x0cAdvanced',]
        str_list = self.string.split(' ')
        res = ''
        for str in str_list:
            if not str in junk:
                res += str+" "
        return res

    def filter_for_comma(self):
        str_list = self.string.split(',')
        res = ''
        for str in str_list:
            res += str+' '
        return res

    def filter_for_space(self):
        string = re.sub('[ ]','',self.string)
        if not string:
            return True
        return False

        


