#!/usr/bin/env python
# -*- coding: utf8 -*-
# import System
# import clr
import re


def intercept(message, user_name, bits, subscription_month_count, is_subscription, bot_name):
    # ==========================================
    # 受信したとき (on Receive)
    # ==========================================
    # ※適時仕様を変える場合があります
    #
    # message  : 受信した文字 (Receive message)
    # user_name : ユーザID     (user_name)
    # bits     : ドネート額   (bits >  Twitch : points / Youtube : $ )
    # subscription_month_count  : サブスク継続月数 ( subscription_month_count > Twitch / Youtubeの場合はTier数を返します)
    # is_subscription     : サブスク継続中か？ ( is_subscription? > Twitch / Youtubeの場合は、チャットスポンサーか？を返します)
    # bot_name  : 投稿者がBOTを使っていた場合のクライアント名（bot_name > Twitch)
    #
    # Return Value:
    #  書き換え後の文字　(Modified message)
    # 

    # 他にも、動的に送ることができるコマンドあり。
    # ただし、ループするとフリーズしたりBANされるので注意。
    # 先頭に無視されるコマンドなどをいれて、通信がループしないように。

    # Variables----------------------------------------------------------------------------------
    # OriginalText       : 母国語テキスト枠 (Native inputbox)   .... Windows.Forms.TextBox object.
    # TranslatedText     : 翻訳語テキスト枠 (Translated inputbox)... Windows.Forms.TextBox object.
    # ToDiscordText      : テキスト枠       (to Discord inputbox)... Windows.Forms.TextBox object.
    # SendOriginalText   : 翻訳送信処理     (Send message with Native text)
    # SendTranslatedText : 翻訳送信処理     (Send message with Translated text)
    # SendTextToDiscord  : 送信処理         (Send message to Discord)
    #
    # Send～は、.Textに 'go' を代入したときに処理される
    # ↑ここまでテンプレ

    if user_name in ['StreamLabs', 'NightBot', 'StreamElements']:
        send_event_response_message(message, bits)

    send_multilingual_message(message)
    return message


def send_event_response_message(message, bits):
    command_so = '!so'
    if command_so in message:
        return

    # Streamlabsで設定した文章に変更する
    follow_keyword = 'さん、フォローありがとうございます。　呼ばれたいニックネームがあればチャットで教えてください(/･ω･)/'
    raid_keyword = 'さんレイドありがとうございます(/･ω･)/'
    bits_keyword = 'さん' + str(int(bits)) + 'Bitsありがとうございます(/･ω･)/'
    host_keyword = 'さんによってホストされました(/･ω･)/'
    subscription_keyword = 'さんサブスクありがとうございます(/･ω･)/'
    subscription_gift_keyword = 'さんサブスクギフトありがとうございます(/･ω･)/'

    original_text = ''
    if follow_keyword in message:
        follow_user_name = message.replace(follow_keyword, '')
        original_text = ''
    elif raid_keyword in message:
        raid_user_name = message.replace(raid_keyword, '')
        original_text = command_so + ' ' + raid_user_name
    elif bits_keyword in message:
        bits_user_name = message.replace(bits_keyword, '')
        original_text = ''
    elif host_keyword in message:
        host_user_name = message.replace(host_keyword, '')
        original_text = ''
    elif subscription_keyword in message:
        subscription_user_name = message.replace(subscription_keyword, '')
        original_text = ''
    elif subscription_gift_keyword in message:
        subscription_gift_user_name = message.replace(subscription_gift_keyword, '')
        original_text = ''

    if original_text != '':
        OriginalText.Text = original_text
        SendOriginalText.Text = 'go'


def send_multilingual_message(message):
    # En以外の言語も同時に送信したい場合
    country_codes = ['kr']
    for country_code in country_codes:
        # ここに処理追加
        continue


def test_intercept():
    # pytestで挙動確認用。自分のTwitchユーザー名等入れる
    user_name = ''

    intercept(user_name + 'さんレイドありがとうございます(/･ω･)/', 'Streamlabs', '', '', '', '')
