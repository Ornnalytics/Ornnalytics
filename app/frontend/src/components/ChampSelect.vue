<template>
    <div class="champsIconsSelection">
        <button class="champIconSelection roleTOP" :class="{[lado]: true, picked: (this.rolePicked==='TOP'), setted: (this.champsPicked[0] !== 0)}" @click="pickRole('TOP')">
          <img :src="'/static/icons/'+ this.champsPicked[0] +'.jpg'" v-if="this.champsPicked[0] !== 0">
        </button>
        <button class="champIconSelection roleJGL" :class="{[lado]: true, picked: (this.rolePicked==='JGL'), setted: (this.champsPicked[1] !== 0)}" @click="pickRole('JGL')">
          <img :src="'/static/icons/'+ this.champsPicked[1] +'.jpg'" v-if="this.champsPicked[1] !== 0">
        </button>
        <button class="champIconSelection roleMID" :class="{[lado]: true, picked: (this.rolePicked==='MID'), setted: (this.champsPicked[2] !== 0)}" @click="pickRole('MID')">
          <img :src="'/static/icons/'+ this.champsPicked[2] +'.jpg'" v-if="this.champsPicked[2] !== 0">
        </button>
        <button class="champIconSelection roleADC" :class="{[lado]: true, picked: (this.rolePicked==='ADC'), setted: (this.champsPicked[3] !== 0)}" @click="pickRole('ADC')">
          <img :src="'/static/icons/'+ this.champsPicked[3] +'.jpg'" v-if="this.champsPicked[3] !== 0">
        </button>
        <button class="champIconSelection roleSUP" :class="{[lado]: true, picked: (this.rolePicked==='SUP'), setted: (this.champsPicked[4] !== 0)}" @click="pickRole('SUP')">
          <img :src="'/static/icons/'+ this.champsPicked[4] +'.jpg'" v-if="this.champsPicked[4] !== 0">
        </button>
    </div>
</template>

<script>

export default {
  name: 'champ_selector',
  props: ['lado', 'rolePicked', 'champsPicked'],
  methods: {
    pickRole (role) {
      this.$emit('pickRole', role)
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
  margin: 30px;
}

.champIconSelection > img {
  border-radius: 100%;
  width: 100px;
  height: 100px;
}

.blue {
  box-shadow: 0 0 7px blue;
}

.red {
  box-shadow: 0 0 7px red;
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

</style>
