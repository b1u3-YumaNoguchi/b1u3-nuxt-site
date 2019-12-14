export const state = () => ({
  counter: 0,
  updated_posts: [],
  message: ''
})

// mutations は store の state を変える関数群
export const mutations = {
  increment (state) {
    state.counter++
  },
  set_message (state, msg) {
    state.message = msg
  }
}

// actions 内では commit を用いて mutation を呼び出す
export const actions = {
  increment (context) {
    context.commit('increment')
  },
  set_message ({ commit }, msg) {
    commit('set_message', msg)
  }
}
