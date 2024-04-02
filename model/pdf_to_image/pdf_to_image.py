import fitz
import os
import argparse

parser = argparse.ArgumentParser(description='본인의 교재 PDF를 PNG로 저장해주는 프로그램입니다.')
parser.add_argument('--import_path', help='PDF 교재가 담긴 경로')
parser.add_argument('--target_path', help='PNG로 바뀐 경로')

args = parser.parse_args()

import_path = args.import_path
target_path = args.target_path

doc = fitz.open(import_path)

if not os.path.exists(target_path):
    os.makedirs(target_path)

for i, page in enumerate(doc):
    img = page.get_pixmap()
    output_path = os.path.join(target_path, f"page_{i+1}.png")
    img.save(output_path, 'PNG')