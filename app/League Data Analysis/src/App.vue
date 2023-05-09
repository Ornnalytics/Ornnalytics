
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

<script setup>
import champList from './components/ChampList.vue'
import champSelect from './components/ChampSelect.vue'
</script>


<style scoped>

main {
  display: flex;

}

</style>
