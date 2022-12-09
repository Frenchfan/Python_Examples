from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import random

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')
    
def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # 3 элемента на выходе /sum 123 4324
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')

def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # 4 элемента на выходе /sum 123 4324 435
    x = int(items[1])
    y = int(items[2])
    z = int(items[3])
    update.message.reply_text(f'{x} + {y} * {x} = {x + y * z}')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')

def pinguin_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Льдинка - лучше всех')
