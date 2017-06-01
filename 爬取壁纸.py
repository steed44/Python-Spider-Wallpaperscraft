import requests
from bs4 import BeautifulSoup
import os

root = 'H://pic//'
'''
url = "https://wallpaperscraft.com/image/multicolored_grid_abstraction_115586_2560x1080.jpg"
root = 'H://pic//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
    else:
        print("文件已经存在")
except:
    print("爬取失败")

'''
'''try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
    
demo = r.text
demo'''


#获取页面内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#解析页面,提取图片地址
#def parsePage(ilt, html):
def parsePage(html):
    #url = "https://wallpaperscraft.com/all/2560x1080"
    #html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    #ilt = soup.find_all(class_="wallpaper_pre")
    ilt = soup.find_all(class_="preview_size")
    picSoup = BeautifulSoup(str(ilt),'html.parser')
    for link in picSoup.find_all('a'):
        print(link.get('href'))
        parseDownAdd(link.get('href'))
    

#解析子页，提取高清图片下载地址
def parseDownAdd(preHtml):
    url = 'https:'+ preHtml
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    ilt = soup.find_all(id="downloads_big")
    picSoup = BeautifulSoup(str(ilt),'html.parser')
    for link in picSoup.find_all('img'):
        downPic('https:' + link.get('src'),root)


#下载图片并保存到本地
def downPic(picURL,root):
    path = root + picURL.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(picURL)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
        else:
            print("文件已经存在")
    except:
        print("爬取失败")


#主函数
def main():
    start_url = "https://wallpaperscraft.com/all/2560x1080"
    depth = 3
    infoList = []
    for i in range(depth):
       try:
           if i+1 == 1:
               html = getHTMLText(start_url)
           else:
               url = start_url + '/page' + str(i+1)
               print(url)
               html = getHTMLText(url)
               
           parsePage(html)
       except:
            continue

main()
#parsePage()
    
