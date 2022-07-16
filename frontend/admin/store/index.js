export const state = () => ({
  counter: 0,
  isVisibleLayerDrawer: false,
});

export const getters = {
  getCounter(state) {
    return state.counter;
  },
};

export const mutations = {
  increment(state) {
    state.counter++;
  },
  TOGGLE_VISIBLE_LAYER_DRAWER: (state) =>
    (state.isVisibleLayerDrawer = !state.isVisibleLayerDrawer),
};

export const actions = {
  async fetchCounter(state) {
    // make request
    const res = { data: 10 };
    state.counter = res.data;
    return res.data;
  },
  toggleVisibleLayerDrawer({ commit }) {
    commit("TOGGLE_VISIBLE_LAYER_DRAWER");
  },
};
