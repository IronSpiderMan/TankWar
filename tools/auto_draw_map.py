# from PIL import Image
# from settings import Settings
#
# settings = Settings()
#
# im = Image.new("RGB", (30*19, 30*15), (200, 200, 200))
#
# x, y = 0, 0
# print(len(settings.MAP_ONE))
# for i in settings.MAP_ONE:
#     for j in i:
#         print(j)
#         temp_im = Image.open(f'../resources/images/test_img/{j}.png')
#         im.paste(temp_im, (x*30, y*30))
#         x += 1
#     x = 0
#     y += 1
# im.show()






# import os
#
# import pygame
#
# class MyImage:
#
#     def __init__(self, image, rect=None):
#         self.image = image
#         self.rect = rect
#
#
# path = r"D:\Coding Files\Workplace\PythonWorkplace\TankWar2.0\resources\images\test_img"
#
# files = [path + "\\" + file for file in os.listdir(path)]
#
# pygame.init()
#
# screen = pygame.display.set_mode((30*19, 30*15))
#
# pygame.display.set_caption("地图生成器")
#
# images = []
#
# for i in range(15):
#     for j in range(19):
#         image = pygame.image.load(files[1])
#         myImage = MyImage(image)
#         myImage.image = image
#         myImage.rect = pygame.Rect(30*j, 30*i, 30, 30)
#
#         images.append(image)
#         screen.blit(image, myImage.rect)
# while True:
#     for event in pygame.event.get():
#         if event == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.update()

def func():
    import os
    import PySimpleGUI as sg

    path = r"D:\Coding Files\Workplace\PythonWorkplace\TankWar2.0\resources\images\walls"

    files = [path + "\\" + file for file in os.listdir(path)]

    sg.Image()

    layout = [
        [sg.Image(files[0], size=(30, 30), enable_events=True) for i in range(19)] for j in range(15)
    ]
    layout.append([sg.Button("保存地图"), sg.Button("重置"), sg.Button("退出")])

    window = sg.Window("绘制地图", layout)
    while True:
        event, values = window.read()
        if event in (None, "确定"):
            window.refresh()
        elif event in range(285):
            print(event)
            elem = window.find_element(event)
            num = elem.Filename.split("\\")[-1].split(".")[0]
            num = (int(num) + 1) % 5
            elem.Filename = files[num]
            elem.Update(files[num], size=(30, 30))
            window.refresh()
        elif event in (None, "保存地图"):
            lines = []
            line = []
            img = 0
            for i in range(0, 15):
                for j in range(0, 19):
                    elem = window.find_element(img)
                    num = elem.Filename.split("\\")[-1].split(".")[0]
                    line.append(num)
                    img += 1
                lines.append(line)
                line = []

            content = "["
            for line in lines:
                content += "["
                for num in line:
                    content += num + ", "
                content += "],\n"
            content += "]"

            with open("map.txt", "w") as f:
                f.write(content)
        elif event == "退出":
            window.close()
            exit()

if __name__ == '__main__':
    func()