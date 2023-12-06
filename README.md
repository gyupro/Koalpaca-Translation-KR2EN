# Koalpaca-Translation-KR2EN

이 프로젝트는, 맥락을 기억하지 않습니다. 한글 문장이 들어오면, 그대로 영어 문장을 출력하는 문장 번역기입니다.

성능을 향상시킬수 있는 더 좋은 아이디어 있으면 이슈 부탁드리겠습니다. !

## 테스트 된 환경

- Ubuntu 20.04
- pytorch 2.1.1

V100 기준 GPU VRAM 사용량 : 12GB

## 설치 및 실행

필요한 라이브러리 설치
```bash
git clone https://github.com/gyupro/Koalpaca-Translation-KR2EN.git
cd Koalpaca-Translation-KR2EN
pip install -r requirements.txt
```
실행
```bash
python serving.py
```
위의 파이썬 커맨드 실행 후, [http://localhost:7860](http://localhost:7860)으로 들어가시면 gradio 채팅 앱이 보일껍니다. 입력문장에 한글을 입력하시고, 엔터를 누르시면 번역된 결과를 보실수 있습니다.

![image](https://github.com/gyupro/Koalpaca-Translation-KR2EN/assets/79894531/9f2cb1df-78de-4433-b9fc-f425fc4519dd)

필요한 모델 & 토크나이저는 자동으로 다운됩니다.

## 데이터셋

데이터셋은 AIHUB의 구어체 번역 데이터셋을 사용했습니다. [AIHUB](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71265)

Train 폴더에 있는 데이터만 사용했으며, 데이터셋을 전처리한 코드는 [여기](make_dataset.ipynb) 에서 보시면 됩니다.

[KO_TO_EN](https://drive.google.com/file/d/12qNXQ3SPKLHGa3PuuAFQD2NI3-qV15Xa/view?usp=sharing) source 한국어 target 영어 120만 문장 쌍  
[EN_TO_KO](https://drive.google.com/file/d/1pzgN2PvKfY5cgWR0V9cE1J6JukrrDcRc/view?usp=sharing) source 영어 target 한국어 120만 문장 쌍

## 데이터셋 예제
[여기에서 확인해볼수 있습니다.](make_dataset.ipynb)

## 학습

학습은 위의 KO_TO_EN과 EN_TO_KO를 모두 source KO target EN으로 학습시켰으며, Koalpaca의 run_tensor_parellel.py파일을 사용했습니다.
사용된 모델은 polyglot 5.8B입니다.

# 장점
학습된 어체가 구어체이다보니, 구어체를 잘 인식하고 상황에 맞게 잘 번역합니다.

# 단점
학습된 문장 자체가 짧은 단문이기 때문에, 긴문장 번역에 취약점을 보입니다. 또한 구어체 번역이기에, 전문 서적, 전문번역 성능은 떨어집니다.

