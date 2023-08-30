# Koalpaca-Translation-KR2EN

[데모](http://210.105.193.76:7861/)

데모는 잠시 열어둘 예정이고, 언제닫힐지 모릅니다.

이 프로젝트는, 맥락을 기억하지 않습니다. 한글 문장이 들어오면, 그대로 영어 문장을 출력하는 문장 번역기입니다.

## 설치 및 실행

필요한 라이브러리 설치.
```bash
pip install -r requirements.txt
```
```python
python serving.py
```

필요한 모델 & 토크나이저는 자동으로 다운됩니다.

## 데이터셋

데이터셋은 AIHUB의 구어체 번역 데이터셋을 사용했습니다. [AIHUB](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71265)

Train 폴더에 있는 데이터만 사용했으며, 데이터셋을 전처리한 코드는 [여기](make_dataset.ipynb) 에서 보시면 됩니다.

[KO_TO_EN](https://drive.google.com/file/d/12qNXQ3SPKLHGa3PuuAFQD2NI3-qV15Xa/view?usp=sharing) source 한국어 target 영어 120만 문장 쌍  
[EN_TO_KO](https://drive.google.com/file/d/1pzgN2PvKfY5cgWR0V9cE1J6JukrrDcRc/view?usp=sharing) source 영어 target 한국어 120만 문장 쌍

## 데이터셋 예제
[여기에서 확인해볼수 있습니다.](make_dataset.ipynb)



