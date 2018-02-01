# 社畜丼-外部DB --secondondb--
ローカルタイムライン(LTL)を取得してきて保存します。  
取得と同時に外部のBOTなどにLTLの更新を通知する機能も付ける。 
通知先管理用のポータルも作る。  
ポータル用の丼認証機能も付ける。  

## 雑な設計
 - (ストリーム取得鯖)丼に接続し、ストリームを流してもらう  
 - (同)ハートビート最終確認時刻を変数に保存  
 - (同)update 又はdelete受信時、DBを更新する  
 - (DB)更新をhook送信鯖に更新を通知  
 - (hook送信鯖)DBからの通知を受信  
 - (同)hook先登録DBからhook先一覧取得  
 - (同)toot情報を暗号化し、hook先にpost送信  
 - (hook受信側システム)受信したデータを復号し、利活用  

## システム構成
 - **INTAKE** 70%  
    ストリーム取得サーバ  
    + 丼に接続し、ストリーミングAPIにより、データを受信する  
    + 受信したデータを元に、DBの更新を行う  
    + 複数台同時起動し、接続障害に備える
 - **BUCKET** 0%  
    DBサーバ  
    + statusなど、公開情報を保存するDB
    + DB更新時にSPRINKLERに通知する機能を有する  
    + 後々、Active-Standby構成や、負荷分散に対応する
 - **SPRINKLER** 0%  
    Hook送信サーバ  
    + BUCKETに常時接続し、DB更新時に登録済みのHook先にeventとidをPOSTする　 
    + 送信元を証明するため、何らかのトークンを付与する
 - **LADLE** 0%  
   DBアクセスAPIサーバ  
   + 他システムからの要求に応じ、jsonデータを返す  
   + BULBのユーザー認証機能を使用し、ユーザー認証を行う  
   + 後々、検索機能も追加する
 - **BULB** 0%  
   認証サーバ  
   + 各サーバからの認証要求に応答する  
   + 丼に登録しているユーザーかどうか認証する
   + TANKに保存された公開鍵を用いて署名の暗号化が行える
 - **TANK** 0%  
   機密管理サーバ  
   + システム内部で扱う機密データなどを保存する  
   + 全てのデータを暗号化する
 - **RECEPTOR** 0%  
   登録ユーザポータル  
   + 統合基盤使用登録作業を行う
 - **CONTROLER** 0%
   管理者ポータル  
