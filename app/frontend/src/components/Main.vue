<template>
  <main>
    <div id="champZone">
      <div id="blueChampSelect">
        <champSelect :lado=blue_side></champSelect>
      </div>
      <div id="champList">
        <champList></champList>
      </div>
      <div id="redChampSelect">
        <champSelect :lado=red_side></champSelect>
      </div>
    </div>

    <div id="dataZone">
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
  </main>
</template>


<script>
import champList from './ChampList.vue'
import champSelect from './ChampSelect.vue'
import champRec from './ChampRec.vue'
import configRec from './ConfigRec.vue'
import drakeInfo from './DrakeInfo.vue'

export default {
  data() {
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
  created() {
    console.log('SE llama')
  },
  components: {
    champList,
    champSelect,
    champRec,
    configRec,
    drakeInfo
  }
}
</script>

<style>

body {
  margin: 0px;
}
main {
  padding: 10px;
  display: flex;
}

#champZone {
  display: flex;
}

#dataZone {
  display: flex;
  flex-direction: column;
}

.drakeInfo {
  margin: 10px;
  padding: 5px;
  min-height: 1.5rem;
  background-color: lightgray;
  border-radius: 3px;
}

.configRecommendation {
  margin: 10px;
  padding: 5px;
  min-height: 1.5rem;
  background-color: lightgray;
  border-radius: 3px;
}

.champRecommendations {
  margin: 10px;
  padding: 5px;
  min-height: 1.5rem;
  background-color: lightgray;
  border-radius: 3px;
}
</style>