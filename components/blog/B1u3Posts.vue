<template>
  <div>
    <h1>
      POSTS
    </h1>
    <b1u3-post />
    <b1u3-post
      v-for="(post, id) in $store.state.posts_with_key"
      :id="id"
      :key="id"
      :title="post.title"
      :content="post.content"
      :date="post.date"
    />
  </div>
</template>

<script>
import B1u3Post from '@/components/blog/B1u3Post.vue'
export default {
  components: {
    B1u3Post
  }
}
</script>
