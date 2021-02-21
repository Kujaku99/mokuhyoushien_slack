'''
from slackbot.bot import listen_to
from plugins.users_df import DFGenerator


@listen_to(r"^/ranking")
def mention_func(message):
    generator = DFGenerator()
    df = generator.df
    df_s = df.sort_values('score', ascending=False)
    df_s['rank'] = df_s['score'].rank(method="min", ascending=False)
    ranking_message = "\n【今週の目標達成数ランキング】\n"
    for row in df_s.itertuples():
        rank = row.rank
        name = row.name
        score = row.score
        ranking_message += f"{str(int(rank))}位: {name}さん({str(int(score))}回)\n"
    message.reply(ranking_message, in_thread=True)
'''