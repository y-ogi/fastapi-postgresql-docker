<template>
  <div class="hello">
    <h1>Hello World {{ message }}</h1>
    <h1>{{ items.name }}</h1>
  </div>
</template>

<script>

export default {
    components: {
    },
    data() {
      return {
        message : '',
        items: [],
      }
    },
    created() {
      this.getItems()
    },
    methods: {
      getItems() {
        this.axios.get('http://192.168.0.128:8000/items/1')
        .then(response => {
          this.items = response.data
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