<template>
  <Page title="GESTIONAR CAPAS RÁSTER">
    <a-button type="primary" class="mb-1" @click="handleCreate">
      <a-icon type="plus" />
      <span>NUEVO</span>
    </a-button>
    <RasterLayerForm />
    <RasterLayerTable />
  </Page>
</template>

<script>
import { mapActions } from "vuex";
import Page from "../components/shared/Page.vue";
import RasterLayerForm from "../components/rasterlayer/RasterLayerForm.vue";
import RasterLayerTable from "~/components/rasterlayer/RasterLayerTable.vue";
export default {
  name: "RasterLayersPage",
  components: {
    Page,
    RasterLayerForm,
    RasterLayerTable,
  },
  methods: {
    ...mapActions(["toggleRasterLayerDrawer"]),
    handleCreate() {
      this.toggleRasterLayerDrawer();
    },
  },
};
</script>
