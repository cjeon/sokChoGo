# sokChoGo
속초로가자!!

# Requirements

0. Iphone & Mac. 
1. Apple Developer ID => 아이폰에 gpx 를 올리기 위해 필요합니다.
2. XCode.
3. pyautogui. 마우스 위치 인식과 클릭을 위해 사용합니다.  
설치는 https://pyautogui.readthedocs.io/en/latest/install.html 를 참고하시고, 혹시 PIL을 설치하라고 하면 Image 를 설치하시면 됩니다.

# Setup

## Environments
0. `brew install python3`
1. `pip3 install pyobjc-core`
2. `pip3 install pyobjc`
3. `pip3 install pyautogui`
4. (optional) `pip3 install image`  

## XCode
0. Xcode를 키신 후 `Create a new Xcode project`클릭.
1. ios > Application > `Single View Application`
2. 아무렇게나 setup하고 `next`
3. Developer mode가 활성화된 아이폰으로 연결.
4. Build 합니다. Build 하려면 Apple Developer ID가 필요합니다.

## sokChoGo
0. sokChoGo 를 실행하신 후 지시에 따라 마우스커서를 움직이면서 엔터를 누릅니다. 좌표 기록을 위함입니다.
1. How it works와 How to use를 참고하세요.

# How it works

1. w, a, s, d를 누를 때마다 위도, 경도(0.0002씩)를 바꾼 GPX파일이 생성됩니다. (0.0002가 적합한지는 모르겠습니다. 자유롭게 변경하세요.)
2. XCode에서 이 gpx파일을 아이폰에 인식시켜 실제로 그 위치에 있는 것으로 착각하게 만듭니다.
3. 무한반복합니다. profit!

# How to use

1. repo 를 clone 받으세요. `git clone https://github.com/cjeon/sokChoGo.git`
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
