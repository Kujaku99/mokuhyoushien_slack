from slackbot.bot import listen_to
from plugins.users_df import users_df
import numpy as np


@listen_to(r"^/finish")
def mention_func(message):
    user = message.body['user']
    if user in users_df.index.values:
        users_df.at[user, 'score'] += 1
        goal = users_df.at[user, 'goal']
        if type(goal) is str:
            message.reply(f"「{goal}」を達成しました！お疲れ様です！！今週の目標達成数は{str(int((users_df.at[user, 'score'])))}です！")#OK
            users_df.at[user, 'goal'] = np.NaN
        else:
            message.reply(f"目標が登録されていません...それはともかくお疲れ様です！！今週の目標達成数は{str(int((users_df.at[user, 'score'])))}です！")  # OK
    else:
        message.reply("まずは「register ユーザー名」でユーザー登録をして下さい。")
