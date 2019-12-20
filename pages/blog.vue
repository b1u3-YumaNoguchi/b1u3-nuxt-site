<template>
  <v-container class="b1u3-blog-container">
    <v-row>
      <v-col class="flex-grow-1">
        <h1>
          TITLE
        </h1>
        <hr>
        <nuxt-child />
      </v-col>
      <v-col cols="4" class="hidden-sm-and-down">
        <b1u3-side-bar />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import B1u3SideBar from '@/components/blog/B1u3SideBar.vue'

export default {
  components: {
    B1u3SideBar
  },
  async fetch ({ store }) {
    await store.dispatch('get_updated_posts')
    // await store.dispatch('get_posts')
    await store.dispatch('get_posts_with_key')
  }
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
