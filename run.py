from slackbot.bot import Bot
import time
import schedule
from plugins.post_ranking import post_ranking
import threading


schedule.every().sunday.at("10:00").do(post_ranking)


def func_bot():
    bot = Bot()
    bot.run()


def func_periodic():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    thread_1 = threading.Thread(target=func_bot)
    thread_2 = threading.Thread(target=func_periodic)

    thread_1.start()
    thread_2.start()
