from flask import Flask, render_template, request
from notion_client import Client
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# Flaskアプリの初期化
app = Flask(__name__)

# Notion APIのクライアント初期化
notion = Client(auth=os.getenv("NOTION_TOKEN"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        page_id = request.form["page_id"]
        text = request.form["text"]

        # Notionページにブロックを追加
        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {"type": "text", "text": {"content": text}}
                        ]
                    }
                }
            ]
        )
        return f"ページ {page_id} に追加しました！"

    return render_template("index.html")

# アプリを実行（開発モード）
if __name__ == "__main__":
    app.run(debug=True)
