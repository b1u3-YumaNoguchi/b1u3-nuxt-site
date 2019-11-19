<template>
  <v-app>
    <v-content class="pt-3 b1u3-site">
      <v-container class="b1u3-blog-container">
        <v-row>
          <v-col class="flex-grow-1">
            <h1>
              TITLE
            </h1>
            <hr>
            <h1>
              UPDATED
            </h1>
            <v-simple-table dense fixed-header class="mb-2" style="border: thin solid;">
              <thead>
                <tr>
                  <th class="text-left">
                    Updated&nbsp;Posts
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    Updated&nbsp;post1
                  </td>
                </tr>
                <tr>
                  <td>
                    Updated&nbsp;post2
                  </td>
                </tr>
                <tr>
                  <td>
                    Updated&nbsp;post3
                  </td>
                </tr>
              </tbody>
            </v-simple-table>
            <hr>
            <h1>
              POSTS
            </h1>
            <!-- ここから for で回す -->
            <div class="b1u3-blog-post">
              <p style="margin-bottom: 0px;">
                YYYY-MM-DD
              </p>
              <v-divider />
              <h3>
                最新ブログ1
              </h3>
              <v-chip x-small color="red" text-color="white">
                カテゴリー1
              </v-chip>
              <v-chip x-small color="green" text-color="white">
                カテゴリー2
              </v-chip>
              <p>ブログ内容</p>
              <button>コメントを書く</button>
            </div>
            <!-- ここまで for する -->
            <div class="b1u3-blog-post pt-10">
              <p style="margin-bottom: 0px;">
                YYYY-MM-DD
              </p>
              <v-divider />
              <h3>
                最新ブログ2
              </h3>
              <v-chip x-small color="red" text-color="white">
                カテゴリー1
              </v-chip>
              <v-chip x-small color="green" text-color="white">
                カテゴリー2
              </v-chip>
              <p>ブログ内容</p>
              <button>コメントを書く</button>
            </div>
          </v-col>
          <v-col cols="4" class="hidden-sm-and-down">
            <h1>
              プロフィール
            </h1>
            <!-- 遅延読み込みの v-img は、自前のassetsから参照できない -->
            <!--
            <v-img
              src="/assets/syoumeisyashin_man.png"
            >
            </v-img>
            -->
            <!-- html 側に、width, height を書くとそっちに調整される。縦横も維持されない -->
            <v-row justify="center">
              <img
                src="@/assets/syoumeisyashin_man.png"
                style="height: 150px;"
              >
            </v-row>
            <p>えぬわいっていいます。技術ブログやってます。</p>
            <v-text-field
              placeholder="SEARCH"
              append-icon="mdi-magnify"
            />
            <hr>
            <h1>
              ツイッターのTL
            </h1>
            <h1>
              カテゴリー
            </h1>
            <v-chip small color="red" text-color="white">
              カテゴリー1
            </v-chip>
            <v-chip small color="green" text-color="white">
              カテゴリー2
            </v-chip>
            <!-- ここに 1 * 3 の画像リスト置く -->
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
}
</script>

<style lang="scss">
.b1u3-site {
  background:
    linear-gradient(135deg, #A8B1BB 22px, #ffffff 22px, #ffffff 24px, transparent 24px, transparent 67px, #ffffff 67px, #ffffff 69px, transparent 69px),
    linear-gradient(225deg, #A8B1BB 22px, #ffffff 22px, #ffffff 24px, transparent 24px, transparent 67px, #ffffff 67px, #ffffff 69px, transparent 69px)0 64px;
  background-color:#A8B1BB;
  background-size: 64px 128px;
  /* scss で書いてみる */
}
.b1u3-blog-container {
  background-color: #ffffff;
  border-radius: 10px;
}
</style>
