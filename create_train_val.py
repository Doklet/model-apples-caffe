import numpy as np
import os
 
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
DATASET_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '../../../datasets/apple'))
TXT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, './data'))
print DATASET_DIR
print TXT_DIR

good_dir = os.path.join(DATASET_DIR, 'good')
bad_dir = os.path.join(DATASET_DIR, 'bad')
print good_dir

good_images = [image for image in os.listdir(good_dir)]
bad_images = [image for image in os.listdir(bad_dir)]
print 'good images'
print good_images
print 'bad images'
print bad_images
 
good_train = good_images[:int(len(good_images)*0.7)]
good_test = good_images[int(len(good_images)*0.7):]
 
bad_train = bad_images[:int(len(bad_images)*0.7)]
bad_test = bad_images[int(len(bad_images)*0.7):]
 
with open('{}/train.txt'.format(TXT_DIR), 'w') as f:
    for image in good_train:
        f.write('{} 0\n'.format(image))
    for image in bad_train:
        f.write('{} 1\n'.format(image))
    f.close()
 
with open('{}/val.txt'.format(TXT_DIR), 'w') as f:
    for image in good_test:
        f.write('{} 0\n'.format(image))
    for image in bad_test:
        f.write('{} 1\n'.format(image))
    f.close()