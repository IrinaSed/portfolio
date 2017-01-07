import locale
import os
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

from mySite.models import Visit, Like

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'mySite', 'static').replace('\\', '/')
FONT_FILE = os.path.join(STATIC_ROOT, 'fonts', 'dpark.ttf')


def get_counter_lines(page, ip):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    day, date, time = Visit.get_last_visit_of(page, ip).strftime("%A, %d.%m.%Y %H:%M").split()
    return [
        ('Посещения', 35),
        ('Сегодня: {}'.format(Visit.today_count()), 35),
        ('Всего: {}'.format(Visit.all_count()), 35), ('', 0),
        ('Последнее: ', 35),
        ('День: {}'.format(day[:-1]), 25),
        ('Дата: {}'.format(date), 25),
        ('Время: {}'.format(time), 25),
    ]


def get_counter_image(page, ip):
    lines = get_counter_lines(page, ip)
    image = Image.new('RGBA', (170, 330), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for i, line in enumerate(lines):
        font = ImageFont.truetype(FONT_FILE, line[1])
        draw.text((10, 20 + i * 40), line[0], (0, 0, 0), font=font)
    buffer = BytesIO()
    image.save(buffer, 'PNG')
    image.close()
    del draw
    buffer.seek(0)
    return buffer


def get_like_image(anchor):
    count = Like.get_count(anchor)
    image = Image.new('RGBA', (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_FILE, 34)
    draw.text((0, 0), str(count), (255, 255, 255), font=font)
    buffer = BytesIO()
    image.save(buffer, 'PNG')
    image.close()
    del draw
    buffer.seek(0)
    return buffer
