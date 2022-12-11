<template>
  {{ message }}
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
            <div class="d-flex ">
              <v-card-text>
              {{ item.name }}
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn 
                  size="small"
                  color="secondary"
                  icon="mdi-check"
                  @click="deleteItem(item.id)">
                </v-btn>
              </v-card-actions>
            </div>
          </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
const API_URL = 'http://' + window.location.hostname + ':8000'

export default {
  components: {

  },
  data() {
    return {
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
      this.axios.get(API_URL + '/items/')
      .then(response => {
        this.items = response.data
      })
    },
    addItem() {
        this.axios.post(API_URL + '/items/', {
          name: this.newItem
        })
        .then(response => {
          this.items.push(response.data)
          this.newItem = ''
        })
    },
    deleteItem(id) {
        this.axios.delete(API_URL + '/items/' + id)
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