<template>
    <div class="filter-icons-header">

    </div>
    <div class="champ-listing">
        <div class="champ-icon" v-for="champ in champList">
            <!--<champIcon champId="{{champ.id}}"></champIcon>-->
            {{ champ }}
        </div>
    </div>
</template>

<script>
//import mySQLFdbunctions from "../sqlFunct.js"
import champIcon from './ChampIcon.vue'
//import mySQLFunctions from '../sqlFunct.js'
export default {
  data() {
    return {
      champList: [
        {
          "champ_id": 1,
          "name": "Annie",
          "main_role": "MID",
          "sec_role": "SUP"
        },
        {
          "champ_id": 2,
          "name": "Olaf",
          "main_role": "TOP",
          "sec_role": "JGL"
        }
      ],
    }
  },
  components: {
    champIcon
  }
}
</script>