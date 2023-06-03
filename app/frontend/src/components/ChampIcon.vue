<template>
  <div class="champIcon" :class="{champId : true}">
    <img :src="'/static/icons/'+ champId +'.jpg'">
  </div>
</template>

<script>

export default {
  name: 'ChampionIcon',
  props: ['champId']
}

</script>

<style scoped>
.champIcon {
  background-color: #444;
  color: #fff;
  border-radius: 5px;
  padding: 20px;
  font-size: 150%;
}
</style>
