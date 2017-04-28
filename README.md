# Train apples model for caffe

Repo to train a caffe model on the apple dataset.

Clone this repo into the CAFFE_ROOT/examples folder

Download the apple dataset to the following relative path "../../../datasets/apple" (should be on the same level as caffe dir)

Run `make copy_dataset` to copy the images to data/images dir 

Run `make create_train_val to create the data/train.txt and data/val.txt file's containing the path to the image and the label.

Run `make create_imagenet` to create the db for train and val, will be places in the ./db folder

Run `make create_mean` to create the mean.binaryproto

Run `make train` to train the model will be output to ./models/alexnet/caffe_alexnet_train_iter_1000.caffemodel