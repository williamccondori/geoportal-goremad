<template>
  <Page title="GESTIONAR CAPAS RÁSTER">
    <a-button type="primary" class="mb-1">
      <a-icon type="plus" />
      <span>NUEVO</span>
    </a-button>
    <RasterLayerTable />
  </Page>
</template>

<script>
import RasterLayerTable from "~/components/rasterlayer/RasterLayerTable.vue";
import Page from "../components/shared/Page.vue";
export default {
  name: "RasterLayersPage",
  components: {
    Page,
    RasterLayerTable,
  },
};
</script>
