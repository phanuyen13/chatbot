import openai
from docopt import docopt

class AIChat:
    def __init__(self):
        openai.api_key = ''

    def response(self, user_input):
        # openai の GPT-3 モデルを使って、応答を生成する
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=1024,
            temperature=0.5,
        )

        return response['choices'][0]['text']

def main():

    __doc__ = """
Usage:
    chatbot.py --chat

    """

    args = docopt(__doc__)
    # print(args)

    if args['--version']:
        print('AIChat 1.0')
        return

    if args['--chat']:
        # AIChat のインスタンスを作成する
        chatai = AIChat()

        print('>> AIChat: こんにちは、私はchatbotです。')

        while True:
            # ユーザーからの入力を受け取る
            user_input = input('>> User: ')

            # ユーザーからの入力が「終了」だった場合、終了する
            if user_input == '終了':
                break

            # chataiからの応答を取得する
            response = chatai.response(user_input)
            print('>> AIChat: ' + response)

        print('>> AIChat: いつでもお話ししてくださいね。')


if __name__ == '__main__':
    main()
