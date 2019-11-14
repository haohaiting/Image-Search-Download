"""
Action-Effect Dataset Generation (Bing)
@author: haohaiting

Search term is 'verb-noun pairs+effect_phrase_1+effect_phrase_2 ...'
Directlry name is 'verb-noun pairs+effect_sentence'
Each folder contains image url lists and corresponding images

ref:
	keywords and code - What Action Causes This? \
		Towards Naive Physical Action-Effect Prediction
	code - Bing Image Search SDK for Python

!!! NOTICE:
	The subscription_key is personal.
"""


from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials
import urllib.request as urllib2
import shutil
import imghdr
import os
import sys


# Personal key
subscription_key = "BING_SEARCH_V7_SUBSCRIPTION_KEY"

target_types = ['jpg', 'jpeg', 'png', 'bmp']

# pass the keywords file path into argument
keywords_file = sys.argv[1]

with open(keywords_file, mode="r") as f0:
	for line in f0:
		print(line)
		if line.split():
			# if use action-cause clauses, uncomment below
		    
			# vn_effect = line.strip().split(", ")
			# search_term = vn_effect[0] + '+' + '+'.join(vn_effect[2:])
			# print(search_term)
			# DIR = "Bing"
			# if not os.path.exists(DIR): os.mkdir(DIR)
			# DIR = os.path.join(DIR, '+'.join(vn_effect[:2]))
			# if not os.path.exists(DIR): os.mkdir(DIR)

			# if each line in the keywords file is a separated search term
			# if use action-cause clauses, comment below

			search_term = line.strip()
			DIR = "Bing"
			if not os.path.exists(DIR): os.mkdir(DIR)
			DIR = os.path.join(DIR, search_term))
			if not os.path.exists(DIR): os.mkdir(DIR)

			# initialize 
			client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
			# search the first 100 results
			image_results = client.images.search(query=search_term, count=100)
            
            		# if the result is not null
			if image_results.value:
			    	# open a file to record the original url of those image
				writer = open(DIR + '/url_list.txt','w+')
				count = 0
				# for each image in the search result
				for _ in image_results.value:
					image_link = _.content_url
					try:
					    	# read the raw image and store them from index 000
						raw_img = urllib2.urlopen(image_link, timeout=2).read()
						file_name = str('%03d'%count)
						file_path = os.path.join(DIR, file_name)
						with open(file_path, 'wb') as f:
							f.write(raw_img)
							
						# check file type
						file_type = imghdr.what(file_path)
						# if file type is the required format
						if file_type is not None and file_type in target_types:
						    	# save to required directory
							new_file_name = "{}.{}".format(file_name, file_type)
							new_file_path = os.path.join(DIR, new_file_name)
							shutil.move(file_path, new_file_path)
							# record the url in txt file
							writer.write(image_link)
							writer.write('\n')
							# print the status
							print("## OK:  {}".format(file_path))
							count += 1
						else:
						    	# otherwise remove it
							os.remove(file_path)
							# print the status
							print("## Err:  {}".format(file_path))
					except Exception as e:                          # handle exception
						print("could not load : " + image_link)
						print(e)
			else:
			    print("No image results returned!")
