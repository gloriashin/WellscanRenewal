#!/bin/bash
FPS=10
i=1

DATA_NAME=$(basename "$(dirname "$PWD")")
echo "$DATA_NAME"
WELL_ADDRESS=$(basename "$PWD")
MOVIE_NAME="${DATA_NAME}.${WELL_ADDRESS}.avi"

if [ -e "$MOVIE_NAME" ]; then
  echo "$MOVIE_NAME exists. Skip."
else
  rm -rf tmp
  mkdir tmp

  for TIF in *.{tif,jpg}
  do
    TMP=$(printf "tmp/image%03d.bmp" $i)
    echo "$TIF --> $TMP"
    convert "$TIF" label:"$DATA_NAME" -gravity Center -append -resize 505x510! "$TMP"
    i=$((i + 1))
  done

  mencoder "mf://tmp/*.bmp" -mf fps=$FPS:w=505:h=510 -o "$MOVIE_NAME" -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell:vbitrate=1000
  rm -rf tmp
fi