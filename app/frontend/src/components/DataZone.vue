<template>
  <div id="mainContent">
    <div id="champRecommendations">
      <champRec></champRec>
    </div>
    <div id="configRecommendation">
      <configRec></configRec>
    </div>
    <div id="drakeInfo">
      <drakeInfo></drakeInfo>
    </div>
  </div>
</template>

<script>

import champRec from './ChampRec.vue'
import configRec from './ConfigRec.vue'
import drakeInfo from './DrakeInfo.vue'

export default {
  data () {
    return {
      message: 'My first component',
      blue_side: 'blue',
      red_side: 'red',
      ticketsBought: 0,
      ticketsTotal: 200,
      moneyAvailable: 29.02,
      priceMatch: 5,
      matches_added: [],
      champs: []
    }
  },
  components: {
    champRec,
    configRec,
    drakeInfo
  }
}
</script>

<style scoped>

#mainContent {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
}

#mainContent>* {
  margin: 5px;
}

#champRecommendations {
  flex: 0.2;
}

#configRecommendation {
  flex: 0.6;
}

#drakeInfo {
  flex: 0.2;
}

</style>
