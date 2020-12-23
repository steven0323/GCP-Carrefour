import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup 
import requests 
from tqdm import tqdm 
import time
from datetime import date


def debugging(url):
        headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHaTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        info = {"product number":[],"price":[],"suggested price":[],"sales":[],'description':[],"specification":[],"detailed specification":[],"category 1":[],"category 2":[],"category 3":[],"category 4":[],"category 5":[]}
        r = requests.get(url,headers=headers)
        soup = BeautifulSoup(r.content,'html.parser')
        try:
            info['product number'].append(soup.find("div",class_="productstar_Box").find("span").text)
        except:
            info['product number'].append("None")

        try:
            s_price = soup.find("div",class_="product_PRICEBOX").find("span",class_="price_snum").text.replace("$","").replace("\r","").replace("\n","")
            
            if s_price == '' or s_price==None or s_price == " ":
                info['price'].append(soup.find("div",class_="product_PRICEBOX").find("span",class_="price_num").text.replace("$","").replace("\r","").replace("\n",""))
                info['suggested price'].append(soup.find("div",class_="product_PRICEBOX").find("span",class_="price_num").text.replace("$","").replace("\r","").replace("\n",""))
                
            else:
                info['price'].append(soup.find("div",class_="product_PRICEBOX").find("span",class_="price_num").text.replace("$","").replace("\r","").replace("\n",""))
                info['suggested price'].append(soup.find("div",class_="product_PRICEBOX").find("span",class_="price_snum").text.replace("$","").replace("\r","").replace("\n",""))
                
        except:
            info['price'].append("None")
            info['suggested price'].append("None")
        try:
            info['sales'].append(soup.find("div",class_="bonus_mbox").find('a').text)
        except:
            info['sales'].append("None")




        try:
            category = soup.find("div",class_="navigation").find_all("li")
            cg = ""
            for cate in category:
                cg+=cate.text
            cate = cg.split(">")
            try:
                info['category 1'].append(cate[0])
            except:
                info['category 1'].append("None")
            try:
                info['category 2'].append(cate[1])
            except:
                info['category 2'].append("None")
            try:
                info['category 3'].append(cate[2])
            except:
                info['category 3'].append("None")
            try:
                info['category 4'].append(cate[3])
            except:
                info['category 4'].append("None")
            try:
                info['category 5'].append(cate[4])
            except:
                info['category 5'].append("None")
        except:
            info['category 1'].append("None")
            info['category 2'].append("None")
            info['category 3'].append("None")
            info['category 4'].append("None")
            info['category 5'].append("None")

        
        
        try:
            spec = soup.find("table",class_="title_word").text
            spec = spec.replace("\r","")
            spec = spec.replace("\n","")
            spec = spec.replace("\xa0","")
            spec = spec.replace("\t","")
            spec = spec.split(" ")
            k=0
            for i in spec:
                if "商品規格" in i:
                    pass
                elif "規格" in i:
                    k+=1
                    i = i.replace("規格","").replace(":","")
                    info['specification'].append(i)
                else:
                    pass
            if k ==0:
                info['specification'].append("None")
            
            '''
            if soup.find("table",class_="title_word").find("select",class_="for_input"):
                spec = soup.find("table",class_="title_word").find_all("td")[2].text
                spec = spec.replace("\r","")
                spec = spec.replace("\n","")
                spec = spec.replace("\xa0","")
                spec = spec.replace("\t","")
                spec = spec.split(" ")
                k=0
                
                for i in spec:
                    if "規格" in i:
                        k+=1
                        i = i.replace("規格","").replace(":","")
                        info['specification'].append(i)
                    else:
                        pass
                if k ==0:
                    info['specification'].append("None")
            elif "商品規格" in soup.find("table",class_="title_word").find_all("td")[0].text:
                spec = soup.find("table",class_="title_word").find_all("td")[1].text
                
                spec = spec.replace("\r","")
                spec = spec.replace("\n","")
                spec = spec.replace("\xa0","")
                spec = spec.replace("\t","")
                spec = spec.split(" ")
                k=0
                
                for i in spec:
                    if "規格" in i:
                        k+=1
                        i = i.replace("規格","").replace(":","")
                        info['specification'].append(i)
                    else:
                        pass
                if k ==0:
                    info['specification'].append("None")
            else:    
                spec = soup.find("table",class_="title_word").find_all("td")[0].text
                spec = spec.replace("\r","")
                spec = spec.replace("\n","")
                spec = spec.replace("\xa0","")
                spec = spec.replace("\t","")
                spec = spec.split(" ")
                k=0
                # debudding
                
                for i in spec:
                    if "規格" in i:
                        k+=1
                        i = i.replace("規格","").replace(":","")
                        info['specification'].append(i)
                    else:
                        pass
                if k ==0:
                    info['specification'].append("None")
            '''
        except:
            info['specification'].append("None")
        
        try:
            dspec = soup.find("div",class_="main_indexProbox01").find("div",id="product_content02").text
            dspec = dspec.replace("\r","")
            dspec = dspec.replace("\xa0","")
            dspec = dspec.replace("\t","")
            #ddes = ddes.replace("\n","")
            info['detailed specification'].append(dspec)
        except:
            info['detailed specification'].append("None")



        try:
            des = soup.find("div",class_="main_indexProbox01").find("div",id="product_content01").text
            des = des.replace("\r","")
            des = des.replace("\xa0","")
            des = des.replace("\t","")
            #des = des.replace("\n","")
            info['description'].append(des)
        except:
            info['description'].append("None")
        
   
        return info 

df = debugging("https://www.rt-mart.com.tw/direct/index.php?action=product_detail&prod_no=P0000200128245")
print(df['specification']) 