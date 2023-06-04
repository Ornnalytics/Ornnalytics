<template>
    <div id="mainContent">
        CHAMP RECOMMENDATIONS
    </div>
</template>


<script>

import axios from 'axios'

export default {
  data() {
      return {
        champ_id: 0,
        champ_rec: []
      }
  },
  created () {
    this.getChampRec()
  },
  methods: {
    getChampRec () {
      const path = 'http://localhost:8000/suggestion/'
      const parameters = {
        r_1: 1,
        r_2: 4,
        r_3: 6,
        r_4: 7,
        r_5: 123,
        b_1: 23,
        b_2: 54,
        b_3: 62,
        b_4: 156,
        b_5: 18,
        player: 'r_5',
        role: 'top',
        timeline: '021122'
      }
      axios.get(path, parameters)
        .then((res) => {
          this.soulList = res.data
          this.soulList.sort((a, b) => (a.winrate < b.winrate) ? 1 : -1)
        })
        .catch((error) => {
          console.error(error)
        })
    }
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
}

</style>
