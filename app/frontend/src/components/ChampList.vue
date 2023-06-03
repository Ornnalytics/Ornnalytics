<template>
    <div>
        <div class="filter-icons-header">
            FILTER
        </div>
        <div class="champList">
          <button class="champIcon" v-for="champ in champList">
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
      champList: []
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
  height: 70vh;
  widtH: 50vw;
  overflow-y: scroll;
  display: grid;
  grid-template-columns: 90px 90px 90px 90px 90px 90px 90px;
  grid-gap: 10px;
  background-color: #fff;
  color: #444;
  padding-left: 50px;
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