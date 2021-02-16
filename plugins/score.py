from slackbot.bot import listen_to
from plugins.users_df import users_df


@listen_to('^/score')
def mention_func(message):
    user = message.body['user']
    if user in users_df.index.values:
        message.reply(f"今週の目標達成数は{str(int(users_df.at[user, 'score']))}です。")#OK
    else:
        message.reply("まずは「register ユーザー名」でユーザー登録をして下さい。")
