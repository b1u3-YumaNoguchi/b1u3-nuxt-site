import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
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
    html = markdown.markdown(last,
                             extensions=[GithubFlavoredMarkdownExtension()])
    return (title, categories, html)

if __name__ == '__main__':
    t, c, html = generate()
    print(t)
    print(c)
    print(html)

