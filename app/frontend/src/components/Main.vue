<template>
  <main>
    <div id="champZone">
      <div id="blueChampSelect">
        <champSelect :lado=blue_side :rolePicked=b_rolePicked :champsPicked=b_champsPicked @pickRole="pickRoleB"></champSelect>
      </div>
      <div id="champList">
        <champList @setChamp="setChamp"></champList>
      </div>
      <div id="redChampSelect">
        <champSelect :lado=red_side :rolePicked=r_rolePicked :champsPicked=r_champsPicked @pickRole="pickRoleR"></champSelect>
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
      b_rolePicked: '',
      r_rolePicked: '',
      b_champsPicked: [1, 0, 777, 0, 0],
      r_champsPicked: [0, 0, 0, 0, 0],
      roleDict: {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
    }
  },
  methods: {
    pickRoleB (role) {
      this.b_rolePicked = role
      this.r_rolePicked = ''
      console.log(this.b_rolePicked)
      if (this.pickedChamp !== '') {
        this.b_champsPicked[this.roleDict[this.b_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      }
    },
    pickRoleR (role) {
      this.b_rolePicked = ''
      this.r_rolePicked = role
      console.log(this.r_rolePicked)
      if (this.pickedChamp !== '') {
        this.r_champsPicked[this.roleDict[this.r_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      }
    },
    setChamp (champ_id) {
      this.pickedChamp = champ_id
      if (this.b_rolePicked !== '') {
        this.b_champsPicked[this.roleDict[this.b_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      } else if (this.r_rolePicked !== '') {
        this.r_champsPicked[this.roleDict[this.r_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      }
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
  flex: 1;
}

#blueChampSelect {
  flex: 1;
}

#redChampSelect {
  flex: 1;
}

</style>
