from plugins.users_df import users_df
from slackbot.bot import listen_to


@listen_to(r"^/unregister")
def mention_func(message):
    user = message.body['user']
    if user in users_df.index.values:
        name = users_df.at[user, 'name']
        message.reply(f"{name}さんのユーザー登録を解除しました。")
        users_df.drop(user, axis=0, inplace=True)
    else:
        message.reply("ユーザー登録されていません。")
