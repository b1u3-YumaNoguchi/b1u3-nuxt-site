export const state = () => ({
  counter: 0
})

// mutations は store の state を変える関数群
export const mutations = {
  increment (state) {
    state.counter++
  }
}

// actions 内では commit を用いて mutation を呼び出す
export const actions = {
  increment (context) {
    context.commit('increment')
  }
}
