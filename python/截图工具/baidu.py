# @ Time    : 2019/2/27 15:01
# @ Author  : JuRan

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11739882'
API_KEY = 'NAt4QZZIIOy4m2KkFkPxn8vZ'
SECRET_KEY = '2SdDDDXYEPXceNSimy6Dce8bPPGbBfwB'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_content():
    image = get_file_content('screen.png')

    content = client.basicGeneral(image)
    # print(content['words_result'])

    image_content = ""
    for words in content['words_result']:
        image_content += words['words']

    return image_content

# print(get_content())

