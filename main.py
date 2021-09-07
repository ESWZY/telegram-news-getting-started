import hashlib
import json
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from telegram_news.template import InfoExtractorJSON, NewsPostmanJSON
from telegram_news.utils import xml_to_json

bot_token = os.getenv("TOKEN")
channel = os.getenv("CHANNEL")
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
db = Session(bind=engine.connect())

url = "https://www.scmp.com/rss/91/feed"
tag = "SCMP"
table_name = "scmpnews"

ie = InfoExtractorJSON()

# Pre-process the XML string, convert to JSON string
def list_pre_process(text):
    text = json.loads(xml_to_json(text))
    return json.dumps(text)
ie.set_list_pre_process_policy(list_pre_process)

# Route by key list
ie.set_list_router(['rss', 'channel', 'item'])
ie.set_link_router(['link'])
ie.set_title_router(['title'])
ie.set_paragraphs_router(['description'])
ie.set_time_router(['pubDate'])
ie.set_source_router(['author'])
ie.set_image_router(['media:thumbnail', '@url'])

# Customize ID for news item
def id_policy(link):
    return hashlib.md5(link.encode("utf-8")).hexdigest()
ie.set_id_policy(id_policy)

np = NewsPostmanJSON(listURLs=[url], sendList=[channel], db=db, tag=tag)
np.set_extractor(ie)
np.set_table_name(table_name)
np.poll()
