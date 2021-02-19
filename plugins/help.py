from slackbot.bot import listen_to


@listen_to(r'^/help')
def mention_func(message):
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
