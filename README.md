## Django-practice
#### App list
1. home - 메인 페이지
2. vl - 사진을 입력받아 어느 나라인지 분류(한국, 프랑스, 이탈리아, 미국, 호주)
3. board - 게시판
4. accounts - 회원가입, 로그인, 로그아웃
#### VL
학습데이터
크롤러를 사용하여 구글 스트리트 뷰 데이터 수집
각 클래스별 1500장(학습:1000, 검증:300, 테스트:200)
google_street_view_crawler.ipynb 참고
모델학습
EfficientnetB0 모델을 사용하여 분류모델 학습
EfficientnetB0 모델의 가중치를 초기화 시키고 모델은 그대로 사용
 Jetson_nano_EfficientnetB0_training_5_classes.ipynb 참고 