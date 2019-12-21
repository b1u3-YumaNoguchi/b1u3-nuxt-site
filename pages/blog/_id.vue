<template>
  <b1u3-post :id="$route.params.id" :title="title" :content="content" :date="date" />
</template>

<script>
import B1u3Post from '@/components/blog/B1u3Post.vue'

export default {
  validate ({ params, store }) {
    // URL のバリデーション
    // return /^\d+$/.test(params.id)
    // priority queue が使える
    // console.log('posts_with_key: ', store.state.posts_with_key)
    return store.state.keys.includes(params.id)
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
