Repo to train a caffe model on the apple dataset.

Clone this repo into the CAFFE_ROOT/examples folder

Download the apple dataset to the following relative path "../../../datasets/apple" (should be on the same level as caffe dir)

Run `make copy_dataset´ to copy the images to data/images dir 

Run `make create_train_val´ to create the data/train.txt and data/val.txt file's containing the path to the image and the label.