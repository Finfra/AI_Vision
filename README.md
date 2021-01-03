# 시각지능 딥러닝 실무 예제 코드
## 알림 : 이전 수업을 들으신 분들은 아래와 같은 방식으로 clone하세요.
- 2020년 9월 이전에 수업 들으신 분들
```
git clone -b 202008_kaist --single-branch https://github.com/Finfra/AI_Vision.git
```
- 2020년 12월에 수업 들으신 분들
```
git clone -b 202012_DICT --single-branch https://github.com/Finfra/AI_Vision.git
```

# 설치
* Google Mount(필수)
```
from google.colab import drive
drive.mount('/gdrive')
```
* Git Clone
```
%%bash
cd /content/drive/MyDrive/
[ -d AI_Vision ]&&mv AI_Vision AI_Vision.$(date +%Y_%m_%d_%H_%M_%S)
git clone https://github.com/Finfra/AI_Vision
```
