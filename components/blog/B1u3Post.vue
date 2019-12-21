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
    <v-chip x-small color="red" text-color="white">
      カテゴリー1
    </v-chip>
    <v-chip x-small color="green" text-color="white">
      カテゴリー2
    </v-chip>
    <p>
      {{ content }}
    </p>
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
