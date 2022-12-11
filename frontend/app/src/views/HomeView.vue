<template>
  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-text-field 
          label="Things you have to do" 
          variant="filled" 
          append-inner-icon="mdi-send"
          v-model="newItem"
          @click:append-inner="addItem"
          @keypress.prevent.enter.exact="enableSubmit"
          @keyup.prevent.enter.exact="submit"
          >
        </v-text-field>
      </v-col>  
      <v-col cols="12" v-for="item in items" :key="item.id">
        <v-card
            theme="dark"
          >
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="text-h6">
              {{ item.name }}
              </v-card-title>
            </div>
            <v-card-actions>
              <v-btn prepend-icon="mdi-check" @click="deleteItem(item.id)">
                Done
              </v-btn>
            </v-card-actions>
          </div>
          </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>

export default {
  components: {

  },
  data() {
    return {
      message: 'Click me',
      items: [],
      newItem: '',
      canSubmit: false,
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
    },
    enableSubmit() {
      this.canSubmit = true
    },
    submit() {
      if (!this.canSubmit) return;
      this.addItem()
      this.canSubmit = false
    }
  }
}

</script>