# WellscanRenewal
modified version of Wellscan from Taejoonlab
Scripts to analyze 96/386 well plate images from flatbed scanner.

###image processing: file속 이미지 파일 위치 주소는 변경 바람.

## 0.reduce file size

사이즈를 줄인 후 저장할 폴더를 미리 생성하거나 생성하는 코드를 추가해야함.

#$ python3 reduce_filesize.py


## 1. crop#$ bash crop-1x2.sh

원본 이미지의 플레이트 수에 따라 다른 파일 선택 가능. x1, y1, y2, width, height는 샘플에 따라 다를 수 있으니 조정 필요. (raw-to-plate.py는 주석을 달아놓은 것임. 원본은 origin이 붙어있음)

## PLATE별로 폴더를 분리.

$mkdir plate1 plate2

$mv [filename]P8*.jpg plate1

$mv [filename]P10*.jpg plate2

## 2. plate to well#$ plate-to-96well_jpeg.sh

tif file인 경우 jpeg 없는 것 쓰면 됨. 

json.2400이 적힌 파일에서 세부사항 수정. (width, height, x1, rotation 등 상황에 맞게 조정 필요)

## 3. make movie

#$ make-movie-all.sh

만약 명령 프롬프트에서 돌아가는 게 너무 오래 걸린다면 nohup과 &을 쓰면 됨. background에서 명령을 실행해 터미널을 종료해도 프로그램이 돌아감.

#ex: nohup bash crop-1x2.sh &
