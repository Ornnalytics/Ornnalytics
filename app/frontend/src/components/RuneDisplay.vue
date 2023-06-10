<template>
  <div id="main-Container">
    <div id="perkData-Container">
      <img :src="'/static/lane_icons/'+ this.runesDisplayed.line +'.png'">
    </div>
    <div style="display: flex; flex-direction: row; align-content: center; justify-content: center;">
      <button class="changeButton" @click="changeRunes('left')">
        <img src="/static/useful_icons/arrow.png">
      </button>
      <div id="perkContent-Container">
        <div id="perkStyles-Container">
          <div class="perkStyle">
            <img :src="'/static/perk_icons/'+ this.runesDisplayed.mainStyle +'.png'">
          </div>
          <div class="perkStyle">
            <img :src="'/static/perk_icons/'+ this.runesDisplayed.secondaryStyle +'.png'">
          </div>
        </div>
        <div id="perks-Container">
          <div id="mainPerks-Container">
            <div class="perk" v-for="(perk, i) in this.runesDisplayed.main" v-bind:key="'A' + i">
              <img :src="'/static/perk_icons/'+ perk +'.png'">
            </div>
          </div>
          <div id="secPerks-Container">
            <div class="perk" v-for="(perk, i) in this.runesDisplayed.secondary" v-bind:key="'B' + i">
              <img :src="'/static/perk_icons/'+ perk +'.png'">
            </div>
            <div class="lastPerk" v-for="(perk, i) in this.runesDisplayed.lastPerks" v-bind:key="'C' + i">
              <img :src="'/static/perk_icons/'+ perk +'.png'">
            </div>
          </div>
        </div>
      </div>
      <button class="changeButton" @click="changeRunes('right')">
        <img src="/static/useful_icons/arrow.png" style="transform: rotate(180deg)">
      </button>
    </div>
    <div style="display: flex; justify-content: center;">
      <span>
        {{ runePos+1 }}/{{ runes.length }}
      </span>
    </div>
  </div>
</template>

<script>

export default {
  props: ['configuration'],
  data() {
    return {
      runes: [],
      runesDisplayed: {},
      runePos: 0,
      runesDict: {}
    }
  },
  created() {
    console.log(this.configuration)
    this.runes = this.configuration
    this.adaptRunes(this.runes[this.runePos])
  },
  watch: {
    configuration: {
      handler(newvalue, oldvalue) {
        this.runePos = 0
        this.adaptRunes(newvalue[this.runePos])
        this.runes = newvalue
      }
    }
  },
  methods: {
    adaptRunes (runes) {
      this.runesDisplayed = {}
      this.runesDisplayed.champ_id = runes.champ_id
      this.runesDisplayed.line = runes.line
      this.runesDisplayed.option = runes.opt

      this.runesDisplayed.mainStyle = runes.main_perk_style_id
      this.runesDisplayed.main = [
        runes.main_perk_id_1,
        runes.main_perk_id_2,
        runes.main_perk_id_3,
        runes.main_perk_id_4
      ]

      this.runesDisplayed.secondaryStyle = runes.second_perk_style_id
      this.runesDisplayed.secondary = [
        runes.second_perk_id_1,
        runes.second_perk_id_2
      ]

      this.runesDisplayed.lastPerks = [
        runes.last_perk_id_1,
        runes.last_perk_id_2,
        runes.last_perk_id_3
      ]

      this.$forceUpdate()
      console.log(this.runesDisplayed)
    },
    changeRunes (side) {
      if (side === 'left') {
        if (this.runePos === 0) {
          this.runePos = this.runes.length - 1
        } else {
          this.runePos -= 1
        }
      } else if (side === 'right') {
        if (this.runePos === this.runes.length - 1) {
          this.runePos = 0
        } else {
          this.runePos += 1
        }
      }

      this.adaptRunes(this.runes[this.runePos])
    }
  }
}

</script>

<style>

#main-Container {
  display: flex;
  flex-direction: column;
  padding: 5px 15px;
}

#perkContent-Container {
  padding: 20px;
}

#perkData-Container {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}

#perkData-Container > * {
  margin: 10px;
  width: 40px;
  height: 40px;
}

#perkStyles-Container {
  display: flex;
  flex-direction: row;
  margin-bottom: 10px;
}

.perkStyle {
  display: flex;
  justify-content: center;
  align-content: center;
  flex: 1 1 auto;

  filter: drop-shadow(1px 1px 1px #222);
}

.perkStyle>img {
  width: 40px;
}

.perk {
  display: flex;
  justify-content: center;
  align-content: center;
  margin: 6px;
}

.perk > img {
  width: 35px;
  filter: drop-shadow(2px 2px 2px #222);
}

.lastPerk {
  display: flex;
  justify-content: center;
  align-content: center;
}

.lastPerk > img {
  width: 29px;
  filter: drop-shadow(2px 2px 2px #222);
}

#perks-Container {
  display: flex;
  flex-direction: row;

}

#mainPerks-Container {
  display: flex;
  flex-direction: column;
  align-content: center;

  flex: 1 1 auto;
  margin: 20px;
}

#secPerks-Container {
  display: flex;
  flex-direction: column;
  align-content: center;

  flex: 1 1 auto;
  margin: 20px;
}

.changeButton {
  cursor: pointer;
  background-color: transparent;
  border: 0px;
}

.changeButton>img {
  width: 15px;
  height: 15px;
}

</style>
