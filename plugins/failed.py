from slackbot.bot import listen_to
from plugins.users_df import DFGenerator
import numpy as np


@listen_to(r'^/failed')
def mention_func(message):
    user = message.body['user']
    generator = DFGenerator()
    df = generator.df
    if user in df.index.values:
        goal = df.at[user, 'goal']
        if type(goal) is str:
            df.at[user, 'goal'] = np.NaN
            message.reply(f"「{goal}」を達成できませんでした...次は頑張ろう！")
            generator.save()
        else:
            message.reply(f"目標が設定されていません...それはともかく次は頑張ろう！")

    else:
        message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。")
