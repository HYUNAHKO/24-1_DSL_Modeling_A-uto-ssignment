import re
from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description='원하는 문제번호를 입력해 해당 문제들이 포함된 PDF 파일을 반환받는 프로그램입니다.')
parser.add_argument('--import_path', help='문제 이미지 파일이 담긴 경로')
parser.add_argument('--target_path', help='출력될 PDF 파일이 저장되기를 원하는 경로')

args = parser.parse_args()

import_path = args.import_path
target_path = args.target_path

while True:
    user_input = input("몇 개의 문제가 필요하시나요? ")
    if user_input.isdigit():
        n = int(user_input)
        break
    else:
        print("정수 값을 입력해주세요.")

queries = []

pattern = re.compile(r'^\d+(\.\d+)+\.$')

for i in range(n):
    while True:
        question_number = input("원하는 문제 번호를 입력하세요: ").strip()
        if pattern.match(question_number):
            queries.append(question_number)
            break
        else:
            print("문제 번호 형식이 올바르지 않습니다. 예: 3.10.8. 또는 4.9.10. 형식으로 입력해주세요.")
    print(f"Q{i + 1}: {question_number}")

print("입력받은 문제 번호들:", queries)

image_paths = []

for query in queries:
    img_path = os.path.join(import_path, f"{query}png")
    if not os.path.exists(img_path):
        print(f"문제번호 {query}가 데이터베이스에 존재하지 않습니다.")
    else:
        image_paths.append(img_path)

if image_paths == []:
    print('요청하신 문제들이 데이터베이스에 존재하지 않습니다.')
    quit()

def images_to_pdf(image_paths, output_pdf):
    images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        images.append(image)

    images[0].save(output_pdf, save_all=True, append_images=images[1:])

    for image in images:
        image.close()

def get_unique_filename(output_pdf):
    base_name, ext = os.path.splitext(output_pdf)
    index = 1
    while os.path.exists(output_pdf):
        output_pdf = f"{base_name}_{index}{ext}"
        index += 1
    return output_pdf

if not os.path.exists(target_path):
    os.makedirs(target_path)

output_pdf = get_unique_filename(os.path.join(target_path, "output.pdf"))

images_to_pdf(image_paths, output_pdf)

print("PDF 파일이 생성되었습니다:", output_pdf)
