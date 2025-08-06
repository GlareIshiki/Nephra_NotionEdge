# Nephra_NotionEdge

ブラウザが "/" にアクセス
↓ （GET）
Flaskは index.html を返す
↓
ユーザーがフォームを入力 → 送信
↓ （POST）
Flaskの同じ "/" に POSTリクエストが飛ぶ
↓
request.method == "POST" の処理が実行される
↓
Notionにデータ送信 → 結果を表示

GET：お店に行って「メニュー見せてください」→ メニュー（index.html）をもらう
POST：そのメニューに「このパフェください！」って注文を書く → お店が注文受け取って（Notionに）届ける