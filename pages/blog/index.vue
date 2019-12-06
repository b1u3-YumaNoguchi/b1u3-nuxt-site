<template>
  <div>
    <b1u3-updated-post-list />
    <hr>
    <b1u3-posts />
  </div>
</template>

<script>
import B1u3Posts from '@/components/blog/B1u3Posts.vue'
import B1u3UpdatedPostList from '@/components/blog/B1u3UpdatedPostList.vue'

export default {
  components: {
    B1u3Posts,
    B1u3UpdatedPostList
  }
}
</script>
