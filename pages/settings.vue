<template>
  <div>
    <a-breadcrumb>
      <a-breadcrumb-item>
        <nuxt-link to="/"> INICIO </nuxt-link>
      </a-breadcrumb-item>
      <a-breadcrumb-item>CONFIGURACIÓN</a-breadcrumb-item>
    </a-breadcrumb>
    <a-page-header title="CONFIGURACIÓN" @back="() => $router.back()" />
    <a-divider />
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
  </div>
</template>

<script>
export default {
  name: "SettingsPage",
  data() {
    return {};
  },
};
</script>

<style lang="less" scoped></style>
