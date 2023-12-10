from PIL import Image
import os

dowloadsFolder = '/users/miguelpereira/Downloads/'

if __name__ == "__main__":
    for filename in os.listdir(dowloadsFolder):
        name, extension = os.path.splitext(dowloadsFolder + filename)
        cont = 0
        if extension in ['.pdf']:
            sqlFolder = '/users/miguelpereira/Dowloads/universidad/'
            os.rename(dowloadsFolder + filename, sqlFolder + filename)
            print('file moved')
            cont += 1
        '''
        if extension in ['.pdf']:
            UnivesidadFolder = '/users/miguelpereira/Dowloads/universidad/'
            os.rename(dowloadsFolder+ filename, UnivesidadFolder + filename)
            print('file moved')
            cont = cont + 1
        if extension in ['.docx']:
            UnivesidadFolder = '/users/miguelpereira/Dowloads/universidad/'
            os.rename(dowloadsFolder+ filename, UnivesidadFolder + filename)
            print('file moved')
            cont = cont + 1
        if extension in ['.ipynb']:
            matematicaFolder = '/users/miguelpereira/Dowloads/matematica/'
            os.rename(dowloadsFolder + filename, matematicaFolder + filename)
            print('file moved')
            cont += 1
        if extension in ['.pptx']:
            UnivesidadFolder = '/users/miguelpereira/Dowloads/universidad/'
            os.rename(dowloadsFolder+ filename, UnivesidadFolder + filename)
            print('file moved')
            cont = cont + 1
        if extension in ['.docx']:
            UnivesidadFolder = '/users/miguelpereira/Dowloads/universidad/'
            os.rename(dowloadsFolder+ filename, UnivesidadFolder + filename)
            print('file moved')
            cont = cont + 1
        '''
    print(f"Se han movido {cont} archivos")
            
        