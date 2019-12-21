import Vue from 'vue'
export const state = () => ({
  counter: 0,
  updated_posts: [],
  posts: [],
  posts_with_key: {},
  // ブログのキー: チェック params のチェックで使用するやつ
  keys: [],
  message: ''
})

// mutations は store の state を変える関数群
export const mutations = {
  increment (state) {
    state.counter++
  },
  set_message (state, msg) {
    state.message = msg
  },
  updated_posts_push (state, name) {
    state.updated_posts.push(name)
  },
  posts_push (state, post) {
    const date = post.date.toDate()
    const hours = date.getHours()
    const minutes = date.getMinutes()
    const formattedDate = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}`
    state.posts.push({ title: post.title, content: post.content, date: formattedDate })
  },
  posts_push_with_key (state, payload) {
    const date = payload.post.date.toDate()
    const hours = date.getHours()
    const minutes = date.getMinutes()
    const formattedDate = `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} ${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}`
    Vue.set(state.posts_with_key, payload.key, { title: payload.post.title, content: payload.post.content, date: formattedDate })
    state.keys.push(payload.key)
  }
}

// actions 内では commit を用いて mutation を呼び出す
export const actions = {
  increment (context) {
    context.commit('increment')
  },
  async set_message ({ commit }, msg) {
    const messageRef = this.$fireStore.collection('message').doc('message')
    try {
      const messageDoc = await messageRef.get()
      commit('set_message', messageDoc.data().message)
    } catch (e) {
      alert(e)
    }
  },
  async get_updated_posts ({ commit }) {
    const updatedPostsRef = this.$fireStore.collection('updated_posts')
    await updatedPostsRef.get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          // console.log(doc.data().name)
          commit('updated_posts_push', doc.data().name)
        })
      })
  },
  async get_posts ({ commit }) {
    const postsRef = this.$fireStore.collection('blog')
    await postsRef.get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          commit('posts_push', doc.data())
        })
      })
  },
  async get_posts_with_key ({ commit }) {
    const postsRef = this.$fireStore.collection('blog')
    await postsRef.get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          commit('posts_push_with_key', { key: doc.id, post: doc.data() })
        })
      })
  },
  async nuxtServerInit ({ dispatch }) {
    await dispatch('get_posts_with_key')
  }
}
