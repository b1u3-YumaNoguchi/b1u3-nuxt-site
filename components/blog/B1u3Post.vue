<template>
  <div class="b1u3-blog-post pb-10">
    <p style="margin-bottom: 0px;">
      {{ date }}
    </p>
    <v-divider />
    <h3>
      <a @click="$router.push('/blog/'+id)">
        {{ title }}
      </a>
    </h3>
    <v-chip
      v-for="(category_id, ind) in $store.state.posts_with_key[id].categories"
      :key="ind"
      x-small
      :color="$store.state.categories[category_id].color"
      :text-color="$store.state.categories[category_id].text_color"
      class="ms-1"
    >
      {{ $store.state.categories[category_id].name }}
    </v-chip>
    <div v-html="content" />
    <v-row align="center" justify="center">
      <v-img
        src="https://s3-ap-northeast-1.amazonaws.com/blog.b1u3/5c51a0a6.jpg"
        max-width="300"
      />
    </v-row>
    <button>コメントを書く</button>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default () {
        return 'デフォルト記事名'
      }
    },
    content: {
      type: String,
      default () {
        return 'デフォルト記事内容'
      }
    },
    date: {
      type: String,
      default () {
        return 'YYYY-MM-DD'
      }
    },
    id: {
      type: String,
      default () {
        return '0'
      }
    }
  }
}
</script>
