import pyautogui
import os
import sys

# 아래 변수를 바꿔서 원하는 설정을 사용하세요
global base_lat, base_lon, diff_lat, diff_lon, gpx_path

# 시작 위, 경도. 포켓몬 Go가 되는 지역으로 설정하세요.
base_lat = 38.212018
base_lon = 128.591537

# 한 걸음마다 바꿀 위, 경도.
diff_lat = 0.0005
diff_lon = 0.0005

# GPX 파일 위치와 이름. 없으시면 저장하고 싶은 path를 입력하시면 됩니다.
# 예시: "/Users/cjeon/Desktop/test_py_1.gpx"
gpx_path = "pikapika.gpx"


def gen_gpx(lat, lon):
    #
    # GPX 파일을 생성합니다.
    #
    global base_lat, base_lon, diff_lat, diff_lon, gpx_path

    # 하드코딩된 gpx 파일을 l에 담습니다.
    l = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n', '<gpx\n', 'xmlns="http://www.topografix.com/GPX/1/1"\n', 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n', 'xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"\n', 'version="1.1" \n', 'creator="gpx-poi.com">\n', '   <wpt lat="38.212018" lon="128.591537">\n', '   </wpt>\n', '</gpx>']

    # lat과 lon에 따라 위치를 변경합니다.
    l[7] = '   <wpt lat="{}" lon="{}">\n'.format(base_lat + diff_lat * lat, base_lon + diff_lon * lon)

    # 바뀐 위, 경도를 gpx 파일에 씁니다.
    f = open(gpx_path, "w")
    f.writelines(l)
    f.close()

    # 바뀐 위, 경도를 터미널에 씁니다.
    print("현재 위치:")
    print("{}, {}".format(base_lat + diff_lat * lat, base_lon + diff_lon * lon))

    # 세이브 파일을 덮어씁니다.
    write_save(base_lat + diff_lat * lat, base_lon + diff_lon * lon)
    return


def input_manager():
    #
    # Keystroke를 낚아챕니다. command+c 로 종료하게 설정해놨습니다.
    #
    os.system("stty raw -echo")
    c = sys.stdin.read(1)
    os.system("stty -raw echo")
    if ord(c) == 3 or ord(c) == 27:
        print("키보드 인터럽트 감지! 안녕히가세요~")
        exit()
    print(c)
    return c


def write_save(lat, lon):
    #
    # 세이브 파일에 위, 경도를 적습니다.
    # 기본 세이브 파일 이름은 save.txt 입니다.
    #

    f = open("save.txt", "w")
    f.write("{},{}".format(lat, lon))
    f.close()
    return


def load_save():
    #
    # 세이브 파일에서 위, 경도를 불러옵니다.
    # 기본 세이브 파일 이름은 save.txt 입니다.
    #

    try:
        f = open("save.txt", "r")
        line = f.readline()
        f.close()
        return True, float(line.split(",")[0]), float(line.split(",")[1])
    except FileNotFoundError as e:
        print("세이브 파일이 없어 위, 경도를 불러오지 못했습니다. 세이브 파일은 자동생성됩니다.")
        print(e)
    except ValueError as e:
        print("세이브 파일을 파싱하지 못했습니다.")
        print(e)
    return False, base_lat, base_lon


def main():
    global base_lat, base_lon

    print("(1/3)GPS button에 커서를 올려주세요.")
    input("완료되었으면 엔터를 눌러주세요.")

    xcode_gps_button_loc = pyautogui.position()
    print("\n(2/3)GPX file에 커서를 올려주세요.")
    input("완료되었으면 엔터를 눌러주세요.")

    xcode_gpx_file_loc = pyautogui.position()
    print("\n(3/3)터미널에 커서를 올려주세요.")
    input("완료되었으면 엔터를 눌러주세요.")
    terminal_loc = pyautogui.position()

    success, base_lat, base_lon = load_save()
    if success:
        print("\n저장파일에서 좌표값을 자동으로 불러왔습니다.")
    else:
        print("\n저장파일에서 좌표값 불러오기를 실패했습니다.")

    print("\n끝! wasd로 움직이고 cmd + c로 종료하세요.\n좌표가 바뀔 때마다 자동으로 저장됩니다.")
    lat = 0
    lon = 0
    # 인터럽트가 없는 한 아래를 무한반복한다.
    while True:
        k = input_manager()
        if k == 'w':
            lat += 1
        elif k == 'd':
            lon += 1
        elif k == 's':
            lat -= 1
        elif k == 'a':
            lon -= 1
        # gpx 파일 생성
        gen_gpx(lat, lon)
        # gps 버튼 클릭
        pyautogui.moveTo(xcode_gps_button_loc)
        pyautogui.click()
        # gpx 클릭
        pyautogui.moveTo(xcode_gpx_file_loc)
        pyautogui.click()
        # 터미널 클릭
        pyautogui.moveTo(terminal_loc)
        pyautogui.click()
    return

main()
