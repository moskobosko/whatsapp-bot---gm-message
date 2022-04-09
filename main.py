import os.path
import datetime
import pyautogui as pt
from time import sleep
import keyboard
import daytime
import pyperclip as pc

application_path = os.path.dirname("sys.executable")


def nav_to_image(image, clicks, off_x=0, off_y=0, morning=False, region=(0, 0, 1920, 1080)):
    position = pt.locateOnScreen(image, region=region, confidence=.7)

    if position is None:
        print("image not found")
        return 0
    else:
        if morning is False:
            pt.moveTo(position, duration=.5)
            pt.moveRel(off_x, off_y)
            pt.click(clicks=clicks, interval=.1)


def schedule():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    while True:
        if (day == "Thursday" and now.hour >= 7 and now.hour <= 9) or (
                day == "Friday" and now.hour >= 8 and now.hour <= 10):
            main()
            sleep(60*4)
        else:
            sleep(30)
        now = datetime.datetime.now()
        day = now.strftime("%A")


def my_function():
    if nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\good_morning.png', clicks=1, morning=True, region=(0, 0, 1250, 950)) != 0:
        nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\paperclip.png', clicks=2, off_x=-100)
        keyboard.write("בוקר טוב")
        pt.press('enter')
    else:
        return 0


def mosko():
    if nav_to_image('images/mosko.png', clicks=0, region=(0, 0, 1250, 950)) != 0:
        nav_to_image('images/magnifying_glass.png', clicks=1, off_x=-100)
        keyboard.write('אמא')
        nav_to_image('images/mom.png', clicks=1)
        nav_to_image('images/paperclip.png', clicks=1, off_x=-100)
        keyboard.write("תתקשרי אליי!")
        pt.press('enter')
    else:
        return 0


def main():
    sleep(1)
    nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\google.png', clicks=1)
    nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\google_2.png', clicks=1)
    sleep(1)
    nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\whatsapp.png', clicks=1)
    sleep(10)
    while nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\Deep_Learning.png', clicks=1) == 0:
        sleep(1)
    nav_to_image(r'C:\Users\Eyal\PycharmProjects\whatsapp_bot_1\images\Deep_Learning.png', clicks=1)
    sleep(0.5)

    while my_function() == 0:
        sleep(5)
    #my_function()
    #while mosko() == 0:
    #    sleep(15)
    #mosko()


if __name__ == '__main__':
    schedule()

# #def get_message():
#     nav_to_image('images/paperclip.png', clicks=3, off_x=-40, off_y=-90)
#     pt.click(button='right')
#     nav_to_image('images/copy.png', clicks=1)
#     nav_to_image('images/plus.png', clicks=1)
#     pt.click(1600, 50)
#     pt.click(button='right')
#     nav_to_image('images/paste.png', clicks=1)
#     keyboard.press('enter')
#     sleep(1)
#     pt.click(1700, 500)
#     nav_to_image('images/plus.png', clicks=3, off_y=25)
#     pt.click(button='right')
#     nav_to_image('images/copy.png', clicks=1)
#     pt.press('space')
#
#     pt.click(1800, 20)
#     nav_to_image('images/paperclip.png', clicks=1, off_x=-100)
#     pt.click(button='right')
#     nav_to_image('images/paste.png', clicks=1)
#     sleep(1

# )
    # keyboard.press('enter')


# get_message()
