# 24-1_DSL_Modeling_A-uto-ssignment
24-1_DSL_Modeling_A(uto)ssignment

## 주제
* 사용자가 원하는 번호만을 추출하여 하나의 문제집으로 제작

### Team 유현동 정성오 김현동 고현아
---
# Overview
[[발표 자료](/24-1_Modeling_CV_A(uto)ssignment.pdf)]

## Purpose
두꺼운 전공 교재의 페이지를 넘기면서 문제를 찾고, 이를 메모장에 일일이 옮기는 작업을 자동화해주기 위함이다. 

## Overall Pipeline 
---
![Example Image](/images/pipeline.png)

* Question을 식별하기 위한 YOLOv7
* Question num을 인식하기 위한 PORORO

---

## Model
---
### 1) PDF to image
---
* 'fitz': 이 모듈은 PyMuPDF 라이브러리의 일부로, PDF 파일을 다루기 위해 사용됩니다.
* 역할 : 교재 pdf를 input으로 받으면, 각 페이지를 image로 변환 
* Installation and run : 'pdf_to_image.py'

### 2) YOLOv7

![슬라이드11](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/6c6b9b56-68f6-44b4-a228-a8c6343cd55a)

"You Only Look Once" 시리즈의 최신 버전 중 하나로, 실시간 객체 탐지를 위한 딥러닝 모델이다. YOLO v7 말고 v6, v8도 사용했는데, bounding box 정확성 수치와 최종 결과가 v7이 가장 정확하게 나와 채택했습니다. 

[YOLOv7 paper](https://arxiv.org/abs/2207.02696)

* Roboflow를 통해 Image Segmentation이 완료된 훈련 데이터를 입력으로 받아, YOLOv7 fine-tuning 진행
* 이후 입력된 이미지에서 'question' 부분을 탐지하고 해당 부분을 crop하여 이미지로 저장

#### Result 
---
![슬라이드12](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/c777eadb-cfb7-4e53-b83f-59f013593c7a)


### 3) PORORO ; Optical Character Recognition 

![슬라이드14](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/f435adeb-ab25-4260-b598-54a24b453e01)

* YOLOv7 모델을 통해 추출된 문제 이미지에서 문제 번호를 정확하게 식별하고, 이를 파일명으로 사용하여 이미지를 저장하기 위해 사용

## Dataset
---
* Introduction to Mathematical Statistics PDF

## Final Result
---
### User Interaction
---
![슬라이드22](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/503dd946-90f8-48be-bdd1-3ffdf1f77b42)

![슬라이드23](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/def194c9-c941-4ed5-82fd-004d5a07ecc7)

![슬라이드24](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/24ab19fe-c35b-439e-87d9-43de6aa7df3d)

### Final Workbook Result
---
![슬라이드25](https://github.com/DataScience-Lab-Yonsei/24-1_DSL_Modeling_A-uto-ssignment/assets/126374997/648d12d0-94a6-4ad4-99f4-a3f3af30cf11)

## File Description
---
* Pdf To Image
    * 'pdf_to_image.py'
* YOLOv7
    * 'yolov7x.pt' : pretrained parameter for Yolov7-X model
    * 'YOLOv7_fine_tuned_params.pt' :pretrained parameter by a textbook (Introduction to Mathemtical Statistics)
* PORORO
    * 'pororo_implementation.py' : OCR model
* User Interaction
    * 위의 전체 모델을 연결하여 최종 결과를 도출해내는 py 파일
