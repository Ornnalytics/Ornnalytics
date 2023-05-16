<template>
    <div class="champsIconsSelection" :class="{ side : true }">
        <div class="champIconSelection roleTOP">
        </div>
        <div class="champIconSelection roleJGL">
        </div>
        <div class="champIconSelection roleMID">
        </div>
        <div class="champIconSelection roleADC">
        </div>
        <div class="champIconSelection roleSUP">
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    side: {
        type: String,
        required: true,
        validator(value) {
            // The value must match one of these strings
            return ['blue', 'red'].includes(value)
        }
    }
})

print(props.side)

</script>

<style scoped>
.champIconSelection {
    background: lightblue;
    border-radius: 50%;
    width: 100px;
    height: 100px;
}

#blue {
    border-color: blue;
}

#red {
    border-color: red;
}
</style>
