from flask import Flask, render_template, request, redirect, url_for
from notion_api import query_database, get_page, append_text_block, extract_title

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        database_id = request.form["database_id"]
        return redirect(url_for("view_database", database_id=database_id))
    return render_template("index.html")

@app.route("/db/<database_id>")
def view_database(database_id):
    start_cursor = request.args.get("cursor")
    response = query_database(database_id, start_cursor)
    results = response["results"]

    for result in results:
        result["title_text"] = extract_title(result)

    return render_template(
        "database.html",
        database_id=database_id,
        data=response
    )

@app.route("/page/<page_id>", methods=["GET", "POST"])
def view_page(page_id):
    if request.method == "POST":
        text = request.form["text"]
        append_text_block(page_id, text)
        return redirect(url_for("view_page", page_id=page_id))

    page = get_page(page_id)
    return render_template("page.html", page=page)

if __name__ == "__main__":
    app.run(debug=True)
