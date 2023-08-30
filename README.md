# Koalpaca-Translation-KR2EN

[데모](http://210.105.193.76:7860/)

데모는 잠시 열어둘 예정이고, 언제닫힐지 모릅니다.

이 프로젝트는, 맥락을 기억하지 않습니다. 한글 문장이 들어오면, 그대로 영어 문장을 출력하는 문장 번역기입니다.

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



