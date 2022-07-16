<template>
  <a-table :columns="columns" :data-source="data" size="small" bordered>
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

const data = [
  {
    key: 1,
    name: "Vector Layer 1",
    title: "Vector Layer 1",
  },
  {
    key: 2,
    name: "Vector Layer 2",
    title: "Vector Layer 2",
  },
  {
    key: 3,
    name: "Vector Layer 3",
    title: "Vector Layer 3",
  },
];
export default {
  data() {
    return {
      columns,
      data,
    };
  },
  methods: {
    handleEdit(key) {
      console.log(key);
    },
    handleDelete(key) {
      console.log(key);
    },
  },
};
</script>

<style scoped></style>
