<template>
  <div id="mainContainer">
    <div class="champsIconsSelection">
      <div v-for="position in positions" v-bind:key="position.pos" class="champsIcon-Container">
        <button v-if="lado === 'blue'" class="selectIcon" :class="{setted: (myRole===position.role)}" @click="pickMyRole(position.role)">
          <img src="/static/useful_icons/arrow.png" style="transform: rotate(180deg)">
        </button>
        <button class="champIconSelection"
                :class="{[lado]: true, picked: (rolePicked && rolePicked===position.role), setted: (champsPicked[position.pos] !== 0)}"
                @click="pickRole(position.role, $event)">
          <img :src="'/static/icons/'+ champsPicked[position.pos] +'.jpg'" v-if="champsPicked[position.pos] !== 0">
        </button>
        <button v-if="lado === 'red'" style="transform: rotate(180deg)"  class="selectIcon" :class="{setted: (myRole===position.role)}" @click="pickMyRole(position.role)">
          <img src="/static/useful_icons/arrow.png" style="transform: rotate(180deg)">
        </button>
      </div>
    </div>
    <div class="teamData-Container">
      <div class="damageData-Container">
        <span>
          Winrate: {{(wr*100).toFixed(2)}}%
        </span>
        <br>
        <span>
          Daño del equipo
        </span>
        <div class="bar-Container">
          <div id="AP">
          </div>
          <div id="AD">
          </div>
          <div id="TD">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'champ_selector',
  props: ['lado', 'rolePicked', 'champsPicked', 'myRole'],
  data () {
    return {
      wr: 0,
      positions: [
        {
          'pos': 0,
          'role': 'TOP'
        },
        {
          'pos': 1,
          'role': 'JGL'
        },
        {
          'pos': 2,
          'role': 'MID'
        },
        {
          'pos': 3,
          'role': 'ADC'
        },
        {
          'pos': 4,
          'role': 'SUP'
        }
      ]
    }
  },
  watch: {
    champsPicked: {
      handler(newvalue, oldvalue) {
        this.getTeamData()
      }
    }
  },
  methods: {
    pickRole (role, event) {
      if (event.ctrlKey) {
        this.$emit('unPickChamp', role)
      }
      this.$emit('pickRole', role)
    },
    pickMyRole (role) {
      this.$emit('pickMyRole', role)
    },
    getTeamData () {
      const path = 'http://localhost:8000/team_data/'

      console.log(this.champsPicked)

      axios.post(path, {
        picks: this.champsPicked
      })
        .then((res) => {
          var champRec = res.data
          document.getElementById('AP').setAttribute('style', 'width: ' + champRec.AP + '%;')
          document.getElementById('AD').setAttribute('style', 'width: ' + champRec.AD + '%;')
          document.getElementById('TD').setAttribute('style', 'width: ' + champRec.TD + '%;')
          this.wr = champRec.WR
          console.log('teamteamteamteam', champRec)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>

.champsIconsSelection {
  width: fit-content;
  user-select: none;
}

.champIconSelection {
  opacity: 0.7;
  background: #cddede;
  border-radius: 50%;
  width: 100px;
  height: 100px;
}

.champIconSelection > img {
  border-radius: 100%;
  width: 100px;
  height: 100px;
}

.champsIcon-Container {
  display: flex;
  flex-direction: row;
  margin: 30px;
}

.blue {
  box-shadow: 0 0 7px blue;
}

.red {
  box-shadow: 0 0 7px red;
}

.selectIcon {
  opacity: 0.2;
  padding: 5px;
}

.selectIcon>img {
  width: 20px;
  height: 20px;
  margin: 10px;
}

.picked {
  box-shadow: 0 0 20px 5px darkgreen;
}

.setted {
  opacity: 1;
}

button {
  padding: 0px;
  border: 0px;
  background-color: transparent;
  cursor: pointer;
}

.teamData-Container {
  padding: 20px;
}

.damageData-Container {
  display: flex;
  flex-direction: column;
}

.damageData-Container > span {
  margin-left: auto;
  margin-right: auto;
}

.bar-Container {
  display: flex;
  user-select: none;
}

#AP {
  background-color: #2796BC;
  width: 33%;
  height: 20px;
}

#AD {
  background-color: #E9422E;
  widtH: 33%;
  height: 20px;
}

#TD {
  background-color: #AAA;
  widtH: 33%;
  height: 20px;
}

</style>
