import numpy as np
import os, glob
from skimage import io
from os.path import expanduser
from PIL import Image, ImageDraw
import xmltodict

dataset_path = ('{}/datasets/Tobacco800').format(expanduser("../.."))
files_color = glob.glob(("{}/Tobacco800_SinglePageTIF/onlysign/*.tif").format(dataset_path))
mask_dir = ("{}/Tobacco800_SinglePageTIF/mask/").format(dataset_path)

# this is the functional part
def patch_save(pfile, tag):
	# print ('file {}').format(file)
	maxval = 0
	image = Image.open(pfile)
	base_name = os.path.basename(pfile)
	stride = 50  # sum must be stride*stride-2*stride+1

	X = int(tag['@col'])
	Y = int(tag['@row'])
	W = int(tag['@width'])
	H = int(tag['@height'])

	# write login to move the window with proper stride
	for i in range(0, image.size[0], stride):
		for j in range(0, image.size[1], stride):
			box = image.crop((i, j, i + stride, j + stride))

			#II = II + 0
			x = i
			y = j
			w = stride
			h = stride
			#print ('x:{} y:{}, X:{}, Y:{}').format(x, y, X, Y)

			name = ('{}_50-50_i{}_j{}.png').format(base_name, i, j)
			data = np.asarray(box)
			numpy_sum = np.sum(np.sum(data, axis=0), axis=0)

			if numpy_sum < stride*stride and w <= W and h <= H:
				# call_occupancy_check(i,j,stride,stride, TAG); x-mask = rectangle, X-patch = rectangle window
				if (x >= X and (y + h/2 >= Y or y < Y - h/2)) or (y >= Y and (x + w/2 >= X or x < X - w/2)):
					name = ("{}/Tobacco800_SinglePageTIF/patches/positive/{}").format(dataset_path, name)
					#print ('POSITIVE {}').format(name)
					box.save(name, "PNG")
				else:
					pass	#name = ("{}/Tobacco800_SinglePageTIF/patches/negative/{}").format(dataset_path, name)

			elif numpy_sum == stride*stride and (w > W or h > H):
				print 'patches ST mask size\n'
			# if maxval < numpy_sum:
			# 	maxval = numpy_sum
			break
		# 	print II
		# 	if II == 1000:
		# 		break
		# if II == 1000:
		# 	break

def printDetails(filename, tag):
	filename = os.path.splitext(os.path.basename(filename))[0]
	filename = ('{}/Tobacco800_SinglePageTIF/onlysign/{}.tif').format(dataset_path, filename)
	# sanity test
	if not os.path.exists(filename):
		print ('file {} NOT present').format(filename)
	#print ('filename {}').format(filename)
	patch_save(filename, tag)

files = glob.glob(("{}/Tobacco800_Groundtruth_v2.0/XMLGroundtruth_v2.0/*.xml").format(dataset_path))
for file1 in files:
	# print(('\nProcessing file : {}').format(file1))
	with open(file1) as fd:
		doc = xmltodict.parse(fd.read())
		try:
			TAG = doc['GEDI']['DL_DOCUMENT']['DL_PAGE']['DL_ZONE']
			try:
				if TAG[ 0]['@gedi_type'] == 'DLSignature':
					printDetails(file1, TAG[0])
				elif TAG[1]['@gedi_type'] == 'DLSignature':
					printDetails(file1, TAG[1])
				#else:
					#print (('TRY :: file {} skipped').format(file1))
			except:
				if TAG['@gedi_type'] == 'DLSignature':
					printDetails(file1, TAG)
				#else:
					#print (('EXCEPT : file {} skipped').format(file1))
		except:
			#print (('No DLZone for {}').format(file1))
			continue
