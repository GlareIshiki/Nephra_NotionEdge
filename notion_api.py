
import os
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()
notion = Client(auth=os.getenv("NOTION_TOKEN"))

def convert_to_uuid(base62_id: str) -> str:
    if "-" in base62_id:
        return base62_id
    return f"{base62_id[0:8]}-{base62_id[8:12]}-{base62_id[12:16]}-{base62_id[16:20]}-{base62_id[20:32]}"

def query_database(database_id, start_cursor=None, page_size=100):
    database_id = convert_to_uuid(database_id)
    return notion.databases.query(
        database_id=database_id,
        start_cursor=start_cursor,
        page_size=page_size
    )

def get_page(page_id):
    page_id = convert_to_uuid(page_id)
    return notion.pages.retrieve(page_id=page_id)

def append_text_block(page_id, text):
    page_id = convert_to_uuid(page_id)
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": text}
                        }
                    ]
                }
            }
        ]
    )

def extract_title(page, prop_name="タイトル"):
    props = page["properties"]
    if prop_name not in props:
        return "（無題）"

    title_data = props[prop_name].get("title", [])
    texts = []

    for part in title_data:
        if "plain_text" in part:
            texts.append(part["plain_text"])

    return "".join(texts) if texts else "（無題）"