import os
import shutil

folder = 'Dataset/training'
images = []
labels = []

fileList = os.listdir(folder)
os.mkdir(f'{folder}/train')
os.mkdir(f'{folder}/validate')
for file in fileList:
	fileName = os.path.splitext(file)[0]
	imgExt = os.path.splitext(file)[1]
	if imgExt == '.jpg':
		images.append(file)
		labels.append(f'{fileName}.txt')
data_train_img = images[0:int(len(images)*0.7)]
data_train_labels = labels[0:int(len(labels)*0.7)]

data_validate_img = images[int(len(images)*0.7):int(len(images))]
data_validate_labels = labels[int(len(labels)*0.7):int(len(labels))]

def moveFiles(curLoc,sourceLoc):
	for i in curLoc:
		source = f'{folder}/{i}'
		dest = f'{folder}/{sourceLoc}/{i}'
		shutil.copy(source,dest)
		os.remove(source)

moveFiles(data_train_img,'train')
moveFiles(data_train_labels,'train')

moveFiles(data_validate_img,'validate')
moveFiles(data_validate_labels,'validate')





