# sokChoGo
속초로가자!!

**회사에서 작성한거라 많이 부실합니다.  </br>
퇴근시간이 지나서 날림으로 작성했는데 양해바랍니다.**

# Requirements

0. Iphone & Mac. 
1. Apple Developer ID => 아이폰에 gpx 를 올리기 위해 필요합니다.
2. XCode.
3. pyautogui. 마우스 위치 인식과 클릭을 위해 사용합니다. 설치는 https://pyautogui.readthedocs.io/en/latest/install.html 를 참고하시고, 혹시 PIL을 설치하라고 하면 Image 를 설치하시면 됩니다.

# How it works

1. w, a, s, d를 누를 때마다 위도, 경도(0.0002씩)를 바꾼 GPX파일이 생성됩니다. (0.0002가 적합한지는 모르겠습니다. 자유롭게 변경하세요.)
2. XCode에서 이 gpx파일을 아이폰에 인식시켜 실제로 그 위치에 있는 것으로 착각하게 만듭니다.
3. 무한반복합니다. profit!

# How to use

(중요! script안에 gpx 경로가 하드코딩되어있으니 적절하게 바꾸어서 사용하세요!)
(`f = open("/Users/cjeon/Desktop/test_py_1.gpx","w")`)

1. repo 를 clone 받으시거나, 어차피 .py 파일은 하나밖에 없으니까 그냥 다운받으십니다.
2. Xcode에서 simple iphone project를 생성합니다.
(2.5 최초 gpx 업로드시 XCODE에서 수동으로 add gpx file to project... 를 해주셔야 3번에서 정상동작합니다. 사진 2 최하단 참조.)
3. XCode에서 gps 아이콘 위에 마우스를 가져다대고 엔터를, 사용하실 gpx 파일 이름 위에 마우스를 두고 엔터를, 터미널 위에 마우스를 두시고 엔터를 누르시면 좌표가 등록됩니다.
4. 이제 wasd 로 조작하시고, command + c로 escape 하시면 됩니다.

gps 아이콘
(Test 1 왼쪽 파랑색 아이콘)
![alt tag](http://i.imgur.com/M9h8Lgk.png)


사용하실 gpx 파일 이름
(해당 화면에선 test_py_1)
![alt tag](http://i.imgur.com/4bSNR8q.png)
