<template>
  <!--<header>
    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main>-->
  <main>
    <div id="blueChampSelect">
      <champSelect side="blue"></champSelect>
    </div>
    <div id="champList">
      <champList></champList>
    </div>
    <div id="redChampSelect">
      <champSelect side="red"></champSelect>
    </div>
  </main>
</template>


<script>
import champList from './ChampList.vue'
import champSelect from './ChampSelect.vue'

export default {
  data() {
    return {
      message: 'My first component',
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
  methods: {
    
  },
  components: {
    champList,
    champSelect
  }
}
</script>

<style>

main {
  display: flex;
}

</style>