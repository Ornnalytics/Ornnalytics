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

    <dataZone></dataZone>
  </main>
</template>

<script>
import champList from './ChampList.vue'
import champSelect from './ChampSelect.vue'
import dataZone from './DataZone.vue'

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
    champList,
    champSelect,
    dataZone
  }
}
</script>

<style>

html, body {
  margin: 0px;
}
main {
  padding: 10px;
  display: flex;
  position: absolute;
  top: 0px;
  right: 0px;
  left: 0px;
  bottom: 0px;
}

#champZone {
  display: flex;
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
