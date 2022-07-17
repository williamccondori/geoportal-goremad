<template>
  <a-form-model
    ref="ruleForm"
    :model="form"
    :rules="rules"
    @submit.prevent="handleSubmit"
  >
    <a-form-model-item prop="username">
      <a-input v-model="form.username" placeholder="Nombre de usuario">
        <a-icon slot="prefix" type="user" style="color: rgba(0, 0, 0, 0.25)" />
      </a-input>
    </a-form-model-item>
    <a-form-model-item prop="password">
      <a-input-password v-model="form.password" placeholder="Contraseña">
        <a-icon slot="prefix" type="lock" style="color: rgba(0, 0, 0, 0.25)" />
      </a-input-password>
    </a-form-model-item>
    <a-form-model-item>
      <a-button type="primary" block html-type="submit" :loading="loading">
        Ingresar
      </a-button>
      <a-button type="link" block>¿Olvidó su contraseña?</a-button>
    </a-form-model-item>
  </a-form-model>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      form: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          {
            required: true,
            message: "Ingrese su nombre de usuario",
          },
        ],
        password: [
          {
            required: true,
            message: "Ingrese su contraseña",
          },
        ],
      },
    };
  },
  methods: {
    handleSubmit() {
      this.$refs.ruleForm.validate(async (valid) => {
        if (valid) {
          try {
            this.loading = true;
            await this.$auth.loginWith("local", { data: this.form });
          } catch (error) {
            this.$message.success(error.message);
          } finally {
            this.loading = false;
          }
        }
      });
    },
  },
};
</script>
