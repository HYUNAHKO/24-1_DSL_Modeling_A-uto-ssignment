import os
import re
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

from PIL import Image
from pororo import Pororo

ocr = Pororo(task='ocr', lang='en')

# checking names of cropped images(questions) and the numebr of images
# img_folder_path : 'YOLO_Implementation.py'를 통해 crop된 이미지가 저장된 경로를 입력해주세요.
def check_cropped_images(img_folder_path):
    os.chdir(img_folder_path)
    files = os.listdir(img_folder_path)
    img_files = [file for file in files if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg')]
    length_cropped_images = len(img_files)

    return img_files, length_cropped_images

def extracting_question_number(img_files):
    extracted_problem_num_list = []
    index = 0

    while index < len(img_files):
        img_path = img_files[index]
        result = ocr(img_path)
        if result:
            extracted_problem_num_list.append(result[0])
        index += 1

    extracted_versions = []
    for i, text in enumerate(extracted_problem_num_list):
        try:
            question_num = re.match(r'(\d+\.\d+\.\d+)', text).group()
            extracted_versions.append(question_num)
        except:
            extracted_versions.append('NULL')
            continue

    return extracted_versions

# crop된 이미지 이름을 문제 번호로 바꿔서 다시 저장
# target_dir : crop된 이미지들을 이름을 바꿔서 다시 저장할 폴더를 지정해주세요.
def change_image_name(target_dir, extracted_versions):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for png_file_name, new_name in zip(png_files, extracted_versions):
        if new_name != 'NULL':
            img = mpimg.imread(os.path.join(img_folder_path, png_file_name))
            mpimg.imsave(os.path.join(target_dir, new_name)+".png", img)

# 각각의 문제 이미지에 여백을 생성합니다.
# target_dir을 동일하게 설정하면 기존 이미지 위에 덮어씌워집니다.

def make_space(target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for png_file_name, new_name in zip(png_files, extracted_versions):
        img_path = os.path.join(img_folder_path, png_file_name)
        img = Image.open(img_path)
        width, height = img.width, img.height

        # Create a new image with white background
        merged_image = Image.new('RGB', (int(width * 1.1), int((width * 1.1) * 1.414)), color='white')
        merged_image.paste(img, (int((width * 1.1) / 2) - int(width / 2), int(height * 0.1)))

        # Save the image with the new name
        new_image_path = os.path.join(target_dir, new_name + ".png")
        merged_image.save(new_image_path)

        print(f"Image saved: {new_image_path}")