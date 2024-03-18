# テスト課題　説明

## 実行環境
- PC: macOS Ventura 13.6.4
- Python: ver3.8.2
- フレームワーク: Flask 3.0.2
- MySQL: ver8.3.0
- Pythonパッケージ: requirements.txt 参照

## 実行手順
1. 事前準備
   1. venv 仮想環境の有効化
      - ```source invox/bin/activate```
   2. MySQL サーバー起動
      - ```mysql.server start```
   3. Flask アプリサーバー起動
      - ```python analyze.py```
2. ブラウザでアプリ表示
   - http://127.0.0.1:5000
3. 画像パス欄を入力し、解析ボタン押下
4. 処理結果を確認
5. 事後作業
   1. Flask アプリサーバー停止
      - CTRL+C キー押下
   2. MySQL サーバー停止
      - ```mysql.server stop```
   3. venv 仮想環境の無効化
      - ```deactivate```
