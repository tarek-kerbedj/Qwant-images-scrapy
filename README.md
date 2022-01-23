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
some of you at this point might wonder why didn't i use the pipeline object offered by scrapy , i tried doing that and it didn't work out 
and that's why i resorted to using multithreading with urllib3
