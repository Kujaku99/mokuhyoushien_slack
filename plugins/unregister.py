from plugins.users_df import DFGenerator
from slackbot.bot import listen_to


@listen_to(r"^/unregister")
def mention_func(message):
    user = message.body['user']
    generator = DFGenerator()
    df = generator.df
    if user in df.index.values:
        name = df.at[user, 'name']
        message.reply(f"{name}さんのユーザー登録を解除しました。", in_thread=True)
        df.drop(user, axis=0, inplace=True)
        generator.save()

    else:
        message.reply("ユーザー登録されていません。", in_thread=True)
