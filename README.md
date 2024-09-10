# fishregression

### 작업 순서
1. 빙어 + 도미 데이터로 LinearRegression 학습
2. (1) 을 모델을 저장
3. API 화( FastAPI ) -> 도커 패키징 -> 컨테이너 RUN ( 8001 )
4. 기존의 KNeighborsClassifier API 도커 RUN ( 8002 )
5. cli 프로그램 생성 - input 으로 길이 받기 -> (3) 호출 -> (4) 호출 -> 결과(빙어, 도미) 출력

![image](https://github.com/user-attachments/assets/56121192-44a1-4407-b7b6-0f31018bfb9b)

### usage
```bash
$ pip install git+https://github.com/j25ng/fishregression.git
$ fish
$ 🐟 물고기의 길이를 입력하세요 (cm): 10
$ 🐟 물고기는 빙어로 예측됩니다.
```
#### LB/default.conf
```
server {
    listen 80;

    location /how_weight/ {
        proxy_pass http://<server ip>:8001/;
    }

    location /kind_fish/ {
        proxy_pass http://<server ip>:8002/;
    }
}
```
#### Docker
```bash
$ sudo docker run -d -p 8001:8080 --name rg j25ng/fishregression:0.1.0
$ sudo docker run -d -p 8002:8080 --name ml j25ng/fishmlserv:0.8.3
$ sudo docker run -d -p 8080:80 --name lb j25ng/lb:0.1.0
```
