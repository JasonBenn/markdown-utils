import os

from dotenv import load_dotenv
from instapaper import Instapaper as ipaper
# https://github.com/rsgalloway/instapaper
from slugify import slugify
from tqdm import tqdm

load_dotenv()
NOTES_ROOT = "/Users/jasonbenn/new-notes/exported/instapaper"

# TOS: Apps must not make multiple simultaneous requests to the Instapaper Mobilizer or the "Bookmarks: Get Text" method. Such requests must be performed in series, not in parallel. Requests to the Instapaper Mobilizer must only be made when the user has explicitly requested a page to be viewed, and may not be automatically bulk-loaded in advance or in the background.

i = ipaper(os.getenv("INSTAPAPER_KEY"), os.getenv("INSTAPAPER_SECRET"))
i.login(os.getenv("INSTAPAPER_EMAIL_ADDRESS"), os.getenv("INSTAPAPER_PASSWORD"))

bookmarks = i.bookmarks()
for mark in tqdm(bookmarks, desc="bookmarks"):
    assert mark.title
    slug = slugify(mark.title)
    filepath = os.path.join(NOTES_ROOT, slug)
    if not os.path.exists(filepath):
        open(filepath, "w").write(mark.text)
