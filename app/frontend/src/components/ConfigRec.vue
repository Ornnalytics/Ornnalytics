<template>
    <div id="mainContent">
      <div v-if="champId !== 0" style="display: flex; align-items: center; flex: 1 1 auto;">
        <div v-if="this.runes.length > 0" id="runeDisplay-Container">
          <runeDisplay :configuration='this.runes'></runeDisplay>
        </div>
        <div id="buildDisplay-Container">
          <buildDisplay :champ_id='champId'></buildDisplay>
        </div>
      </div>
      <div v-else style="margin: auto; font-size: 1.5rem; text-align: center;">
        Para ver las recomendaciones, primero pickea un lado y linea, y luego un champ!
      </div>
    </div>
</template>


<script>

import axios from 'axios'
import runeDisplay from './RuneDisplay.vue'
import buildDisplay from './BuildDisplay.vue'

export default {
  props: ['r_picks', 'b_picks', 'r_pos', 'b_pos'],
  data() {
      return {
        champ_id: 0,
        build: [],
        runes: [],
        roleDict: {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
      }
  },
  computed: {
    champId: function() {
      if (this.r_pos !== '') {
        this.getChampRunes(this.r_picks[this.roleDict[this.r_pos]])
        return this.r_picks[this.roleDict[this.r_pos]]
      } else if (this.b_pos !== '') {
        this.getChampRunes(this.b_picks[this.roleDict[this.b_pos]])
        return this.b_picks[this.roleDict[this.b_pos]]
      } else {
        return 0
      }
    }
  },
  methods: {
    getChampRunes (champId) {
      const path = 'http://localhost:8000/runes/' + champId
      axios.get(path)
        .then((res) => {
          this.runes = res.data
          this.runes.sort((a, b) => (a.line === b.line && a.opt > b.opt) ? 1 : (a.line === this.r_pos || a.line === this.b_pos) ? -1 : 1)
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
  background: #4545454d;

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
