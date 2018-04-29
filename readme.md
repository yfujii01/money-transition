# money-transition

資産の遷移を記録する

## 利用方法

1. cp config.json_sample config.json

1. config.jsonにマネーフォワードのidとpasswordを入力

1. pip install selenium

1. chrome driverインストール
    1. wget http://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
    1. unzip chromedriver_linux64.zip
    1. sudo mv chromedriver /usr/local/bin
    1. rm chromedriver_linux64.zip

1. mkdir data

1. python init.py

## 結果

dataフォルダに日付付きで出力される