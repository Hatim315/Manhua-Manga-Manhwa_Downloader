import requests
import os,asyncio,aiohttp,aiofiles
from bs4 import BeautifulSoup as bs

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

async def get_image(s,url,x,Dir):
    """For Downloading every image"""
    async with s.get(url) as r:
        if r.status==200:
            f= await aiofiles.open(f'{Dir}/Image{x}',mode="wb")
            await f.write(await r.read())
            await f.close()

async def get_all(session,urls,Dir):
    """for using all urls at once"""
    tasks=[]
    x=0 #Here x is used for numbering all the images.
    for i in urls:
        task=asyncio.create_task(get_image(session,i,x,Dir))
        tasks.append(task)
        x+=1
    await asyncio.gather(*tasks)
    


async def main_get_images(Dir,url):
    """for making directory and for starting aiohttp session. This Function is a root function"""
    if not os.path.exists(Dir):
       os.mkdir(Dir)
    urls=get_imgurls(url)
    async with aiohttp.ClientSession() as session:
        await get_all(session,urls,Dir)
        






    
