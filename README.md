# Manga-Manhua-Manhwa_Downloader

## Introduction
This Project is made for weebs for downloading all types of mangas/manhua and manhwas without opening any browser and with cmdline. This will be able to download most of the mangas, but some mangas like Dragon ball and one piece are unavailable.
## Availability
   1. Manhuas- Almost all the manhuas are available.<br>
   2. Manhwas- All popular ones (like Solo Levelling) and most of others are available.<br>
   3. Mangas-  Available except for the ones which easily get copyrights like One piece, Dragon Ball and Attack on titan".<br>

I know that there are a lot of shortcomings in this script but in future I will add as many features and as many websites as possible, so that there will never be any unavailable manga,manhua or manhwa in this project.

## Installation 
1. Clone this repository by using ``` git clone https://github.com/Hatim315/Manhua-Manga-Manhwa_Downloader```<br>
2. Run ```source bin/activate```
2. Run ```pip install -r requirements.txt```<br>
3. Enjoy!!<br>
#### Important Message
    This script is sensitive to name such as,
    If you search One Punch Man, then you will get an error.
    Because the real name is One-Punch Man.
       One Punch Man --> Incorrect
       One-Punch Man --> Correct
## Usage
First of all, activate the virtual environment with ```source bin/activate```.
After that, there are two ways of using this script:

### 1. With Cmdline arguments
    You can use arguments to pass different parameters. For example,
    If you run ```python main.py -h```. You will get all the available arguments. These are:
    ```
    -h, --help  show this help message and exit.
    -n N        Name of the manga/manhua/manhwa you want to download.
    -l L        Number of latest chapters you want.
    -t T        To set time interval(in secs)(recommended 5secs) between each pdf getting created according to your internet speed.
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
   







