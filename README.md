## Django-practice
#### App list
1. home - 메인 페이지
2. vl - 사진을 입력받아 어느 나라인지 분류(한국, 프랑스, 이탈리아, 미국, 호주)
3. board - 게시판
4. accounts - 회원가입, 로그인, 로그아웃
#### VL
 크롤러를 사용하여 구글 스트리트 뷰를 통해 학습데이터 수집
 EfficientnetB0 모델을 사용하여 분류모델 학습
 google_street_view_crawler.ipynb, Jetson_nano_EfficientnetB0_training.ipynb 참고
 Jetson_nano_EfficientnetB0_training.ipynb 의 경우 이진분류모델 예시가 나와 있지만 실제로는 5개의 클래스로 카테고리 분류를 하였다.
 