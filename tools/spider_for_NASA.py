import requests

from lxml import etree
import os
import json
from jsonpath import jsonpath
from time import sleep

class Spider:
    def __init__(self,url,headers):
        self.url = url
        self.headers = headers
        

    def getHtml(self):
        response = requests.get(url=self.url, headers=self.headers)
        html = response.text
        return html

    def xpath_analyzer(self):
        html = self.getHtml()
        tree = etree.HTML(html)

        name_list = tree.xpath('/html/body/app-root/div/div/app-search/mat-drawer-container/mat-drawer-content/div[2]/div/div/app-record-list/cdk-virtual-scroll-viewport/div[1]/app-record-item[1]')
        print(name_list)

    def search(self):
        for i in range(14700,19000):
            head = 'https://ntrs.nasa.gov/api/citations/'
            top = '202100'
            code = top+(str)(i)
            pdfs_dir = './pdfs/'
            src = head+code+'/downloads/'+'TM-'+code+'.pdf'
            src_form1 = head+code+'/downloads/BCookClimateDynChangingAccepted.pdf'
            html = requests.get(url=src_form1,headers=self.headers).text
            content = requests.get(url=src_form1,headers=self.headers).content
            print(html+f'--{i}')
            
            try:
                if(html != '{"statusCode":404,"message":"Not Found"}' and html != '{"statusCode":404,"message":"Not found"}'):
                    with open(pdfs_dir+code+'.pdf','wb') as f:
                        f.write(content)

            except:
                continue
            


    def jsonpath_analyzer(self):
        obj = json.load(open('./html.txt','r',encoding = 'utf-8'))

        res = jsonpath(obj,'$..results[*]')
        #print(res,len(res))
        
        src_list = []
        name_list = []
        #abstract_list = []
        keywords_list = []
        print(len(res))
        for i in range(len(res)):
            # and jsonpath(res[i],'$..abstract')
            if(jsonpath(res[i],'$..original') and jsonpath(res[i],'$..submissionId')  and jsonpath(res[i],'$..keywords')):
                try:
                    src_list.append(jsonpath(res[i],'$..original')[0])
                except:
                    continue
                try:
                    name_list.append((jsonpath(res[i],'$..submissionId')[0]))
                except:
                    continue
                # try:
                #     abstract_list.append(jsonpath(res[i],'$..abstract')[0])
                # except:
                #     continue
                try:
                    keywords_list.append(jsonpath(res[i],'$..keywords')[0])
                except:
                    continue


        
        
        if not os.path.exists('./pdfs'):
            os.mkdir('./pdfs')

        if not os.path.exists('./abstracts'):
            os.mkdir('./abstracts')

        if not os.path.exists('./keywords'):
            os.mkdir('./keywords')

        pdfs_dir = './pdfs/'
        abstract_dir = './abstracts/'
        keywords_dir = './keywords/'

        head = 'https://ntrs.nasa.gov/'

        print(len(src_list),len(name_list),len(keywords_list))
        print(name_list)
        #save pdfs
        for i in range(len(src_list)):
            try:
                src = head+src_list[i]
                content = requests.get(url=src, headers=self.headers).content
                with open(pdfs_dir+name_list[i]+'.'+'pdf','wb') as f:
                    f.write(content)
                print(name_list[i]+'pdf--saved')

            #save abstracts
                # with open(abstract_dir+name_list[i]+'.'+'txt','w') as f:
                #     f.write(abstract_list[i])
                # print(name_list[i]+'abstracts--saved')

            #save keywords
                key = ""
                for keyword in keywords_list[i]:
                    key += keyword+" "
                    print(key)
                with open(keywords_dir+name_list[i]+'.'+'txt','w') as f:
                    f.write(key)
                print(name_list[i]+'keywords--saved')

            except:
                print(name_list[i]+"is no longer exist")


        #print(src_list,name_list,abstract_list,keywords_list)


        

    



