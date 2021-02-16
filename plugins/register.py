from slackbot.bot import listen_to
from plugins.users_df import users_df
import numpy as np


@listen_to(r'^/register\s+\S.*')
def mention_func(message):
    user = message.body['user']
    register_message = message.body['text']
    temp, name = register_message.split(None, 1)
    #改行を含んでいたら改行以降を捨てる
    if "\n" in name:
        name, _ = name.split("\n", 1)
    users_list = users_df.index.values.tolist()
    if user in users_list:
        old_name = users_df.at[user, 'name']
        message.reply(f"{old_name}さんは既に登録されています。名前を{name}に変更しました。")
        users_df.at[user, 'name'] = name
    else:
        users_df.at[user] = [name, np.NaN, 0]
        message.reply(f"{name}さんを登録しました。")
