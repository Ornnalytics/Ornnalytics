<template>
  <main>
    <div id="champZone">
      <div id="blueChampSelect">
        <champSelect :lado="'blue'" :rolePicked="b_rolePicked" :champsPicked="b_champsPicked" :myRole="b_myRole"
                     @pickRole="pickRoleB" @pickMyRole="pickMyRoleB" @unPickChamp="unPickChampB"></champSelect>
      </div>
      <div id="champList">
        <champList @setChamp="setChamp"></champList>
      </div>
      <div id="redChampSelect">
        <champSelect :lado="'red'" :rolePicked="r_rolePicked" :champsPicked="r_champsPicked" :myRole="r_myRole"
                     @pickRole="pickRoleR" @pickMyRole="pickMyRoleR" @unPickChamp="unPickChampR"></champSelect>
      </div>
    </div>

    <dataZone :b_picks="b_champsPicked" :b_pos="b_myRole" :r_picks="r_champsPicked" :r_pos="r_myRole"></dataZone>
  </main>
</template>

<script>
import champList from './ChampList.vue'
import champSelect from './ChampSelect.vue'
import dataZone from './DataZone.vue'

export default {
  data () {
    return {
      pickedChamp: 0,
      b_rolePicked: '',
      r_rolePicked: '',
      b_champsPicked: [0, 0, 0, 0, 0],
      r_champsPicked: [0, 0, 0, 0, 0],
      r_myRole: '',
      b_myRole: '',
      roleDict: {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
    }
  },
  methods: {
    pickRoleB (role) {
      this.b_rolePicked = role
      this.r_rolePicked = ''
      if (this.pickedChamp !== '') {
        this.b_champsPicked[this.roleDict[this.b_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      }
    },
    pickRoleR (role) {
      this.b_rolePicked = ''
      this.r_rolePicked = role
      if (this.pickedChamp !== '') {
        this.r_champsPicked[this.roleDict[this.r_rolePicked]] = this.pickedChamp
        this.pickedChamp = ''
      }
    },
    pickMyRoleB (role) {
      this.r_myRole = ''
      this.b_myRole = role
    },
    pickMyRoleR (role) {
      this.r_myRole = role
      this.b_myRole = ''
    },
    unPickChampR (role) {
      this.$set(this.r_champsPicked, [this.roleDict[role]], 0)
    },
    unPickChampB (role) {
      this.$set(this.b_champsPicked, [this.roleDict[role]], 0)
    },
    setChamp (champId) {
      this.pickedChamp = champId

      /* BLUE TEAM PICKS */
      if (this.b_rolePicked !== '') {
        /* IF PICK IS PICKED IN RED TEAM */
        if (this.r_champsPicked.includes(this.pickedChamp)) {
          let i = 0
          i = this.r_champsPicked.indexOf(this.pickedChamp)
          this.$set(this.r_champsPicked, i, 0)
        }
        /* IF PICK IS PICKED IN BLUE TEAM */
        else if (this.b_champsPicked.includes(this.pickedChamp)) {
          let i = 0
          let pre = 0
          i = this.b_champsPicked.indexOf(this.pickedChamp)
          pre = this.b_champsPicked[this.roleDict[this.b_rolePicked]]
          this.b_champsPicked[i] = pre
        }
        /* IF PICK IS NOT PICKED ANYWHERE */
        this.$set(this.b_champsPicked, this.roleDict[this.b_rolePicked], this.pickedChamp)
        this.pickedChamp = ''
      }
      /* RED TEAM PICKS */
      else if (this.r_rolePicked !== '') {
        /* IF PICK IS PICKED IN BLUE TEAM */
        if (this.b_champsPicked.includes(this.pickedChamp)) {
          let i = 0
          i = this.b_champsPicked.indexOf(this.pickedChamp)
          this.$set(this.b_champsPicked, i, 0)
        }
        /* IF PICK IS PICKED IN RED TEAM */
        else if (this.r_champsPicked.includes(this.pickedChamp)) {
          let i = 0
          let pre = 0
          i = this.r_champsPicked.indexOf(this.pickedChamp)
          pre = this.r_champsPicked[this.roleDict[this.r_rolePicked]]
          this.r_champsPicked[i] = pre
        }
        /* IF PICK IS NOT PICKED ANYWHERE */
        this.$set(this.r_champsPicked, this.roleDict[this.r_rolePicked], this.pickedChamp)
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
