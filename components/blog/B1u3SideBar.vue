<template>
  <div>
    <h2>
      プロフィール
    </h2>
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
    <h2>
      ツイッターのTL
    </h2>
    <v-row justify="center">
      <a class="twitter-timeline" data-width="300" data-height="400" href="https://twitter.com/star_owl_main?ref_src=twsrc%5Etfw">Tweets by star_owl_main</a>
      <script async src="https://platform.twitter.com/widgets.js" charset="utf-8" />
    </v-row>
    <h2>
      カテゴリー
    </h2>
    <v-simple-table dense fixed-header>
      <thead>
        <tr>
          <th class="text-center">
            Name
          </th>
          <th class="text-center">
            Count
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-center">
            <v-chip small color="red" text-color="white">
              カテゴリー1
            </v-chip>
          </td>
          <td class="text-center">
            1
          </td>
        </tr>
        <tr>
          <td class="text-center">
            <v-chip small color="green" text-color="white">
              カテゴリー2
            </v-chip>
          </td>
          <td class="text-center">
            2
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
export default {
}
</script>
