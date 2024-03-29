import glob
import frontmatter
import yaml
import requests
from pyquery import PyQuery

glob_files = glob.glob(
    "/Users/benmatheja/OneDrive/Knowledge/Resources/books/*.md")


def resolve_genialokal_url(title, author):
    # print(title)
    # print(author)
    if (author):
        author = author[0]

    querydata = {"q[]": author + " " + title}
    url = 'https://www.genialokal.de/Suche/?q'
    r = requests.get(url, params=querydata, timeout=3)
    print(r.url)
    pq = PyQuery(r.text)
    # or     tag = pq('div.class')
    tag = pq('#pagebody > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > div.content.d-flex.flex-column.justify-content-between.flex-grow-1 > div.hgroup > h5 > a')
    book_link = tag.attr['href']
    try:
        print("Resolved " + title + " " + author + ' to ' +
              'https://www.genialokal.de' + book_link)
    except:
        print("could not resolve book with " + author + " " + title)

    if (book_link):
        return "https://www.genialokal.de" + tag.attr['href']
    else:
        return resolve_genialokal_url(title, "")


data = []
for p in glob_files:
   # print(p)
    # print(frontmatter.load(p).metadata)
    book = frontmatter.load(p).metadata
    if 'tag' in book:
        del book['tag']
    if 'tags' in book:
        del book['tags']
    if 'isbn' in book:
        del book['isbn']
    if 'created' in book:
        del book['created']
    if 'updated' in book:
        del book['updated']
    if 'publisher' in book:
        del book['publisher']
    if 'publish' in book:
        del book['publish']
    if 'cover' in book:
        del book['cover']
    book['link'] = resolve_genialokal_url(book['title'], book['author'])
    data.append(book)

with open('_data/obsidianbooks.yml', 'w', encoding='UTF-8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False,
              encoding="utf-8", allow_unicode=True)
