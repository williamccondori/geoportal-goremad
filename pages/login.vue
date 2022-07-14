<template>
  <a-card>
    <h1 class="login__title">GEOPORTAL GOREMAD</h1>
    <LoginForm />
  </a-card>
</template>

<script>
import LoginForm from "../components/login/LoginForm.vue";
export default {
  name: "LoginPage",
  components: { LoginForm },
  layout: "auth",
};
</script>

<style lang="css" scoped>
.login {
  background-color: aquamarine;
}
.login__title {
  color: teal;
  text-align: center;
  font-weight: bolder;
  margin-bottom: 1rem;
}
</style>
