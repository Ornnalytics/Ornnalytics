<template>
    <div>
        <div class="filter-icons-header">
            <input @input="onSearchInput" placeholder="Buscar...">
        </div>
        <div class="champList">
          <button class="champIcon" v-for="champ in champList" v-key="champ.id" v-show="filter(champ)">
            <img :src="'/static/icons/'+ champ.champ_id +'.jpg'">
            <div>
              <span class="champName">{{ champ.name }}</span>
            </div>
          </button>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      champList: [],
      searchFilter: ''
    }
  },
  created () {
    this.getChamps()
  },
  methods: {
    getChamps () {
      const pathChamps = 'http://localhost:8000/champs'
      axios.get(pathChamps)
        .then((res) => {
          console.log(res.data)
          this.champList = res.data
          console.log(this.champList)
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onSearchInput (ev) {
      console.log(`Input event - Value: ${ev.target.value}`)
      this.searchFilter = ev.target.value
      this.$forceUpdate()
    },
    filter (champ) {
      console.log('FILTERING CHAMP', champ.name, 'With search value:', this.searchFilter)
      if (champ.name.toUpperCase().search(this.searchFilter.toUpperCase()) > -1) {
        return true
      }
    }
  }
}
</script>

<style scoped>

.filter-icons-header {
  width: 100%;
  height: 100px;
}

.champList {
  max-height: 70vh;
  widtH: 50vw;
  overflow-y: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(90px, 90px));
  gap: 10px;
  background-color: #fff;
  color: #444;
  padding-left: 50px;
  align-items: start;
  justify-content: start;
}

.champIcon {
  width: 90px;
  background-color: transparent;
  border: 0;
}

img {
  width: 90px;
}

</style>
