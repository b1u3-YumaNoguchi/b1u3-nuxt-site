from markdown.preprocessors import Preprocessor
import json
import boto3
import re

IMG_TMP = r'!\[(?P<alt>.*)\]\((?P<url>.*)\)'
BUCKET_NAME = 'blog.b1u3'
DEBUG = False

class UrlChanger(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.match(IMG_TMP, line)
            if m is not None:
                """
                # url だけでいいっぽい
                match_string = m.group('alt')
                """
                # <url>の処理
                match_string = m.group('url')
                splited = match_string.split('/')
                if not DEBUG:
                    s3 = boto3.resource('s3')
                # 怪しい実装
                    s3.Bucket(BUCKET_NAME).upload_file(match_string, splited[len(splited)-1], ExtraArgs={'ACL': 'public-read'})
                url = f'https://s3-ap-northeast-1.amazonaws.com/blog.b1u3/{splited[len(splited)-1]}'
                line = line.replace(match_string, url)
            new_lines.append(line)
        return new_lines
