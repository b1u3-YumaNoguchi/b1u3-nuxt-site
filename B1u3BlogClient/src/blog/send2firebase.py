import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from random import choice

class BlogClient():
    def __init__(self, path_to_json=None):
        if path_to_json is None:
            self.cred = credentials.Certificate('/Users/b1u3/b1u3-nuxt-site-6c4e7-firebase-adminsdk-l988c-ef29c27a55.json')
        else:
            self.cred = credentials.Certificate(path_to_json)
        # self.cred = credentials.Certificate(path_to_json)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.categories = dict()

    def get_categories(self):
        category_ref = self.db.collection('category').stream()
        self.categories = {}
        for doc in category_ref:
            self.categories[doc.id] = doc.to_dict()
        return self.categories

    def add_category(self, name):
        self.get_categories()
        # カテゴリーの中にあるか調べる
        for k, v in self.categories.items():
            if v['name'] == name:
                return False
        # なかったら、新しく作る
        category_ref = self.db.collection('category')
        payload = {}
        col, tcol = choice([('green', 'white'), ('red', 'white'), ('pink', 'white'), ('purple', 'white'), ('yellow', 'black'), ('indigo', 'white')])
        payload['color'] = col
        payload['text_color'] = tcol
        payload['name'] = name
        category_ref.add(payload)
        return True

    def category_to_key(self, categories):
        self.get_categories()
        ret = []
        for cat in categories:
            for k, v in self.categories.items():
                # TODO: 高速化
                if cat == v['name']:
                    ret.append(k)
                    sw = True
                    break
            else:
                raise Exception()
        return ','.join(ret)

    def add_post(self, data):
        n = datetime.datetime.now()
        data['date'] = f'{n.year}/{n.month:02}/{n.day:02}/{n.hour:02}/{n.minute:02}'
        blog_ref = self.db.collection('blog')
        blog_ref.add(data)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f'Usage: {__file__} [file_name]')
        sys.exit()
    client = BlogClient()
    f = open(sys.argv[1])
    # 記事のタイトルを保存する
    title = f.readline()
    title = title.strip()
    f.readline()
    # カテゴリーのキーを取る なかったら作る
    categories = f.readline()
    categories = list(map(lambda x: x.strip(), categories.split(',')))
    for cat in categories:
        client.add_category(cat)
    keys_of_categories = client.category_to_key(categories)
    f.readline()
    content = f.read()
    client.add_post({'title': title, 'category': keys_of_categories, 'content': content})
