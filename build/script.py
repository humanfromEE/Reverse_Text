from time import strftime # Для створення імені файлу з датою
from msvcrt import getch # Для затримки програми перед закриттям
import os # Чистка консолі при перезапуску програми, створення каталогів і перевірка їх існування (створення ярлика для програми)

# Увід користувацького текст і поверення його розвернутому вигляді
def InputAndReverseText():
    print('Уведіть ваш текст:', '\n', end = '\t')
    inputUserText = input()
    returnReverseText = ''
    for i in range(len(inputUserText) - 1, -1, -1):
        returnReverseText += inputUserText[i]
    return str(returnReverseText)

# Вивід перевернутого тексту
def OutputReverseText(textReverse = str, countTab = int):
    if (countTab <= 0):
        countTab = 1
    print('Reverse text', '\n', countTab * '\t', textReverse)

# Створення журналу роботи програми
def CreateOrAppendDataInHistoryFile(NameFile = str):
    fileHistory = open(os.getcwd() + '\\history data.txt', 'a')
    fileHistory.write(NameFile + '\n')
    fileHistory.close()

# Створення імені файлу
def CreateNameFile():
    NameFile = '[' + strftime('%d') + '.' + strftime('%m') + '.' + strftime('%Y') + ', '
    NameFile += strftime('%H') + '-' + strftime('%M') + '-' + strftime('%S') + '] '
    NameFile += 'Reverse Text.txt'
    return str(NameFile)

# Створення файлу й оголошення про це
def CreateFilesProgram(textRecord = str, usePath = str):
    if (textRecord != ''):
        # Створення назви файлу, файлу і запис з закриттям
        NameFile = CreateNameFile()
        filePassword = open(usePath + NameFile, 'w')
        filePassword.write(textRecord)
        filePassword.close()
    
        # Стоворення того самого на робочому столі
        fileDesktop = open(os.path.expanduser('~') + '\\Desktop\\' + NameFile, 'w')
        fileDesktop.write(textRecord)
        fileDesktop.close()

        print('Дані записано за адресою у файл:', end = '\n\t')
        print(os.path.expanduser('~') + '\\Desktop\\' + NameFile)
        CreateOrAppendDataInHistoryFile(NameFile)
        OutputReverseText(textRecord, 1)
    else:
        print('У тексті відсутні символи, файл не записано')

def CreateCurrentFolderAndFileIn(textReverse = str):
    File_Path = os.getcwd() + '\\Work Folder\\'
    if (not os.path.exists(File_Path)):
        os.makedirs(File_Path)
    CreateFilesProgram(textReverse, File_Path)

# Вихід або повтор програми
def ExitProgram():
    countEqualSymbol = 75
    print()
    print('=' * countEqualSymbol)
    answerReplay = input('Бажаєте перезапустити програму (\"+\" - так)?: ')
    if (answerReplay == '+'):
        print('\t', 'Консоль буде очищено, натисніть будь-яку клавішу ...')
    else:
        print('\t', 'Програму завершено, натисніть будь-яку клавішу ...')
    print('=' * countEqualSymbol)
    getch()
    os.system('cls')

    if (answerReplay == '+'):
        return False
    else:
        return True

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================

# Головна програма
while (True):
    
    myText = InputAndReverseText()
    CreateCurrentFolderAndFileIn(myText)

    if (ExitProgram()):
        break