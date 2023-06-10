<template>
    <div>
        <div class="filter-icons-header">
          <div class="filter-role-container">
            <button v-for="role in roleOptions" v-bind:key="role" class="filter-role-button"
                    :class="{ not_selected: (selectedRole !== 'ANY' && role !== selectedRole)}"
                    @click="roleSelectedInput(role)">
              <img :src="'/static/lane_icons/'+ role +'.png'" class="filter-role-image">
            </button>
          </div>
          <input @input="onSearchInput" placeholder="Buscar..." clasS="filter-search">
        </div>
        <div class="champList">
          <div class="champIcon" v-for="champ in champList" v-bind:key="champ.id" v-show="filter(champ)">
            <button @click="setChamp(champ.champ_id)">
              <img :src="'/static/icons/'+ champ.champ_id +'.jpg'">
            </button>
            <div>
              <span class="champName">{{ champ.name }}</span>
            </div>
          </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      champList: [],
      searchFilter: '',
      roleOptions: ['TOP', 'JGL', 'MID', 'ADC', 'SUP'],
      selectedRole: 'ANY'
    }
  },
  created () {
    this.getChamps()
  },
  methods: {
    getChamps () {
      const pathChamps = 'http://localhost:8000/champs'
      console.log('H?')
      axios.get(pathChamps)
        .then((res) => {
          console.log('WTf')
          this.champList = res.data.sort((a, b) => (a.name > b.name) ? 1 : -1)
          console.log(this.champList)
        })
        .catch((error) => {
          console.error(error)
        })
        .finally(() => {
          console.log('It tried i guess')
        })
      console.log('Ciau')
    },
    onSearchInput (ev) {
      this.searchFilter = ev.target.value
      this.$forceUpdate()
    },
    filter (champ) {
      let searchFilter = false
      let roleFilter = false
      console.log(this.searchFilter)
      if (champ.name.toUpperCase().search(this.searchFilter.toUpperCase()) > -1) {
        searchFilter = true
      }

      if (this.selectedRole === 'ANY') return searchFilter

      roleFilter = champ.main_role === this.selectedRole || champ.secondary_role === this.selectedRole
      return roleFilter && searchFilter
    },
    roleSelectedInput (role) {
      if (role === this.selectedRole) {
        this.selectedRole = 'ANY'
      } else {
        this.selectedRole = role
      }
      this.$forceUpdate()
    },
    setChamp (champId) {
      this.$emit('setChamp', champId)
    }
  }
}
</script>

<style scoped>

.filter-icons-header {
  width: 100%;

  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 20px;
}

.filter-role-container {
  display: flex;
  flex-direction: row;
}

.filter-role-button {
  flex: 1 1 auto;

  background-color: transparent;
  border: 0px solid transparent;

  cursor: pointer;

  margin: 5px 10px;
  padding: 0px;
}

.not_selected {
  opacity: 0.4;
}

.filter-role-image {
  width: 35px;
  height: 35px;
}

.filter-search {
  margin: 5px;
}

.champList {
  max-height: 70vh;
  widtH: 40vw;
  overflow-y: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(90px, 90px));
  gap: 10px;
  background-color: #fff;
  color: #444;
  padding-left: 50px;
  align-items: start;
  justify-content: start;
}

.champIcon {
  width: 90px;
  background-color: transparent;
  border: 0;
  padding: 0px;
}

.champIcon > button {
  cursor: pointer;
  user-select: none;
}

img {
  width: 90px;
}

.champName {
  user-select: none;
}

.custom-select {
  position: relative;
  width: 100%;
  text-align: left;
  outline: none;
  height: 47px;
  line-height: 47px;
}

button {
  padding: 0px;
  margin: 0px;
  border: 0px;
  background-color: transparent;
  align-content: center;
}
</style>
