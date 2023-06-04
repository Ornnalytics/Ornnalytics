<template>
    <div class="champsIconsSelection">
        <div class="champIconSelection roleTOP" :class="[lado]">
        </div>
        <div class="champIconSelection roleJGL" :class="[lado]">
        </div>
        <div class="champIconSelection roleMID" :class="[lado]">
        </div>
        <div class="champIconSelection roleADC" :class="[lado]">
        </div>
        <div class="champIconSelection roleSUP" :class="[lado]">
        </div>
    </div>
</template>

<script>

export default {
  name: 'champ_selector',
  props: ['lado']
}

</script>

<style scoped>

.champIconSelection {
    background: lightblue;
    border-radius: 50%;
    width: 100px;
    height: 100px;
    margin: 30px;
}

.blue {
    box-shadow: 0 0 7px blue;
}

.red {
    box-shadow: 0 0 7px red;
}

</style>
