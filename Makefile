DATASET_DIR = ../../../datasets/apple
DATA_DIR = ./data
DATA_IMAGE_DIR = ./data/images

copy_dataset:
	rm -rf $(DATA_IMAGE_DIR);
	mkdir $(DATA_IMAGE_DIR);
	# copy good apples
	cp -r $(DATASET_DIR)/good/* $(DATA_IMAGE_DIR);
	# copy bad apples
	cp -r $(DATASET_DIR)/bad/* $(DATA_IMAGE_DIR);

create_train_val:
	-rm $(DATA_DIR)/*.txt
	python create_train_val.py

create_imagenet:
	rm -rf db/*
	cd ../../;./examples/apples/create_imagenet.sh

create_mean:
	cd ../../;./examples/apples/make_imagenet_mean.sh

train:
	cd ../../;./build/tools/caffe train --solver=examples/apples/models/alexnet/solver.prototxt --weights models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel -gpu 0