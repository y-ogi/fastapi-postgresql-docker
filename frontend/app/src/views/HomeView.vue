<template>
  <v-card class="mx-auto">
    <v-list lines="three" select-strategy="single">

      <v-list-item v-for="item in items" :key="item.id" value="item.id">

        <template v-slot:prepend="{ isActive }">
          <v-list-item-action start>
            <v-checkbox-btn :model-value="isActive"></v-checkbox-btn>
          </v-list-item-action>
        </template>
        
        <v-list-item-title>{{ item.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ item.created_at }}</v-list-item-subtitle>
      </v-list-item>

    </v-list>
  </v-card>
</template>

<script>

export default {
  components: {

  },
  data() {
    return {
      message: 'Click me',
      items: [],
      isActive: true,
    }
  },
  created() {
    this.getItems()
  },
  methods: {
    getItems() {
      this.axios.get('http://localhost:8000/items/')
      .then(response => {
        this.items = response.data
      })
    }
  }
}

</script>