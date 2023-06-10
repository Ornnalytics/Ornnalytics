<template>
    <div id="mainContent">
        <div id="champRec-Container">
          <div v-for="(champRec, i) in champ_rec" v-bind:key="i" class="champRec">
            <img :src="'/static/icons/' + champRec.champ_id + '.jpg'">
            <span>{{ (champRec.winrate*100).toFixed(2) }}%</span>
            <span>{{ (champRec.ponderation*100).toFixed(2) }}%</span>
          </div>
        </div>
    </div>
</template>


<script>

import axios from 'axios'

export default {
  props: ['r_picks', 'b_picks', 'r_pos', 'b_pos'],
  data() {
      return {
        champ_id: 0,
        champ_rec: [],
        picks: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        pos: '',
        role: ''
      }
  },
  created () {
    if (this.pos !== '' && this.role !== '') {
      this.getChampRec()
    }
  },
  watch: {
    b_picks: {
      handler(newvalue, oldvalue) {
        this.picks[0] = newvalue[0]
        this.picks[1] = newvalue[1]
        this.picks[2] = newvalue[2]
        this.picks[3] = newvalue[3]
        this.picks[4] = newvalue[4]
        this.getChampRec()
      },
      deep: true
    },
    r_picks: {
      handler(newvalue, oldvalue) {
        this.picks[5] = newvalue[0]
        this.picks[6] = newvalue[1]
        this.picks[7] = newvalue[2]
        this.picks[8] = newvalue[3]
        this.picks[9] = newvalue[4]
        this.getChampRec()
      },
      deep: true
    },
    r_pos: {
      handler(newvalue, oldvalue) {
        if (this.b_pos === '') {
          this.pos = 'r_' + newvalue
          this.role = newvalue
        }
        this.getChampRec()
      }
    },
    b_pos: {
      handler(newvalue, oldvalue) {
        if (this.r_pos === '') {
          this.pos = 'b_' + newvalue
          this.role = newvalue
        }
        this.getChampRec()
      }
    }
  },
  methods: {
    getChampRec () {
      const path = 'http://localhost:8000/suggestion/'

      if (this.pos === '' || this.role === '') {
        console.log(this.pos, this.role)
        console.log('EXITING FROM HERE')
        return
      }
      axios.post(path, {
        picks: this.picks,
        player: this.pos,
        role: this.role,
        timeline: '021122'
      })
        .then((res) => {
          this.champ_rec = res.data
          console.log('AAAAAAAAA', this.champ_rec)
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}

</script>

<style scoped>

#mainContent {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
  background: lightgrey;
  border: 1px solid lightgoldenrodyellow;
}

#champRec-Container {
  display: flex;
  flex-direction: row;
}

.champRec {
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  align-items: center;

  user-select: none;

  margin: 20px;
}

.champRec > img {
  width: 65px;
}

.champRec > span {
  margin-top: 10px;
}

</style>
