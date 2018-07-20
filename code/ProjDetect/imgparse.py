import xmltodict
import glob
import os
import shutil
from PIL import Image, ImageDraw
from os.path import expanduser

# 1. clone project.git in HOME dir
# 2. Enjoy :)

home = expanduser("~")		#'~' refers home, change it to 'dataset_path' with 'expanduser'
dataset_path = ('{}/project/datasets/Tobacco800').format(home) 	#home = Only a Folder that has the path after braces.

def printDetails(filename,TAG):
	filename = os.path.basename( filename )
	print('X:{} Y:{} width:{} height:{}'.format(TAG['@col'], TAG['@row'], TAG['@width'], TAG['@height']))

	# 1. extract name befor dot from filename
	name = os.path.splitext(filename)[0] + '.tif'
	print name
	# 2. create full path to .tif file
	fpath =('{}/Tobacco800_SinglePageTIF/logosign/{}').format(dataset_path, name)	
	destpath = ('{}/Tobacco800_SinglePageTIF/onlysign/{}').format(dataset_path, name)
	shutil.copy(fpath, destpath)	
	# 3. load image
	im = Image.open(fpath)
	print im.size
	# 4. create img var
	mask = Image.new('1', im.size, 'black')
	
	# 5. Use TAG[@col], TAG[@row], TAG[@width], TAG[@height] and mask var to set signature box to 255
	draw = ImageDraw.Draw(mask)	
	draw.rectangle([int(TAG['@col']), int(TAG['@row']), int(TAG['@col'])+int(TAG['@width']), int(TAG['@row'])+int(TAG['@height'])], fill=1, outline=None)

	del draw
	#print type(int(TAG['@col']))
	fmask =('{}/Tobacco800_SinglePageTIF/mask/{}.png').format(dataset_path, os.path.splitext(name)[0])	
	mask.save(fmask, "PNG")
	#os._exit(0)	

files = glob.glob(("{}/Tobacco800_Groundtruth_v2.0/XMLGroundtruth_v2.0/*.xml").format(dataset_path))	#glob.glob - globbing Linux style(wildcards)
for file1 in files:
	print ('\nProcessing file : {}').format(os.path.basename(file1))
	with open(file1) as fd:
		doc = xmltodict.parse(fd.read())	 #Read xml converted to dict.(save as doc)
		try:
			TAG = doc['GEDI']['DL_DOCUMENT']['DL_PAGE']['DL_ZONE']      #doc has 4 indices/tags(index)
			try:
				if TAG[0]['@gedi_type'] == 'DLSignature':		
					printDetails(file1, TAG[0])	#check TAG[0]
				elif TAG[1]['@gedi_type'] == 'DLSignature':
					printDetails(file1, TAG[1]); 	#check TAG[1] and call printDetails() Fn
				else:
					print ('TRY :: file {} skipped').format(os.path.basename(file1))
			except:
				if TAG['@gedi_type'] == 'DLSignature': 		#check any other tag/index that matches signature 
					printDetails(file1, TAG)
				else:
					print ('EXCEPT : file {} skipped').format(os.path.basename(file1))		
		except:								#files with no indices 
			print ('No DLZone for {}').format(os.path.basename(file1))
			continue
