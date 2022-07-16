<template>
  <Page title="CONFIGURACIÓN">
    <a-radio-group>
      <a-tabs default-active-key="1" tab-position="left">
        <a-tab-pane key="1" tab="VALORES INICIALES">
          Content of Tab 1
        </a-tab-pane>
        <a-tab-pane key="2" tab="PARÁMETROS DE SISTEMA">
          Content of Tab 2
        </a-tab-pane>
        <a-tab-pane key="3" tab="USUARIOS"> Content of Tab 3 </a-tab-pane>
      </a-tabs>
    </a-radio-group>
  </Page>
</template>

<script>
import Page from "../components/shared/Page.vue";
export default {
  name: "SettingsPage",
  components: {
    Page,
  },
  data() {
    return {};
  },
};
</script>
