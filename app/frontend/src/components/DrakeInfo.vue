<template>
    <div id="mainContent">
      <div class="dataContainer" v-for="soul in this.soulList" v-bind:key="soul.soulDrake_id">
        <span>
          <img :src="'/static/soul_icons/'+ soulDict[soul.soulDrake_id] +'.png'">
        </span>
        <span>
          {{ soul.winrate }} %
        </span>
      </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      soulList: [],
      soulDict: {
        0: 'chemtech_dragon_icon',
        1: 'air_dragon_icon',
        2: 'hextech_dragon_icon',
        3: 'fire_dragon_icon',
        4: 'earth_dragon_icon',
        5: 'water_dragon_icon'
      }
    }
  },
  created () {
    this.getSoulData()
  },
  methods: {
    getSoulData () {
      const pathSouls = 'http://localhost:8000/souls'
      axios.get(pathSouls)
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
  align-items: center;

  height: 100%;
  width: 100%;
  background-color: lightgrey;
  border: 1px solid lightgoldenrodyellow;
}

.dataContainer {
  display:flex;
  flex-direction: column;
  align-items: center;
  flex: 1 1 auto;
}

</style>
