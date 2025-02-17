#!/bin/bash

#export PYTHONPATH="/home1/00992/linusben/local/lib64/python2.6/site-packages/"

for JPG in $(ls *.jpg)
do
  echo $JPG
  OUT=${JPG/.jpg/.grid.jpg}
  if [ ! -e $OUT ]; then
    $HOME/git/wellscan/plate-to-well.py $JPG 96
  else
    echo "SKIP "$JPG
  fi
done
