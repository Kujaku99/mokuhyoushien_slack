from slackbot.bot import listen_to
from plugins.users_df import DFGenerator
import numpy as np


@listen_to('/')
def mention_func(message):
    rows = message.body['text']
    user = message.body['user']
    rows_list = rows.split('\n')
    for row in rows_list:

        #ユーザー登録
        if row.startswith('/register '):
            generator = DFGenerator()
            df = generator.df
            temp, name = row.split(None, 1)
            users_list = df.index.values.tolist()
            if user in users_list:
                old_name = df.at[user, 'name']
                message.reply(f"{old_name}さんは既に登録されています。名前を{name}に変更しました。", in_thread=True)
                df.at[user, 'name'] = name
            else:
                df.at[user] = [name, np.NaN, 0]
                message.reply(f"{name}さんを登録しました。", in_thread=True)
            generator.save()

        #目標達成
        if row.startswith('/finish'):
            generator = DFGenerator()
            df = generator.df
            if user in df.index.values:
                df.at[user, 'score'] += 1
                goal = df.at[user, 'goal']
                if type(goal) is str:
                    message.reply(f"「{goal}」を達成しました！お疲れ様です！！今週の目標達成数は{str(int((df.at[user, 'score'])))}です！",
                                  in_thread=True)
                    df.at[user, 'goal'] = np.NaN
                else:
                    message.reply(f"目標が登録されていません...それはともかくお疲れ様です！！今週の目標達成数は{str(int((df.at[user, 'score'])))}です！",
                                  in_thread=True)
                generator.save()
            else:
                message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。", in_thread=True)

        #目標未達成
        if row.startswith('/failed'):
            generator = DFGenerator()
            df = generator.df
            if user in df.index.values:
                goal = df.at[user, 'goal']
                if type(goal) is str:
                    df.at[user, 'goal'] = np.NaN
                    message.reply(f"「{goal}」を達成できませんでした...次は頑張ろう！", in_thread=True)
                    generator.save()
                else:
                    message.reply(f"目標が設定されていません...それはともかく次は頑張ろう！", in_thread=True)

            else:
                message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。", in_thread=True)

        #目標設定
        if row.startswith('/start '):
            temp, goal = row.split(None, 1)
            generator = DFGenerator()
            df = generator.df
            if user in df.index.values:
                df.at[user, 'goal'] = goal
                message.reply(f"目標を「{goal}」に設定しました。頑張って下さい！！", in_thread=True)
                generator.save()
            else:
                message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。", in_thread=True)

        #ヘルプを表示
        if row.startswith('/help'):
            message.reply(f"\n【取扱説明書】\n"
                          f"①「 /register ユーザー名(任意)」でユーザー登録をする\n"
                          f"②「 /start 目標(任意)」で今日or明日の目標を設定\n"
                          f"③目標達成出来たら「 /finish」で報告(目標達成数が+1)\n"
                          f"　目標達成出来なかったら「 /failed」で報告\n"
                          f"④日曜日に全登録ユーザーのその週の目標達成数ランキングが配信されます\n"
                          f"----------------------------------------------------\n"
                          f"【コマンド一覧】\n"
                          f" (/の前にスペースが必要です)\n"
                          f" /help ... 取扱説明書とコマンド一覧を表示\n"
                          f" /register ユーザー名(任意) ... ユーザー登録(2回目以降はユーザー名変更)\n"
                          f" /start 目標(任意) ... 目標設定\n"
                          f" /finish ... 目標達成(達成回数+1)\n"
                          f" /failed ... 目標未達成(達成回数は変化なし)\n"
                          f" /score ... 目標達成回数を確認\n"
                          f" /ranking ... 今週の達成数ランキング\n"
                          f" /unregister ... ユーザー登録解除",
                          in_thread=True)

        #ランキングを表示
        if row.startswith('/ranking'):
            generator = DFGenerator()
            df = generator.df
            df_s = df.sort_values('score', ascending=False)
            df_s['rank'] = df_s['score'].rank(method="min", ascending=False)
            ranking_message = "\n【今週の目標達成数ランキング】\n"
            for user_row in df_s.itertuples():
                rank = user_row.rank
                name = user_row.name
                score = user_row.score
                ranking_message += f"{str(int(rank))}位: {name}さん({str(int(score))}回)\n"
            message.reply(ranking_message, in_thread=True)

        #目標達成数を表示
        if row.startswith('/score'):
            generator = DFGenerator()
            df = generator.df
            if user in df.index.values:
                message.reply(f"今週の目標達成数は{str(int(df.at[user, 'score']))}です。", in_thread=True)
            else:
                message.reply("まずは「 /register ユーザー名」でユーザー登録をして下さい。", in_thread=True)

        #登録解除
        if row.startswith('/unregister'):
            generator = DFGenerator()
            df = generator.df
            if user in df.index.values:
                name = df.at[user, 'name']
                message.reply(f"{name}さんのユーザー登録を解除しました。", in_thread=True)
                df.drop(user, axis=0, inplace=True)
                generator.save()

            else:
                message.reply("ユーザー登録されていません。", in_thread=True)