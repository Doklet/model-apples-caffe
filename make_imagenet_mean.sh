#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in db/train_lmdb

EXAMPLE=examples/apples
OUT=examples/apples/data
DATA=examples/apples/db/train_lmdb
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/db/train_lmdb \
  $OUT/mean.binaryproto

echo "Done."
