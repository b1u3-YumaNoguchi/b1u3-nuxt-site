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
    <p> state: {{ $store.state }} </p>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data () {
    return {
      d: 1,
      users: []
    }
  },
  computed: { ...mapState(['counter']) },
  async fetch ({ store }) {
    await store.dispatch('set_message')
    await store.dispatch('get_updated_posts')
    await store.dispatch('get_posts')
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
