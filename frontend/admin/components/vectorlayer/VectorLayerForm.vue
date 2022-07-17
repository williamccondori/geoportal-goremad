<template>
  <a-drawer
    title="NUEVA CAPA VECTORIAL"
    width="30rem"
    :visible="vectorLayerDrawer"
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
          placeholder="INGRESE EL NOMBRE DE LA CAPA"
        />
      </a-form-model-item>
      <a-form-model-item label="TÍTULO" prop="title">
        <a-input
          v-model="form.title"
          placeholder="INGRESE EL TÍTULO DE LA CAPA"
        />
      </a-form-model-item>
      <a-form-model-item label="ARCHIVO" prop="title">
        <FileUpload />
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
import { mapState, mapActions } from "vuex";
import FileUpload from "../shared/FileUpload.vue";

export default {
  components: { FileUpload },
  data() {
    return {
      loading: false,
      form: {
        name: "",
        title: "",
      },
      rules: {
        name: [{ required: true, message: "Ingrese el nombre de la capa" }],
        title: [{ required: true, message: "Ingrese el título de la capa" }],
      },
    };
  },
  computed: {
    ...mapState(["vectorLayerDrawer"]),
  },
  methods: {
    ...mapActions(["toggleVectorLayerDrawer"]),
    resetForm() {
      this.form = {
        name: "",
        title: "",
      };
      this.$refs.ruleForm.resetFields();
    },
    handleClose() {
      this.resetForm();
      this.toggleVectorLayerDrawer();
    },
    handleSubmit() {
      this.$refs.ruleForm.validate(async (valid) => {
        if (valid) {
          try {
            this.loading = true;
            this.resetForm();
            this.$message.success("EL PROCESO HA CONCLUIDO CORRECTAMENTE");
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
