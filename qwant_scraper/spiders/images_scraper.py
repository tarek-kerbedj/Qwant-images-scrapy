import scrapy
from concurrent.futures import ThreadPoolExecutor
from urllib3 import PoolManager
import time
from os import makedirs
from os.path import isdir,join
https = PoolManager(num_pools=150)
class QwantSpider(scrapy.Spider):
	
	#the name of the spider
	name = 'images'	
	#specify keywords to look up
	query = input('choose something to look up ...\n').split(',')
	start_urls=[]
	#this loop generates Qwant queries from our keywords
	qwant_url='https://www.qwant.com/?l=en&q='
	for q in query:
		search_URL=''.join([qwant_url,q,'+-gif&t=images'])
		start_urls.append(search_URL)

	# to generate folder names
	folder_name_gen=(name for name in query)
	# to generate names of the files during the download , since i won't be using a for loop
	# additional info: Qwant only provides 50 image results per query
	gen=(i for i in range(len(start_urls)*50))
	def parse(self,response):
		# creating our folder to store the images
		folder_name=next(self.folder_name_gen)
		if not isdir(folder_name):
		#if the folder doesnt exist , create one
			makedirs(folder_name)
		#scraping the image urls
		raw_image_urls=response.css('img::attr(src)').getall()
	

		def download_image(url):
			# it's best to add a time.sleep() in order not to spam the servers
			response_html=https.request('GET', url) 
			if response_html.status==200:
				with open(join(folder_name,str(next(self.gen)) +".jpg"), 'wb') as file:
					file.write(response_html.data)
		
		
		#with ThreadPoolExecutor() as executor:
		#	executor.map(download_image,raw_image_urls)
		ls=[download_image(url) for url in raw_image_urls]
	
	
		yield 
		
			
		