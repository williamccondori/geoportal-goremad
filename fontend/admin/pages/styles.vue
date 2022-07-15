<template>
  <Page title="GESTIONAR ESTILOS">
    <a-button type="primary" class="mb-1">
      <a-icon type="plus" />
      <span>NUEVO</span>
    </a-button>
  </Page>
</template>

<script>
import Page from "../components/shared/Page.vue";
export default {
  name: "StylesPage",
  components: {
    Page,
  },
};
</script>
