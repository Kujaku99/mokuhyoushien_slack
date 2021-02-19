from slacker import Slacker
import slackbot_settings
from plugins.users_df import DFGenerator


def post_ranking():
    slack = Slacker(slackbot_settings.API_TOKEN)
    channel = 'pj_みんなで応援チャンネル'
    generator = DFGenerator()
    df = generator.df
    df_s = df.sort_values('score', ascending=False)
    df_s['rank'] = df_s['score'].rank(method="min", ascending=False)
    ranking_message = "【今週の目標達成数ランキング】\n"
    for row in df_s.itertuples():
        rank = row.rank
        name = row.name
        score = row.score
        ranking_message += f"{str(int(rank))}位: {name}さん({str(int(score))}回)\n"
    df['score'] = 0
    generator.save()
    slack.chat.post_message(channel, ranking_message, as_user=True)
