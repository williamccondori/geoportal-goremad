<template>
  <a-table :columns="columns" :data-source="vectorLayers" size="small" bordered>
    <template slot="actions" slot-scope="key">
      <a-button type="dashed" size="small" @click="handleEdit(key)">
        <a-icon type="edit" />
      </a-button>
      <a-popconfirm
        title="¿ESTÁ SEGURO QUE DESEA ELIMINAR ESTE REGISTRO?"
        @confirm="handleDelete(key)"
      >
        <a-button type="dashed" size="small">
          <a-icon type="delete" />
        </a-button>
      </a-popconfirm>
    </template>
  </a-table>
</template>

<script>
import { mapState, mapActions } from "vuex";

const columns = [
  {
    title: "NOMBRE",
    dataIndex: "name",
  },
  {
    title: "TÍTULO",
    dataIndex: "title",
  },
  {
    title: "ACCIONES",
    dataIndex: "key",
    scopedSlots: { customRender: "actions" },
  },
];

export default {
  data() {
    return {
      columns,
    };
  },
  async fetch() {
    try {
      await this.fetchVectorLayers();
    } catch (error) {
      this.$message.error(error.message);
    }
  },
  computed: {
    ...mapState(["vectorLayers"]),
  },
  methods: {
    ...mapActions([
      "fetchVectorLayers",
      "fetchVectorLayer",
      "deleteVectorLayer",
      "toggleVectorLayerDrawer",
    ]),
    async handleEdit(vectorLayerKey) {
      try {
        await this.fetchVectorLayer(vectorLayerKey);
        this.toggleVectorLayerDrawer();
      } catch (error) {
        this.$message.error(error.message);
      }
    },
    async handleDelete(vectorLayerKey) {
      try {
        await this.deleteVectorLayer(vectorLayerKey);
        this.$message.success("EL PROCESO SE HA REALIZADO CORRECTAMENTE");
      } catch (error) {
        this.$message.error(error.message);
      }
    },
  },
};
</script>
