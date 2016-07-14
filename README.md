# sokChoGo
**낯선 속초가 아닌 편안한 침대에서, 발 대신 방향키로 포켓몬 세상을 누비세요!**  
**Travel the pokemon world in your comfy bed, with your keyboards, not on your legs.**
* 블락될 수도 있으니 보조 gmail을 쓰시는 걸 추천합니다.
* You may be banned. Please Use at your own risk.

시연 & 설명 동영상 (클릭하시면 youtube로 이동합니다. 자막을 켜시면 설명을 보실 수 있습니다.)  
Sample & explanation video (click the below image to view video on youtube. Enable subtitles to see explanations. Sorry that En subtitle is not yet ready :/)  
[![IMAGE ALT TEXT](http://img.youtube.com/vi/NGt5XR5E5wg/0.jpg)](http://www.youtube.com/watch?v=NGt5XR5E5wg "sokChoGo 시연")

모니터가 2대 이상일 때는 메인 모니터 좌표값이 인식됩니다. 터미널과 엑스코드를 주 모니터에 두시고 사용하세요. 개선할 방법을 찾고 있습니다.
When there are two or more monitors, coordinates of the main monitor is used. Please place your terminal and XCode in your main monitor. I'm trying to solve this problem.

# Table of Contents
* KR
* [Requirements](https://github.com/cjeon/sokChoGo#Requirements)
* [Setup](https://github.com/cjeon/sokChoGo#Setup)
* [How it works](https://github.com/cjeon/sokChoGo#how-it-works)
* [How to use](https://github.com/cjeon/sokChoGo#how-to-use)
* [Contribution](https://github.com/cjeon/sokChoGo#Contribution)
* [EN](https://github.com/cjeon/sokChoGo#en)
* [Requirements](https://github.com/cjeon/sokChoGo#requirementsen)
* [Setup](https://github.com/cjeon/sokChoGo#setupen)
* [How it works](https://github.com/cjeon/sokChoGo#how-it-worksen)
* [How to use](https://github.com/cjeon/sokChoGo#how-to-useen)
* [Contribution](https://github.com/cjeon/sokChoGo#contributionen)

# KR
# Requirements

0. Iphone & Mac. 
1. Apple Developer ID => 아이폰에 gpx 를 올리기 위해 필요합니다. (없어도 되는지는 잘 모르겠습니다.)
2. XCode.
3. pyautogui. 마우스 위치 인식과 클릭을 위해 사용합니다.  

# Setup

## Python3
0. `brew install python3`
1. `pip3 install pyobjc-core`
2. `pip3 install pyobjc`
3. `pip3 install image` 
4. `pip3 install pyautogui` 

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

1. w, a, s, d를 누를 때마다 위도, 경도(0.0005씩)를 바꾼 GPX파일이 생성됩니다. (0.0005가 적합한지는 모르겠습니다. 자유롭게 변경하세요.)
2. XCode에서 이 gpx파일을 아이폰에 인식시켜 실제로 그 위치에 있는 것으로 착각하게 만듭니다.
3. 무한반복합니다. profit!

# How to use

1. repo 를 clone 받으세요. `git clone https://github.com/cjeon/sokChoGo.git`
2. Xcode에서 simple iphone project를 생성합니다. (setup의 xcode 참고)    
(2.5 최초 gpx 업로드시 XCODE에서 수동으로 add gpx file to project... 를 해주셔야 3번에서 정상동작합니다. 사진 2 최하단 참조.)
3. sockchogo.py 에서 자유롭게 변수를 변경합니다.
4. XCode에서 gps 아이콘 위에 마우스를 가져다대고 엔터를, 사용하실 gpx 파일 이름 위에 마우스를 두고 엔터를, 터미널 위에 마우스를 두시고 엔터를 누르시면 좌표가 등록됩니다.
5. 이제 wasd 로 조작하시고, command + c로 escape 하시면 됩니다.
(4번과 5번 과정을 최상단 youtube video에서 진행하였으니 참고해주세요. 자막을 켜고 보세요!)

## gps 아이콘  
(Test 1 왼쪽 파랑색 아이콘)  
![alt tag](http://i.imgur.com/M9h8Lgk.png)


## 사용하실 gpx 파일 이름  
(해당 화면에선 test_py_1)  
![alt tag](http://i.imgur.com/4bSNR8q.png)  

# Contribution
자유롭게 PR 넣어주세요!

# En
# Requirements(en)

0. Iphone & Mac. 
1. Apple Developer ID => needed to upload gpx files to iPhone. (not sure if it's necessary)
2. XCode.
3. pyautogui. Used to get mouse position and trigger clicks.

# Setup(en)

## Python3
0. `brew install python3`
1. `pip3 install pyobjc-core`
2. `pip3 install pyobjc`
3. `pip3 install image`
4. `pip3 install pyautogui`

## XCode
0. Open Xcode, and click `Create a new Xcode project`.
1. ios > Application > `Single View Application`
2. Write anything until `next` is clickable.
3. Connect your iphone with your mac. (* dev mode needed.)
4. Build your empty project. 

## sokChoGo
0. Run sokChoGo by typing `python3 sokchogo.py` in your terminal. Set your mouse cursor location according to setup message.
1. Refer to How it Works and How to use for details.

# How it works(en)

1. A new GPX file with different lattitude and longitude is generated everytime you press `w,a,s,d` buttons. (W goes north, D goes east, etc. )
2. Then XCode fools your iphone using the newly made GPX file.
3. Infinite loop => PROFIT!

# How to use(en)

1. Clone this repo by `git clone https://github.com/cjeon/sokChoGo.git`
2. Create a simple iphone project in XCode.  
(2.5 For the first time, you need to add GPX file to your project manually. Refer to last row of second image.)
3. Change variables in sokchogo.py. 
4. Press enters in following steps. Enters must be pressed when you're focused on terminal (not XCODE). First, GPS icon (blue one) on XCode, GPX filename on XCode, Terminal, on terminal. (refer to attached images)
5. You're all set! Navigate world with WASD.

## gps icon 
(blue icon left to "Test1")  
![alt tag](http://i.imgur.com/M9h8Lgk.png)


## GPX filename 
(test_py_1 in below image)  
![alt tag](http://i.imgur.com/4bSNR8q.png)  

# Contribution(en)
Any kind of PR are welcome!
