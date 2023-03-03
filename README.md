# Manga-Manhua-Manga_Downloader

## Introduction
This Project is made for weebs for downloading all types of mangas/manhua and manhwas without opening any browser and with cmdline. This will be able to download most of the mangas, but some mangas like Dragon ball and one piece are unavailable.

## Installation 
1. Clone this repository by using ``` git clone https://github.com/Hatim315/Manhua-Manga-Manhwa_Downloader```<br>
2. Run ```source bin/activate```
2. Run ```pip install -r requirements.txt ```<br>
3. Enjoy!!<br>

## Usage
First of all, activate the virtual environment with ```source bin/activate```.
After that, there are two ways of using this script:

### 1. With Cmdline arguments
    You can use arguments to pass different parameters. For example,
   If you run ```python main.py -h ```. You will get all the available arguments. These are:
   
   usage: main.py [-h] [-n N] [-l L] [-t T] [-N]
   
   optional arguments:
    -h, --help  show this help message and exit.
    -n N        Name of the manga/manhua/manhwa you want to download.
    -l L        Number of latest chapters you want.
    -t T        To set time interval between each pdf getting created acording to your internet speed.
    -N          For not deleting the Images even after making pdfs.```
    ```
   
    
    Complete Execution: ```python main.py -n <name of the manga/manhua/manhwa> -l <no. of latest chapters you want> -t <time taken after each pdf> -N (This flag can be used to keep the images.)```

### 2. With Direct Input 
    
    You can just directly run ```python main.py ```,and it will ask all the above parameters as user input except for -N. 
    ```
    1. Give the name of the manga/manhua/manhwa you want to download--> <name of the manga/manhua/manhwa>
    2. How many latest Chapters do you want? If you want to download all chapters then write 0 --> <no. of latest chapters you want>
    3. Give the time(in seconds) to wait while making each pdf according to your internet speed 'recommended 5 for medium speed internet'--> <time taken after each pdf>
    
    ```
## Errors and Contribution
   If you face any kind of error, you can raise the issue. If you have any more ideas then feel free to contribute to this project.
   







