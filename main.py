import argparse

def main():

    # コマンドライン引数の設定と取得
    parser = argparse.ArgumentParser(
        'get all tweet', usage='python main.py --user-id=sunflower930316 --save-format=db|csv'
    )

    # ユーザーIDを取得する引数設定
    parser.add_argument(
        '--user-id',
        help='取得したいツイッターアカウントのユーザーIDを指定する。高田憂希のツイートを取得した場合は[sunflower930316]',
        type=str,
        required=True,
    )

    # 保存するフォーマットを指定する引数の指定
    parser.add_argument(
        '--save-format',
        help='保存するフォーマットを指定する。データベースに保存したい場合は[db]、CSV形式でファイル出力したい場合は[csv]',
        type=str,
        required=True,
    )

    args = parser.parse_args()
    userId = args.user_id
    saveFormat = args.save_format
    print(args)

    print('高田憂希しか好きじゃない')

if __name__ == '__main__':
    main()