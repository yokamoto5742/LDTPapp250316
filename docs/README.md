# LDTPapp

このアプリケーションは、生活習慣病療養計画書を作成するための支援ツールです。患者情報を入力し、適切な主病名とシート名を選択することで、療養計画書のテンプレートを自動的に生成します。

## 特徴

- 患者情報の入力と管理
- 主病名とシート名に基づいた療養計画書のテンプレート生成
- 療養計画書の編集、保存、印刷
- 過去の療養計画書の履歴管理
- テンプレートのカスタマイズと保存
- バーコード自動生成機能
- エクスポート・インポート機能

## 使用方法

1. アプリケーションを起動します。
2. 患者IDを入力すると、関連する患者情報が自動的に読み込まれます。
3. 「新規作成」ボタンをクリックして、新しい療養計画書を作成します。
4. 主病名とシート名を選択し、達成目標、行動目標、食事、運動、その他の情報を入力します。
5. 「新規登録して印刷」ボタンをクリックして、療養計画書を生成して印刷します。
6. 生成された療養計画書は自動的に印刷されます。
7. 過去の療養計画書を編集するには、履歴一覧から対象の計画書をクリックします。
8. 必要に応じて療養計画書を編集し、「保存」ボタンをクリックして変更を保存します。
9. 「印刷」ボタンをクリックして、編集した療養計画書を印刷します。
10. 「削除」ボタンをクリックして、不要な療養計画書を削除します。

## テンプレートのカスタマイズ

1. 「テンプレート編集」ボタンをクリックして、テンプレート編集画面を開きます。
2. 主病名とシート名を選択し、テンプレートの内容を編集します。
3. 「保存」ボタンをクリックして、変更したテンプレートを保存します。

## データのエクスポート・インポート

1. 「設定」ボタンをクリックして設定画面を開きます。
2. 「CSV出力」ボタンでデータをCSVファイルにエクスポートできます。
3. 「CSV取込」ボタンで以前エクスポートしたデータをインポートできます。

## 動作環境

- Python 3.11 以上
- Flet フレームワーク 0.23.0
- SQLAlchemy 2.0.39 (データベース)
- Pandas 2.0.3 (データ処理)
- openpyxl 3.1.5 (Excelファイル操作)
- python-barcode 0.15.1 (バーコード生成)
- watchdog 4.0.2 (ファイル監視)
- pywin32 310 (Windowsファイル操作)

## インストール

1. リポジトリをクローンまたはダウンロードします。
2. 必要なPythonパッケージをインストールします。
   ```
   pip install -r requirements.txt
   ```
3. `config.ini`ファイルを編集し、データベースの接続情報とファイルパスを設定します。
4. アプリケーションを起動します。
   ```
   python main.py
   ```

## 設定ファイル (config.ini)

設定ファイルには以下の項目を含みます:
- データベース接続情報
- ウィンドウサイズ設定
- UI要素の高さ設定
- パス設定 (テンプレート、出力先など)
- ファイルパス設定
- バーコード設定

## 注意事項

- このアプリケーションは、医療従事者による適切な判断と監督の下で使用してください。
- 生成された療養計画書は、医療従事者が確認し、必要に応じて修正してください。
- データの機密性と安全性を確保するため、適切なセキュリティ対策を講じてください。
- アプリケーションはpat.csvファイルが存在するか監視しており、ファイルが削除されると自動的に終了します。

## ライセンス

このプロジェクトのライセンス情報については、LICENSEファイルを参照してください。

## 問い合わせ

質問やフィードバックがある場合は、[issues](https://github.com/yokamoto5742/LDTPapp/issues) ページからお問い合わせください。