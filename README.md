# 24-1_DSL_Modeling_A-uto-ssignment
24-1_DSL_Modeling_A(uto)ssignment

## 주제
* 사용자가 원하는 번호만을 추출하여 하나의 문제집으로 제작

### Team 유현동 정성오 김현동 고현아
---
# Overview
[![발표 자료](/24-1_Modeling_CV_A(uto)ssignment.pdf)]


## 1. Overall Pipeline
---
![Example Image](/images/pipeline.png)

* Question을 식별하기 위한 YOLOv7
* Question num을 인식하기 위한 PORORO

## 2. Model
---
### 1) YOLOv7

![Example Image](/images/YOLOv7_architecture.png)

YOLO(You Only Look Once)는 객체 탐지 모델로, 이미지를 한 번만 보고도 여러 객체를 탐지하고 분류할 수 있습니다. 이 모델들은 전체 이미지를 한 번에 처리함으로써 빠른 속도로 실시간 객체 탐지를 가능하게 합니다.

YOLOv7은 이 시리즈의 최신 버전 중 하나로, 이전 버전들보다 더욱 향상된 정확도와 속도를 보입니다. 1-stage detector인 YOLOv7은 객체 탐지에 필요한 연산량을 줄이면서도 뛰어난 성능을 유지합니다. YOLOv7는 아키텍처의 최적화, 더욱 정교해진 학습 방법, 그리고 성능 향상을 위한 다양한 기술적 개선을 포함합니다. 이러한 개선들 덕분에 YOLOv7은 더 빠른 추론 속도와 향상된 탐지 정확도를 이루어냄으로써, 객체 탐지 분야에서 새로운 기준을 제시하고 있습니다.
