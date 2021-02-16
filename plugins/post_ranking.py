from slacker import Slacker
import slackbot_settings
from plugins.users_df import users_df


def post_ranking():
    slack = Slacker(slackbot_settings.API_TOKEN)
    channel = 'pj_みんなで応援チャンネル'
    users_df_s = users_df.sort_values('score', ascending=False)
    users_df_s['rank'] = users_df_s['score'].rank(method="min", ascending=False)
    ranking_message = "【今週の目標達成数ランキング】\n"
    for row in users_df_s.itertuples():
        rank = row.rank
        name = row.name
        score = row.score
        ranking_message += f"{str(int(rank))}位: {name}さん({str(int(score))}回)\n"
    users_df['score'] = 0
    slack.chat.post_message(channel, ranking_message, as_user=True)
