<template>
  <div>
    <h1>
      Vue 自体のサンプル
    </h1>
    <p>{{ d }}</p>
    <h1>
      nuxt-fireのサンプル
    </h1>
    <v-btn @click="readFromFirestore()">
      Get message
    </v-btn>
    <ul>
      <li v-for="(name, index) in users" :key="index">
        {{ name }}
      </li>
    </ul>
    <v-btn @click="getUsers()">
      Get Users
    </v-btn>
    <h1>
      Vuex のサンプル
    </h1>
    <p>Count: {{ counter }}</p>
    <v-btn @click="$store.dispatch('increment')">
      increment
    </v-btn>
    <p> $store.state: </p>
    <table style="border: solid 1px #333">
      <tr>
        <th style="border: solid 1px #333">
          KEYS
        </th>
        <th style="border: solid 1px #333">
          VALUES
        </th>
      </tr>
      <tr v-for="(value, key) in $store.state" :key="key" style="border: solid 1px #333">
        <th style="border: solid 1px #333">
          {{ key }}
        </th>
        <th style="border: solid 1px #333">
          {{ value }}
        </th>
      </tr>
    </table>
    <h3>
      rawHtmlのサンプル
    </h3>
    <div v-html="rawHtml" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data () {
    return {
      d: 1,
      users: [],
      rawHtml: '<p>Using v-html directive: <span style="color:red">This should be red.</span></p>'
    }
  },
  computed: { ...mapState(['counter']) },
  async fetch ({ store }) {
    await store.dispatch('set_message')
    await store.dispatch('get_updated_posts')
    await store.dispatch('get_posts')
    await store.dispatch('get_posts_with_key')
    await store.dispatch('get_categories')
  },
  methods: {
    async readFromFirestore () {
      const messageRef = this.$fireStore.collection('message').doc('message')
      try {
        const messageDoc = await messageRef.get()
        alert(messageDoc.data().message)
      } catch (e) {
        alert(e)
      }
    },
    async getUsers () {
      const collectionRef = this.$fireStore.collection('users')
      const querySnapshot = await collectionRef.get()
      alert(querySnapshot.size)
      this.users.splice(0)
      for (const doc of querySnapshot.docs) {
        this.users.push(doc.get('name'))
      }
    }
  }
}
</script>
