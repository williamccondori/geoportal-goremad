<template>
  <a-layout class="layout">
    <a-layout-sider collapsible width="20rem">
      <a-menu
        theme="dark"
        :default-selected-keys="['1']"
        mode="inline"
        @click="handleClick"
      >
        <a-menu-item key="/">
          <a-icon type="home" />
          <span>INICIO</span>
        </a-menu-item>
        <a-menu-item key="/settings">
          <a-icon type="setting" />
          <span>CONFIGURACIÓN</span>
        </a-menu-item>
        <a-sub-menu key="sub1">
          <span slot="title">
            <a-icon type="appstore" />
            <span>INFORMACIÓN GEOESPACIAL</span>
          </span>
          <a-menu-item key="/vectorlayers">
            GESTIONAR CAPAS VECTORIALES
          </a-menu-item>
          <a-menu-item key="/rasterlayers">
            GESTIONAR CAPAS RÁSTER
          </a-menu-item>
          <a-menu-item key="5"> GESTIONAR ESTILOS </a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <span slot="title">
            <a-icon type="appstore" />
            <span>SERVICIOS EXTERNOS</span>
          </span>
          <a-menu-item key="6"> GEOSERVER </a-menu-item>
          <a-menu-item key="8"> GEONETWORK </a-menu-item>
        </a-sub-menu>
        <a-menu-item key="9">
          <a-icon type="appstore" />
          <span>ORGANIZACIÓN</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header class="layout__header" />
      <a-layout-content class="layout__content">
        <main class="layout__main">
          <nuxt />
        </main>
      </a-layout-content>
      <a-layout-footer class="layout__footer">
        GEOPORTAL GOREMAD ©2022 CREADO POR: GOBIERNO REGIONAL DE MADRE DE DIOS
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script>
export default {
  name: "DefaultTemplate",
  methods: {
    handleClick(event) {
      this.$router.push(event.key);
    },
  },
};
</script>

<style lang="css" scoped>
.layout {
  min-height: 100vh;
}

.layout .layout__header {
  padding: 0;
  background: white;
}

.layout .layout__content {
  padding: 1rem;
}

.layout__main {
  padding: 1rem;
  background: white;
}

.layout__footer {
  text-align: center;
}
</style>
