from slackbot.bot import listen_to
from plugins.users_df import users_df


@listen_to(r'^/start\s+\S.*')
def mention_func(message):
    user = message.body['user']
    temp, goal = message.body['text'].split(None, 1)
    if "\n" in goal:
        goal, _ = goal.split("\n", 1)

    if user in users_df.index.values:
        users_df.at[user, 'goal'] = goal
        message.reply(f"目標を「{goal}」に設定しました。頑張って下さい！！")#OK
    else:
        message.reply("まずは「register ユーザー名」でユーザー登録をして下さい。")
