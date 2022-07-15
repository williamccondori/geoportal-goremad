<template>
  <a-layout class="layout">
    <a-layout-content class="layout__content">
      <nuxt />
    </a-layout-content>
    <a-layout-footer class="layout__footer">
      GEOPORTAL GOREMAD ©2022 CREADO POR: GOBIERNO REGIONAL DE MADRE DE DIOS
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  name: "AuthTemplate",
  methods: {},
};
</script>

<style lang="css" scoped>
.layout {
  min-height: 100vh;
}

.layout .layout__content {
  padding: 1rem;
  display: grid;
  align-content: center;
  justify-content: center;
  grid-template-columns: 25rem;
}

.layout__footer {
  text-align: center;
}
</style>
