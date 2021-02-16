from slackbot.bot import listen_to
from plugins.users_df import users_df
import numpy as np
import math


@listen_to(r'^/failed')
def mention_func(message):
    user = message.body['user']
    if user in users_df.index.values:
        goal = users_df.at[user, 'goal']
        if type(goal) is str:
            users_df.at[user, 'goal'] = np.NaN
            message.reply(f"「{goal}」を達成できませんでした...次は頑張ろう！")#OK
        else:
            message.reply(f"目標が設定されていません...それはともかく次は頑張ろう！")#OK

    else:
        message.reply("まずは「register ユーザー名」でユーザー登録をして下さい。")#OK
