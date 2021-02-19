from slackbot.bot import listen_to
from plugins.users_df import DFGenerator
import numpy as np


@listen_to(r"^/finish")
def mention_func(message):
    user = message.body['user']
    generator = DFGenerator()
    df = generator.df
    if user in df.index.values:
        df.at[user, 'score'] += 1
        goal = df.at[user, 'goal']
        if type(goal) is str:
            message.reply(f"「{goal}」を達成しました！お疲れ様です！！今週の目標達成数は{str(int((df.at[user, 'score'])))}です！")
            df.at[user, 'goal'] = np.NaN
        else:
            message.reply(f"目標が登録されていません...それはともかくお疲れ様です！！今週の目標達成数は{str(int((df.at[user, 'score'])))}です！")
        generator.save()
    else:
        message.reply("まずは「register ユーザー名」でユーザー登録をして下さい。")
