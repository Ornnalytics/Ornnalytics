<template>
    <div id="mainContent">
      <div v-if="this.champ_id !== 0" style="display: flex; align-items: center; flex: 1 1 auto;">
        <div v-if="this.runes.length > 0" id="runeDisplay-Container">
          <runeDisplay :configuration='this.runes'></runeDisplay>
        </div>
        <div id="buildDisplay-Container">
          <buildDisplay :champ_id='this.champ_id'></buildDisplay>
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
import buildDisplay from './BuildDisplay.vue'

export default {
  data() {
      return {
        champ_id: 777,
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
    runeDisplay,
    buildDisplay
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

  user-select: none;
}

#runeDisplay-Container {
  display: flex;
  align-content: center;
  justify-content: center;

  margin-top: 30px;
  width: 50%;
}

#buildDisplay-Container {
  width: 50%;
}

</style>
