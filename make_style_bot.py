import os
import glob
import pandas
import itertools
import torch
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
from torch import nn
import torch.nn.init as init
import torchvision.transforms as transforms
from PIL import Image
from torchvision.utils import make_grid
import numpy as np
# import matplotlib.pyplot
import random
import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

token = '6366790338:AAHffN3bItg_Gy_lhL4kz3GvMCcSPyoKOXQ'
bot = telebot.TeleBot(token)
commands = ['/start']

@bot.message_handler(commands=['start'])
def start(message):
    global msg1


    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Choose a photo", "Propose your photo"]
    reply_markup.row(*buttons)
    # for item in buttons:
    #     print(item)
    #     markup.row(telebot.types.KeyboardButton(item))

    stroka = 'This bot'
    msg1 = bot.send_message(message.chat.id, stroka , reply_markup=reply_markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Choose a photo"):
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Choose a photo", "Propose your photo"]
        reply_markup.row(*buttons)
        # for item in buttons:
        #     print(item)
        #     markup.row(telebot.types.KeyboardButton(item))

        stroka = 'Choose one of the proposed photos'
        bot.send_message(message.chat.id, stroka,reply_markup=reply_markup)
    elif (message.text == "Propose your photo"):
        stroka = 'send your photo'
        bot.send_message(message.chat.id, stroka)
    else:
        reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Choose a photo", "Propose your photo"]
        reply_markup.row(*buttons)

        bot.send_message(message.chat.id,
                         'I dont know what I should reply',
                         parse_mode="HTML", reply_markup=reply_markup)


@bot.message_handler(content_types=['photo'])
def photo(message):
    # print 'message.photo =', message.photo
    fileID = message.photo[-1].file_id
    # print 'fileID =', fileID
    file_info = bot.get_file(fileID)
    # print 'file.file_path =', file_info.file_path
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

if __name__ == '__main__':
    # utils.count_rows()
    random.seed()
    bot.infinity_polling()


