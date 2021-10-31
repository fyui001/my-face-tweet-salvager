# my-fave-tweet-salvager

特定のアカウントの過去ツイートを全件取得します。
アカデミック版のtwitter api(v2)のキーが必要です。
取得した過去ツイートをDBに追加する機能も抱き合わせてます(CSVファイルにも将来対応予定)

# 前提条件

- git
- docker
- docker-compose

上記のソフトウェアが実行するマシンにインストールされていること。

# 準備体操

dotenvファイルをサンプルファイルからコピーして必要な値を入れる。

```shell
cp .env.example .env
```

調整したら、`docker-compose up -d` で各コンテナを起動させる。

# 基本的な使い方

- 立ち上げたappコンテナにログインする

```shell
docker-compose app exec bash
```

- ログインしたら、マイグレーション行いデータベースの準備をする。

```shell
db-migrate 
```

- あとは以下に上げるコマンドを実行して過去ツイートを取得し、DBに保存する。

```shell
# user-idは取得したいアカウントのIDに適宜書き換える
 python main.py --user-id=sunflower930316 --save-format=db
```

# 使い方(応用編)

本アプリケーション最低限のものしか用意してません。
保存するデータを変えるために、テーブル構造を変更するなど行う場合は本リポジトリをfork
して自分のええ塩梅になるようにソースコード・DBなどを書き換えてください。
