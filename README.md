# 技術課題　説明

## 動作環境
- PC: macOS Ventura 13.6.4
- Docker Desktop for Mac: ver4.28.0
- Python: ver3.8.17
- フレームワーク: Flask 3.0.2
- MySQL: ver8.3.0
- Pythonパッケージ: requirements.txt 参照

## 実行手順
1. 事前準備
   1. Dockerイメージ構築  
      ```docker compose build```
   2. Dockerコンテナ作成・起動  
      ```docker compose up -d```
2. ブラウザでアプリ表示
   - http://localhost:8000/
3. 画像パス欄を入力し、解析ボタン押下
4. 処理結果を確認
5. 事後作業
   - Dockerコンテナ停止・削除  
     ```docker compose down```
