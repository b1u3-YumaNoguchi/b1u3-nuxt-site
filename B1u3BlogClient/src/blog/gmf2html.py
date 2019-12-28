import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from b1u3markdown.urlchanger import UrlChanger
"""
入力するファイルのフォーマット
```
タイトル名
カテゴリー名(','区切り)
残りコンテンツ
```
"""


def generate():
    import sys
    if len(sys.argv) != 2:
        print('Using: gfm2html.py [GFM file name]', file=sys.stderr)
        sys.exit()
    f = open(sys.argv[1])
    title = f.readline()
    categories = f.readline()
    last = f.read()
    md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
    md.preprocessors['url_changer'] = UrlChanger(md)
    html = md.convert(last)
    return (title, categories, html)

if __name__ == '__main__':
    t, c, html = generate()
    print(t)
    print(c)
    print(html)

