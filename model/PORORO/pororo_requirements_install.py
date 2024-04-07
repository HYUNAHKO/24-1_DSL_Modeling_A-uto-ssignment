# 처음에 한번만 실행
!git clone https://github.com/yunwoong7/korean_ocr_using_pororo # PORORO OCR을 사용하기 위한 레퍼지토리 clone

!pip install pillow

import os

print('현재 작업 경로 :', os.getcwd())
os.chdir('korean_ocr_using_pororo로 작업경로를 변경해 주세요.')
print('변경된 작업 경로 :', os.getcwd())