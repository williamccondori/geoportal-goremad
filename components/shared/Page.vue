<template>
  <section>
    <a-breadcrumb>
      <a-breadcrumb-item>
        <nuxt-link to="/"> INICIO </nuxt-link>
      </a-breadcrumb-item>
      <a-breadcrumb-item>{{ title }}</a-breadcrumb-item>
    </a-breadcrumb>
    <a-page-header :title="title" @back="() => $router.back()" />
    <slot />
  </section>
</template>

<script>
export default {
  name: "PageContainer",
  props: {
    title: {
      type: String,
      default: "",
    },
  },
};
</script>
