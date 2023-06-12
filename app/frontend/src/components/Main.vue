<template>
  <main>
    <div id="champZone">
      <div id="blueChampSelect">
        <champSelect :lado="'blue'" :rolePicked="b_rolePicked" :champsPicked="b_champsPicked" :myRole="b_myRole"
                     :winrate="b_winrate" @pickRole="pickRoleB" @pickMyRole="pickMyRoleB" @unPickChamp="unPickChampB"></champSelect>
      </div>
      <div id="champList">
        <champList @setChamp="setChamp"></champList>
      </div>
      <div id="redChampSelect">
        <champSelect :lado="'red'" :rolePicked="r_rolePicked" :champsPicked="r_champsPicked" :myRole="r_myRole"
                     :winrate="r_winrate" @pickRole="pickRoleR" @pickMyRole="pickMyRoleR" @unPickChamp="unPickChampR"></champSelect>
      </div>
    </div>

    <dataZone :b_picks="b_champsPicked" :b_pos="b_myRole" :r_picks="r_champsPicked" :r_pos="r_myRole"></dataZone>
    <div class="background"></div>
  </main>
</template>

<script>
import champList from './ChampList.vue'
import champSelect from './ChampSelect.vue'
import dataZone from './DataZone.vue'
import axios from 'axios'

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
      r_winrate: 0.5,
      b_winrate: 0.5,
      roleDict: {'TOP': 0, 'JGL': 1, 'MID': 2, 'ADC': 3, 'SUP': 4}
    }
  },
  methods: {
    pickRoleB (role) {
      this.b_rolePicked = role
      this.r_rolePicked = ''
      if (this.pickedChamp !== '') {
        this.$set(this.b_champsPicked, this.roleDict[this.b_rolePicked], this.pickedChamp)
        this.pickedChamp = ''
        this.winrateCalc()
      }
    },
    pickRoleR (role) {
      this.b_rolePicked = ''
      this.r_rolePicked = role
      if (this.pickedChamp !== '') {
        this.$set(this.r_champsPicked, this.roleDict[this.r_rolePicked], this.pickedChamp)
        this.pickedChamp = ''
        this.winrateCalc()
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
      this.winrateCalc()
    },
    unPickChampB (role) {
      this.$set(this.b_champsPicked, [this.roleDict[role]], 0)
      this.winrateCalc()
    },
    winrateCalc () {
      const path = 'http://localhost:8000/whole_winrate/'

      axios.post(path, {
        r_picks: this.r_champsPicked,

        b_picks: this.b_champsPicked
      })
        .then((res) => {
          var champRec = res.data

          this.r_winrate = champRec.r_WR
          this.b_winrate = champRec.b_WR
          console.log('wrwrwrwrwr', champRec)
        })
        .catch((error) => {
          console.error(error)
        })
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

      this.winrateCalc()
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

.background {
  position: absolute;
  top: 0px;
  bottom: 0px;
  left: 0px;
  right: 0px;
  background-image: url("../../static/background.png");
  background-repeat: no-repeat;
  background-size: cover;
  backdrop-filter: contrast(0.5);
  opacity: 0.5;
  z-index: -1;
}

</style>
