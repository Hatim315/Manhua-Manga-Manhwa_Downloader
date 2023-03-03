import requests,shutil
import os
from bs4 import BeautifulSoup as bs
from threading import Thread
from multiprocessing import cpu_count
def get_imgurls(Url):
    """This function will get all the urls of images available on a Chapter Page"""
    Content=requests.get(Url).text
    soup=bs(Content,"html.parser")
    UrlList=[]
    for i in soup.find_all("img"):
       img_url=i["src"]
       if "https" in img_url:
          NewUrl=img_url.replace("https","http")
          UrlList.append(NewUrl)
    return UrlList

def Get_images(Dir,Url):
    """This function will download each and every image available on the Chapter page"""
    Manga_Urls=get_imgurls(Url)
    if not os.path.exists(Dir):
       os.mkdir(Dir)
    i=0
    Cpu=cpu_count()//2 #just to use half of threads
    Length=len(Manga_Urls)
    Remained=Length%Cpu  
    Diff=Length-Remained #Diff is used to make it easy for us to use threads 
    #I am new to threading but anyways I have used it to increase our downloading speed of images 
    while i!=Diff:
        thread1=Thread(target=Image_maker,args=(Dir,i,Manga_Urls[i]))
        thread2=Thread(target=Image_maker,args=(Dir,i+1,Manga_Urls[i+1]))
        if Cpu<4: 
            thread1.start()
            thread2.start()
            i+=2
            continue
        thread3=Thread(target=Image_maker,args=(Dir,i+2,Manga_Urls[i+2]))
        thread4=Thread(target=Image_maker,args=(Dir,i+3,Manga_Urls[i+3]))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        i+=4
    if Remained!=0:
        for j in range(i,Length):
            Image_maker(Dir, j,Manga_Urls[j])


def Image_maker(Dir,x,i):
    """This function will write bytes on Image file"""
    Name=f"{Dir}/Image{x}"
    Get_images=requests.get(i,stream=True)
    if Get_images.status_code==200:
        with open(Name,"wb") as f:
            Get_images.raw.decode_content=True
            shutil.copyfileobj(Get_images.raw, f)

