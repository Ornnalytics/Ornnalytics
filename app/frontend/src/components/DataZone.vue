<template>
  <div id="mainContent">
    <div id="champRecommendations">
      <champRec :b_picks="b_picks" :b_pos="b_pos" :r_picks="r_picks" :r_pos="r_pos"></champRec>
    </div>
    <div id="configRecommendation">
      <configRec :b_picks="b_picks" :b_pos="b_pos" :r_picks="r_picks" :r_pos="r_pos"></configRec>
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
  props: ['r_picks', 'b_picks', 'r_pos', 'b_pos'],
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
