# Qwant images scraper
## this scrapy bot  allows you to download images from Qwant search engine by providing keywords 

## requirments
- Install scrapy
```
pip install scrapy
```
- Install urllib3
```
pip install urllib3
```
## challenge faced 
some of you at this point might wonder why didn't i use the pipeline object offered by scrapy , i tried  and it didn't work out 
and that's why i resorted to using  urllib3 as an alternative

## how it works
1) first open up  settings.py  located in qwant_script folder and  set ***ROBOTSTXT_OBEY = False***
2) make sure you're on the root directory and fire up the command line
3) run the command 
```
scrapy crawl images
```
4) specificy what you want to search and seperate the keywords by a ***comma*** eg: kanye west,donald trump

 the script will create a folder for each keyword you specify **automatically** 
