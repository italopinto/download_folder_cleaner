import os
import shutil
import sys
from pytube import YouTube

SRC = '/home/italo/Pictures'
DST = '/home/italo/Downloads'


def menu():
    print('Teste do Watchdog com o diretorio Downloads:')
    print('[1] Mover arquivo.')
    print('[2] Deletar arquivo.')
    print('[3] Baixar vídeo do YouTube')
    print('[4] Sair.')
    option = input('Opção: ')

    if option == '1':
        move_file()
        print()
        menu()
    elif option == '2':
        delete_file()
        print()
        menu()
    elif option == '3':
        download_from_youtube()
        print()
        menu()
    elif option == '4':
        sys.exit()


def move_file():
    os.chdir(SRC)
    if not os.path.exists(DST + '/ass.png'):
        shutil.copy2(SRC + '/ass.png', DST)
        print('Arquivo copiado com sucesso!')
    else:
        print('Arquivo já existe.')


def delete_file():
    os.chdir(DST)
    if not os.path.exists('ass.png'):
        print('Arquivo já não está mais aqui.')
    else:
        os.remove('ass.png')
        print('Arquivo deletado com sucesso!')


def download_from_youtube():
    video = input('Cole aqui a URL do vídeo do YouTube: ')
    yt = YouTube(video)
    try:
        yt.streams.filter(progressive=True).first().download(DST)
        print('Download efetuado com sucesso!')
    except:
        print('Deu merda!')


if __name__ == '__main__':
    menu()


'''import os
os.chdir('/home/italo/Downloads')
print(os.path.getsize('Questão.de.Honra.Xivd.Dvdrip.[Dublado].avi')/1000000)
print(type(os.path.getsize('Questão.de.Honra.Xivd.Dvdrip.[Dublado].avi')))'''