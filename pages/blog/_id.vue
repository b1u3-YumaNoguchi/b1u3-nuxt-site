<template>
  <b1u3-post :title="title" :content="content" :date="date" />
</template>

<script>
import B1u3Post from '@/components/blog/B1u3Post.vue'

export default {
  validate ({ params, store }) {
    // URL のバリデーション
    // return /^\d+$/.test(params.id)
  /*
    console.log('includes: ', store.state.keys.includes(params.id))
    console.log(store.state.keys)
    console.log('counter: ', store.state.counter)
    for (const k in store.state.keys) {
      if (k === params.id) {
        return true
      }
    }
    return false
  */
    // console.log('keys: ', store.state.abc)
    // return store.state.keys(key => key === params.id)
    return true
  },
  components: {
    B1u3Post
  },
  computed: {
    blog_key () {
      return this.$route.params.id
    },
    title () {
      return this.$store.state.posts_with_key[this.$route.params.id].title
    },
    content () {
      return this.$store.state.posts_with_key[this.$route.params.id].content
    },
    date () {
      return this.$store.state.posts_with_key[this.$route.params.id].date
    }
  }
}
</script>
