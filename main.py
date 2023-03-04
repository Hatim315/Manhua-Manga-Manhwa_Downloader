import requests,re
import shutil,os,asyncio
from utils.ImagesGetter import get_imgurls,main_Get_Images
from bs4 import BeautifulSoup as bs
from utils.ImgToPdf import PdfMaker
import time
import argparse
parser=argparse.ArgumentParser(description="Flags to use with this script.")
parser.add_argument("-n",metavar='',help="Name of the manga/manhua/manhwa you want to download.")
parser.add_argument("-l",metavar='',help="Number of latest chapters you want.")
parser.add_argument("-N",help="For keeping the Images even after making pdfs",action="store_true")
args=parser.parse_args()
def Mreader_search_manga(Name):
    """This function will find your manga,manhua or manhwa in Mreader's Website"""
    name=Name.replace(' ','+')   
    search_url="https://www.mreader.co/search/?search={}".format(name)
    res=requests.get(search_url)
    soup=bs(res.text,"html.parser")
    results=soup.find_all("a",href=True)
    return results[39]["href"]

def cleaner(FilePath):
    """This Function will clean the mess(images,directories)"""
    for file in os.listdir(FilePath):
        os.remove(f"{FilePath}/{file}")
    os.rmdir(FilePath)

def Mreader_main(Name,Chapwant=None,Delete=None):
      """This function will make pdf of your inputted manga, manhua or manhwa """
      IntFinder=re.compile("(\-\d+){1,4}")
      Searched=Mreader_search_manga(Name)
      Common="https://www.mreader.co"
      name=Name.replace(' ','-')
      Main_Url=f"{Common}/{Searched}/all-chapters"
      Get_Chapters=requests.get(Main_Url)
      Words=re.sub(r'[^\w\s]',' ',Name).split(" ")     
      if Get_Chapters.status_code==404:
          print("Query not Found.\nEither Manga,Manhua or Manhwa you're looking for is not on Database or there might be a typing error such as,\nOne Punch Man --> Not Correct\nOne-Punch Man --> Correct\nSearch on google to find the correct name.")
          return
      base=bs(Get_Chapters.text,"html.parser")
      Chapters=base.find_all("a",href=True)
      if not  os.path.exists(name):
         os.mkdir(name)      
      os.chdir(name)
      Path=os.getcwd()
      print("Starting...")
      ChapCount=0
      for i in range(6,len(Chapters)):#just removed some links that i do not need by specifying the range
        links=Chapters[i]["href"]
        if Words[0] in links:
            Into=IntFinder.search(links)
            if Into:
               count=Into.group(0)
            else:
               
               count='-'+links.split("-")[-3]
            if ChapCount==Chapwant:
                break
            
            Chapter=f"Chapter{count}"
            print(f"Downloading pages of {Chapter} ...")
        
            asyncio.run(main_Get_Images(Chapter,(Common+Chapters[i]['href'])))
            PdfMaker(f"{Path}/{Chapter}", Path, Chapter)
            if Delete==None:
               cleaner(f"{Path}/{Chapter}")
            ChapCount+=1
        
      print("Done!!!")

if __name__=="__main__":
   Delete=None
   if args.n:
      Name=args.n
      if args.l:
        Latest=int(args.l)
      else:
        Latest=None
      if args.N:
        Delete=args.N
         
      
   else:
        Name=input("Give the name of the manga/manhua/manhwa you want to download--> ").lower()
        latest=int(input("How many latest Chapters do you want? If you want to download all chapters then write 0 --> "))
        if latest==0:
            Latest=None
        else:
            Latest=latest
    
   Mreader_main(Name,Chapwant=Latest,Delete=Delete)
   
