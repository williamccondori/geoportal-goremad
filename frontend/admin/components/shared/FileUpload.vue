<template>
  <a-upload-dragger
    accept="zip,application/zip,application/x-zip,application/x-zip-compressed"
    :multiple="false"
    :file-list="zipFiles"
    :remove="handleRemove"
    :before-upload="handleValidate"
  >
    <p class="ant-upload-drag-icon">
      <inbox-outlined />
    </p>
    <p class="ant-upload-text">Click or drag file to this area to upload</p>
    <p class="ant-upload-hint">
      Support for a single or bulk upload. Strictly prohibit from uploading
      company data or other band files
    </p>
  </a-upload-dragger>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      zipFiles: [],
    };
  },
  methods: {
    handleRemove() {
      this.zipFiles = [];
    },
    handleValidate(file) {
      try {
        const isZip = file.type === "application/zip";
        if (!isZip) {
          throw new Error("SOLO SE PERMITEN ARCHIVOS ZIP");
        }
        return isZip;
      } catch (error) {
        this.$message.error(error.message);
        return false;
      }
    },
  },
};
</script>
