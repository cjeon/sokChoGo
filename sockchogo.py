import pyautogui

def gen_gpx(lat,lon):
    l =['<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n', '<gpx\n', 'xmlns="http://www.topografix.com/GPX/1/1"\n', 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n', 'xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"\n', 'version="1.1" \n', 'creator="gpx-poi.com">\n', '   <wpt lat="38.212018" lon="128.591537">\n', '      <time>2016-07-13T09:26:39Z</time>\n', '   </wpt>\n', '</gpx>']
    l[7] ='   <wpt lat="{}" lon="{}">\n'.format(38.212018 + 0.0002 * lat, 128.591537+ 0.0002 *lon)
    f = open("/Users/cjeon/Desktop/test_py_1.gpx","w")
    f.writelines(l)
    return

def main():
    print("GPS button에 커서를 올려주세요.")
    input("press enter to continue")
    xcode_gps_button_loc = pyautogui.position()
    print("GPX file에 커서를 올려주세요.")
    input("press enter to continue")
    xcode_gpx_file_loc = pyautogui.position()
    print("터미널에 커서를 올려주세요.")
    input("press enter to continue")
    terminal_loc = pyautogui.position()
    print("끝! wasd로 움직이고 cmd + c로 escape하세요.")
    lat = 0
    lon = 0
    while(True):
        k = inputManager()
        if k == 'w':
            lat += 1
        elif k == 'a':
            lon += 1
        elif k == 's':
            lat -= 1
        elif k == 'd':
            lon -= 1
        gen_gpx(lat,lon)
        pyautogui.moveTo(xcode_gps_button_loc)
        pyautogui.click()
        pyautogui.moveTo(xcode_gpx_file_loc)
        pyautogui.click()
        pyautogui.moveTo(terminal_loc)
        pyautogui.click()
    return

def inputManager():
    import os, sys
    os.system("stty raw -echo")
    c = sys.stdin.read(1)
    os.system("stty -raw echo")
    if ord(c) == 3 or ord(c) == 27:
        print (" keyboard interrupt. quitting. Bye~~")
        exit()
    print(c)
    return c 
    
    
main()
