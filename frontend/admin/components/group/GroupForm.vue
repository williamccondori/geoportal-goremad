<template>
  <a-drawer
    title="GRUPO"
    width="30rem"
    :visible="groupDrawer"
    @close="handleClose"
  >
    <a-form-model
      ref="ruleForm"
      :model="form"
      :rules="rules"
      @submit.prevent="handleSubmit"
    >
      <a-form-model-item label="NOMBRE" prop="name">
        <a-input
          v-model="form.name"
          placeholder="INGRESE EL NOMBRE DEL GRUPO"
        />
      </a-form-model-item>
      <a-form-model-item label="DESCRIPCIÓN" prop="name">
        <a-input
          v-model="form.description"
          placeholder="INGRESE LA DESCRIPCIÓN DEL GRUPO"
        />
      </a-form-model-item>
      <a-form-model-item>
        <a-button type="primary" block html-type="submit" :loading="loading">
          GUARDAR
        </a-button>
      </a-form-model-item>
    </a-form-model>
  </a-drawer>
</template>

<script>
export default {};
</script>
