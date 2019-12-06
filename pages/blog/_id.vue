<template>
  <b1u3-post />
</template>

<script>
import B1u3Post from '@/components/blog/B1u3Post.vue'

export default {
  validate ({ params }) {
    // URL のバリデーション
    return /^\d+$/.test(params.id)
  },
  components: {
    B1u3Post
  }
}
</script>
