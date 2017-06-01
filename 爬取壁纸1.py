import requests
from bs4 import BeautifulSoup
import os


'''该程序可以爬取https://wallpaperscraft.com/all的类型为“all”的壁纸，用户可以在下面更改一些
自己需要的设置'''


root = 'H://pic//'      #设置图片保存位置（如需更改，要按固定格式）
starPage = 47            #设置爬取起始页（首页是1）
endPage = 70             #设置爬取终止页（最终页可以到网站查看）
resolutio = "2560x1080" #设置你需要的分辨率（注意乘号‘x’的格式），要保证分辨率是壁纸网站所用有的
kv = {'user-agent':'Mozilla/5.0'}  #设置模拟的浏览器

#获取页面内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 300,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("内容获取错误")
        return ""

#解析页面,提取图片地址
def parsePage(html):
    soup = BeautifulSoup(html,'html.parser')
    ilt = soup.find_all('a',target="_blanck")
    #print(ilt[2])
    for i in range(1,21):
        #print(ilt[i].get('href'))
        parseDownAdd(ilt[i].get('href'))
    

#解析子页，提取高清图片下载地址  
def parseDownAdd(preHtml):
    url = 'https:'+ preHtml
    html = getHTMLText(url)
    soup = BeautifulSoup(html,'html.parser')
    ilt = soup.find_all('img',style="max-width: 728px;max-height: 602px;")
    print(ilt[0].get('src'))
    downPic('https:' + ilt[0].get('src'),root)


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
    start_url = "https://wallpaperscraft.com/all/" + resolutio
    for i in range(starPage,endPage+1):
       try:
           if i == 1:
               html = getHTMLText(start_url)
           else:
               url = start_url + '/page' + str(i)
               print(url)
               html = getHTMLText(url)
               
           parsePage(html)
       except:
            continue

main()

    
