## GitHub Actions

このリポジトリは GitHub Actions の練習用に構成されており、Python スクリプトに対して構文チェック（flake8）を自動で行います。

`.github/workflows/python-app.yml` にて定義された CI パイプラインは、`push` および `pull_request` のたびに実行されます。

## ローカルで GitHub Actions を試す（`act` の使用）

GitHub Actions をリモートに push する前に、ローカルで挙動を確認したい場合は [nektos/act](https://github.com/nektos/act) を使うのが便利です。


## ファイル構成

|フォルダ名 |ファイル名 |説明                         |
|:--        |:--     |:--                       |
|stats_training |Scipy_stats_training_1      |This is an elementary statistical code.    |
|stats_training |Scipy_stats_training_2      |This is an elementary t_stat code.   |
|others |integral     |This is an elementary integral code.   |
