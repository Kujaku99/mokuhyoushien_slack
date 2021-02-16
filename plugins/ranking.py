from slackbot.bot import listen_to
from plugins.users_df import users_df


@listen_to(r"^/ranking")
def mention_func(message):
    users_df_s = users_df.sort_values('score', ascending=False)
    users_df_s['rank'] = users_df_s['score'].rank(method="min", ascending=False)
    ranking_message = "\n【今週の目標達成数ランキング】\n"
    for row in users_df_s.itertuples():
        rank = row.rank
        name = row.name
        score = row.score
        ranking_message += f"{str(int(rank))}位: {name}さん({str(int(score))}回)\n"
    message.reply(ranking_message)
