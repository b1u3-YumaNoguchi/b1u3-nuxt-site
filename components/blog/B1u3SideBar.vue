<template>
  <div>
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
