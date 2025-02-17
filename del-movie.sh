#!/bin/bash
FPS=10
i=1

DATA_NAME=$(basename "$(dirname "$PWD")")

WELL_ADDRESS=$(basename "$PWD")
MOVIE_NAME=$DATA_NAME"."$WELL_ADDRESS".avi"

if [ -e $MOVIE_NAME ]; then
  rm $MOVIE_NAME 

