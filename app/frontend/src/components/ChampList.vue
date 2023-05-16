<template>
    <div>
        <div class="filter-icons-header">
            FILTER
        </div>
        <div class="champList">
            <div class="champItem" v-for="(champ, index) in champList" :key="index">
                {{ index }}: {{ champ.name }}
            </div>
        </div>
    </div>
    <!--
    <div class="champ-listing">
        <div class="champ-icon" v-for="champ in champList">
            <champIcon champId="{{champ.id}}"></champIcon>
            {{ champ.name }}
        </div>
    </div>
    -->
</template>

<script>
import champIcon from './ChampIcon.vue'
import axios from 'axios'

export default {
  data () {
    return {
      champList: []
    }
  },
  created () {
    this.getChamps()
    console.log('SE llama')
  },
  components: {
    champIcon
  },
  methods: {
    getChamps () {
      const pathChamps = 'http://localhost:8000/champs'
      axios.get(pathChamps)
        .then((res) => {
          console.log(res.data)
          this.champList = res.data
          console.log(this.champList)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>

.champList {
    height: 70vh;
    widtH: 50vw;
    overflow-y: scroll;
    display: grid;
    grid-template-columns: 100px 100px 100px 100px 100px;
    grid-gap: 10px;
    background-color: #fff;
    color: #444;
}

.champItem {
    background-color: #444;
    color: #fff;
    border-radius: 5px;
    padding: 20px;
    font-size: 150%;
}

</style>