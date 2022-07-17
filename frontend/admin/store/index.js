export const state = () => ({
  isVisibleLayerDrawer: false,

  // Usuarios
  user: null,
  users: [],
  userDrawer: false,

  // Capas vectoriales
  vectorLayer: null,
  vectorLayers: [],
  vectorLayerDrawer: false,

  // Capas raster
  rasterLayer: null,
  rasterLayers: [],
  rasterLayerDrawer: false,

  // Estilos
  style: null,
  styles: [],
  styleDrawer: false,
});

export const actions = {
  toggleVisibleLayerDrawer({ commit }) {
    commit("TOGGLE_VISIBLE_LAYER_DRAWER");
  },

  // Capas vectoriales
  async fetchVectorLayers({ commit }) {
    const { data } = await this.$axios.get(`/vector-layers/`);
    commit("SET_VECTOR_LAYERS", data);
  },
  async fetchVectorLayer({ commit }, vectorLayerKey) {
    const { data } = await this.$axios.get(`/vector-layers/${vectorLayerKey}`);
    commit("SET_VECTOR_LAYER", data);
  },
  async createVectorLayer({ commit }, vectorLayer) {
    const { data } = await this.$axios.post(`/vector-layers/`, {
      ...vectorLayer,
    });
    commit("ADD_VECTOR_LAYER", data);
  },
  async updateVectorLayer({ commit }, vectorLayer) {
    const { data } = await this.$axios.put(
      `/vector-layers/${vectorLayer.key}`,
      {
        ...vectorLayer,
      }
    );
    commit("UPDATE_VECTOR_LAYER", data);
  },
  async deleteVectorLayer({ commit }, vectorLayerKey) {
    const { data } = await this.$axios.delete(
      `/vector-layers/${vectorLayerKey}`
    );
    commit("DELETE_VECTOR_LAYER", data);
  },
  toggleVectorLayerDrawer({ commit }) {
    commit("TOGGLE_VECTOR_LAYER_DRAWER");
  },

  // Capas raster
  async fetchRasterLayers({ commit }) {
    const { data } = await this.$axios.get(`/raster-layers/`);
    commit("SET_RASTER_LAYERS", data);
  },
  async fetchRasterLayer({ commit }, rasterLayerKey) {
    const { data } = await this.$axios.get(`/raster-layers/${rasterLayerKey}`);
    commit("SET_RASTER_LAYER", data);
  },
  async createRasterLayer({ commit }, rasterLayer) {
    const { data } = await this.$axios.post(`/raster-layers/`, {
      ...rasterLayer,
    });
    commit("ADD_RASTER_LAYER", data);
  },
  async updateRasterLayer({ commit }, rasterLayer) {
    const { data } = await this.$axios.put(
      `/raster-layers/${rasterLayer.key}`,
      {
        ...rasterLayer,
      }
    );
    commit("UPDATE_RASTER_LAYER", data);
  },
  async deleteRasterLayer({ commit }, rasterLayerKey) {
    const { data } = await this.$axios.delete(
      `/raster-layers/${rasterLayerKey}`
    );
    commit("DELETE_RASTER_LAYER", data);
  },
  toggleRasterLayerDrawer({ commit }) {
    commit("TOGGLE_RASTER_LAYER_DRAWER");
  },
};

export const getters = {};

export const mutations = {
  TOGGLE_VISIBLE_LAYER_DRAWER: (state) =>
    (state.isVisibleLayerDrawer = !state.isVisibleLayerDrawer),

  // Capas vectoriales
  SET_VECTOR_LAYERS: (state, vectorLayers) =>
    (state.vectorLayers = vectorLayers),
  SET_VECTOR_LAYER: (state, vectorLayer) => (state.vectorLayer = vectorLayer),
  ADD_VECTOR_LAYER: (state, vectorLayer) =>
    state.vectorLayers.push(vectorLayer),
  UPDATE_VECTOR_LAYER: (state, vectorLayer) => {
    const index = state.vectorLayers.findIndex(
      (layer) => layer.key === vectorLayer.key
    );
    state.vectorLayers[index] = vectorLayer;
  },
  DELETE_VECTOR_LAYER: (state, vectorLayerKey) => {
    state.vectorLayers = state.vectorLayers.filter(
      (x) => x.key !== vectorLayerKey
    );
  },
  TOGGLE_VECTOR_LAYER_DRAWER: (state) =>
    (state.vectorLayerDrawer = !state.vectorLayerDrawer),

  // Capas raster
  SET_RASTER_LAYERS: (state, rasterLayers) =>
    (state.rasterLayers = rasterLayers),
  SET_RASTER_LAYER: (state, rasterLayer) => (state.rasterLayer = rasterLayer),
  ADD_RASTER_LAYER: (state, rasterLayer) =>
    state.rasterLayers.push(rasterLayer),
  UPDATE_RASTER_LAYER: (state, rasterLayer) => {
    const index = state.rasterLayers.findIndex(
      (layer) => layer.key === rasterLayer.key
    );
    state.rasterLayers[index] = rasterLayer;
  },
  DELETE_RASTER_LAYER: (state, rasterLayerKey) => {
    state.rasterLayers = state.rasterLayers.filter(
      (x) => x.key !== rasterLayerKey
    );
  },
  TOGGLE_RASTER_LAYER_DRAWER: (state) =>
    (state.rasterLayerDrawer = !state.rasterLayerDrawer),
};
