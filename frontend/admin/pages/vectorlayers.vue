<template>
  <Page title="GESTIONAR CAPAS VECTORIALES">
    <a-button type="primary" class="mb-1" @click="handleCreate">
      <a-icon type="plus" />
      <span>NUEVO</span>
    </a-button>
    <VectorLayerForm />
    <VectorLayerTable />
  </Page>
</template>

<script>
import { mapActions } from "vuex";
import Page from "../components/shared/Page.vue";
import VectorLayerForm from "../components/vectorlayer/VectorLayerForm.vue";
import VectorLayerTable from "~/components/vectorlayer/VectorLayerTable.vue";
export default {
  name: "VectorLayersPage",
  components: {
    Page,
    VectorLayerForm,
    VectorLayerTable,
  },
  methods: {
    ...mapActions(["toggleVisibleLayerDrawer"]),
    handleCreate() {
      this.toggleVisibleLayerDrawer();
    },
  },
};
</script>
