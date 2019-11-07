<template>
  <v-app>
    <v-content class="pt-3 b1u3-site">
      <v-container class="b1u3-blog-container">
        <h1>
          TITLE
        </h1>
        <hr>
        <h1>
          UPDATED
        </h1>
        <!-- ここに 1 * 3 の画像リスト置く -->
        <hr>
        <h1>
          POSTS
        </h1>
        <!-- ここから for で回す -->
        <p>YYYY-MM-DD</p>
        <hr>
        <h3>
          最新ブログ1
        </h3>
        <p>ブログ内容</p>
        <button>コメントを書く</button>
        <!-- ここまで for する -->
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
