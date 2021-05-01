#!/usr/bin/env bash

DATA=/mnt/data/many-to-eng/data/MT/experiments/mdhUV-mdhUBT

tokenize(){
    sacremoses normalize -q -d -p -c tokenize -a -x
}

for split in train val test ; do
    for side in src trg ; do
	[[ -f $DATA/$split.$side.tok ]] || tokenize < $DATA/$split.$side.txt > $DATA/$split.$side.tok
    done
done
