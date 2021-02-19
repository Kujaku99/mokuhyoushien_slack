from slackbot.bot import listen_to
from plugins.users_df import DFGenerator


@listen_to('^/score')
def mention_func(message):
    user = message.body['user']
    generator = DFGenerator()
    df = generator.df
    if user in df.index.values:
        message.reply(f"今週の目標達成数は{str(int(df.at[user, 'score']))}です。")
    else:
        message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。")
