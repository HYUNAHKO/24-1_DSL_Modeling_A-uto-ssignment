# 24-1_DSL_Modeling_A-uto-ssignment
24-1_DSL_Modeling_A(uto)ssignment

## 주제
* 사용자가 원하는 번호만을 추출하여 하나의 문제집으로 제작

### Team 유현동 정성오 김현동 고현아
---
# Overview
[[발표 자료](/24-1_Modeling_CV_A(uto)ssignment.pdf)]

## 0. 목적 
두꺼운 전공 교재의 페이지를 넘기면서 문제를 찾고, 이를 메모장에 일일이 옮기는 작업을 자동화해주기 위함이다. 

## 1. Overall Pipeline & Dataset 구축
---
![Example Image](/images/pipeline.png)

* Question을 식별하기 위한 YOLOv7
* Question num을 인식하기 위한 PORORO
---
* Dataset - 수리통계학 교재 이용
Caption, code, image, image_caption, page_num, question, question_num, table, table_caption, text, title와 같이 11개의 class labeling 진행

## 2. Model
---
### 1) YOLOv7

![Example Image](/images/YOLOv7_architecture.png)

"You Only Look Once" 시리즈의 최신 버전 중 하나로, 실시간 객체 탐지를 위한 딥러닝 모델이다. YOLO v7 말고 v6, v8도 사용했는데, bounding box 정확성 수치와 최종 결과가 v7이 가장 정확하게 나와 채택했습니다. 
YOLOv7의 구조는 위의 사진과 같습니다. 
YOLOv7은 이전 모델보다 최적화뿐만 아니라 훈련 과정 또한 최적화하고자 했다. 구조에 대해 간단하게 설명을 하자면 다음과 같다.
1. Extended efficient layer aggregation networksPermalink
Gradient가 짧을수록 모델이 강력하게 학습할 수 있기에 효율적으로 확장, 셔플, 병합하는 E-ELAN 구조를 사용한다.

2. Model scaling for concatenation-based models
모델 스케일링은 모델을 fine tuning 시켜 추론(inference) 속도를 목적에 맞게 충족시키고자 다양한 스케일의 모델을 생성하는 것이다.

3. Planned re-parameterized convolutionPermalink
네트워크의 순서를 바꿔 추론 비용을 증가시키지 않고 성능을 향상시키는 방법을 이용했다.

4. Coarse for auxiliary and fine for lead loss
레이블 할당 전략은 네트워크 학습을 지원하기 위해 coarse-to-fine lead head guided label assigner를 통해 auxiliary head와 lead head에 soft label을 할당하는 방법을 이용한다.

결과 

### 2) PORORO ; Optical Character Recognition 

