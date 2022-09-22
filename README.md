# 概要
[AtCoder](https://atcoder.jp/?lang=ja)の挑戦ログ

提出結果は各コンテストからしか参照できないので、ここに残すことで自身でも参照可能にする

# VSCodeで完結させるやり方
[online-judge-tools/oj](https://github.com/online-judge-tools/oj) を導入し、VSCode内でテストできるようにする

## 0.拡張の導入
`pip install online-judge-tools`

## 1.コンテストディレクトリ、および、各問題のディレクトリの作成
`各コンテスト/問題`のような構造でディレクトリを作ると、各テストケースを管理しやすいので楽

例：ABC158のC問題に挑戦する時のディレクトリ
`mkdir -p ABC/158/C`

## 2.ディレクトリの移動
コマンドを実行すると直下のファイルを見にいくので、先ほど作成したディレクトリに移動しておく
`cd ABC/158/C`

## 3.テストケースのダウンロード
下記コマンドでダウンロード可能
`oj download 問題のURL`

例：ABC158のC問題テストケースを取得する場合
`oj download https://atcoder.jp/contests/abc158/tasks/abc158_c`

上記コマンドを実施すると、コマンドを実行したディレクトリ直下に`test`ディレクトリとテストケースが記載された`sample` ファイルが作成される

## 4.スクリプトの作成
問題に沿ったスクリプトを作成しよう

例：`script.py`というpythonスクリプトを編集する
`vim script.py`

## 5.作成したスクリプトのテスト実行
下記コマンドでテストを実行できる
`oj t -c "言語 プログラムファイル"`

**※コマンドを実行した配下に存在する`test`ディレクトリを見に行ってテストするため、`test`ディレクトリがないと失敗する！**

例：pythonのプログラムを実行する場合
`oj t -c "python script.py"`
