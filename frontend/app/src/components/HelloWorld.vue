<template>
  <div class="hello">
    <form @submit.prevent="addItem">
      <input v-model="newItem">
      <button>Add Item</button>    
    </form>
    <ul>
      <li v-for="(item, key) in items" :key="key">
        {{ item.name }}<button @click="deleteItem(item.id)">X</button>
      </li>
    </ul>

  </div>
</template>

<script>

export default {
    components: {
    },
    data() {
      return {
        message : '',
        newItem: '',
        items: [],
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
      },
      addItem() {
        this.axios.post('http://localhost:8000/items/', {
          name: this.newItem
        })
        .then(response => {
          this.items.push(response.data)
          this.newItem = ''
        })
      },
      deleteItem(id) {
        this.axios.delete('http://localhost:8000/items/' + id)
        .then(response => {
          console.log(response)
          this.items = this.items.filter((item) => item.id != id);
        })
      }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>