from isOdd import isOdd
from progress.bar import Bar
import time
import emoji
import matplotlib.pyplot as plt
import numpy as np
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

print(isOdd(2))
print(isOdd(1))

print(isOdd(0))
print(isOdd(4))


with Bar('Processing', max=20) as bar:
    for i in range(20):
        # Do some work
        time.sleep(0.5)
        bar.next()
    bar.finish()

print(emoji.emojize('Python is :thumbs_up:'))




# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

list = [1,2,3,2,7]
plt.plot(list)

plt.show()


updater = Updater('5973868843:AAEe-ZreWg4SpGUTVYhzMJ75mS1iijy74Kw')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('ping', pinguin_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))




print('server start')
updater.start_polling()
updater.idle()