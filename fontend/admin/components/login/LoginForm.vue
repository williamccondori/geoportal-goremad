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
      <a-button type="primary" block html-type="submit" :loading="isLoading">
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
      isLoading: false,
      form: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          {
            required: true,
            message: "Por favor ingrese su nombre de usuario",
          },
        ],
        password: [
          {
            required: true,
            message: "Por favor ingrese su contraseña",
          },
        ],
      },
    };
  },
  methods: {
    /**
     * async userLogin() {
      try {
        let response = await this.$auth.loginWith('local', { data: this.login })
        console.log(response)
      } catch (err) {
        console.log(err)
      }
    }
     */
    async handleSubmit() {
      try {
        this.isLoading = true;
        this.$refs.ruleForm.validate(async (valid) => {
          if (valid) {
            console.log("Form is valid");
          }
        });
      } catch (error) {
        this.$message.error(error);
      } finally {
        this.isLoading = false;
      }
    },
  },
};
</script>
