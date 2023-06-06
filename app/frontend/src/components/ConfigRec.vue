<template>
    <div id="mainContent">
      <div v-if="this.champ_id !== 0">
        <div v-if="this.runes.length > 0" id="runeDisplay-Container">
          <runeDisplay :configuration='this.runes'></runeDisplay>
        </div>
      </div>
      <div v-else>
        Para ver las recomendaciones, pickea :P.
      </div>
    </div>
</template>


<script>

import axios from 'axios'
import runeDisplay from './RuneDisplay.vue'

export default {
  data() {
      return {
        champ_id: 1,
        build: [],
        runes: []
      }
  },
  created () {
    if (this.champ_id !== 0) {
      // this.getChampBuild()
      this.getChampRunes()
    }
  },
  methods: {
    getChampBuild () {
      const path = 'http://localhost:8000/build/' + this.champ_id
      axios.get(path)
        .then((res) => {
          this.soulList = res.data
          this.soulList.sort((a, b) => (a.winrate < b.winrate) ? 1 : -1)
        })
        .catch((error) => {
          console.error(error)
        })
    },
    getChampRunes () {
      const path = 'http://localhost:8000/runes/' + this.champ_id
      axios.get(path)
        .then((res) => {
          this.runes = res.data
          console.log('Runes: ', this.runes)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  components: {
    runeDisplay
  }
}

</script>

<style scoped>

#mainContent {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  background: lightgrey;
  border: 1px solid lightgoldenrodyellow;
  align-content: center;
  justify-content: center;
}

#runeDisplay-Container {
  display: flex;
  align-content: center;
  justify-content: center;

  margin-top: 30px;
}

</style>
