<template>
  <div id="main-Container">
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
        <div class="perk" v-for="perk in this.runesDisplayed.main" v-bind:key="perk">
          <img :src="'/static/perk_icons/'+ perk +'.png'">
        </div>
      </div>
      <div id="secPerks-Container">
        <div class="perk" v-for="perk in this.runesDisplayed.secondary" v-bind:key="perk">
          <img :src="'/static/perk_icons/'+ perk +'.png'">
        </div>
        <div class="lastPerk" v-for="perk in this.runesDisplayed.lastPerks" v-bind:key="perk">
          <img :src="'/static/perk_icons/'+ perk +'.png'">
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: ['configuration'],
  data() {
    return {
      runesDisplayed: {}
    }
  },
  created() {
    console.log(this.configuration)
    this.adaptRunes(this.configuration[0])
  },
  methods: {
    adaptRunes (runes) {
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

      console.log(this.runesDisplayed)
    }
  }
}

</script>

<style>

#main-Container {
  display: flex;
  flex-direction: column;
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

</style>
