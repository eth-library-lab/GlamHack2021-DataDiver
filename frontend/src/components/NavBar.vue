<template>
<v-card
  flat
  tile
  dense
  :height="height">
  <v-app-bar 
    app
    color="primary"
    dark>
    <h3 class="ma-3">Data-Diver</h3>
    <v-icon>mdi-diving-snorkel</v-icon>


  </v-app-bar>
</v-card>
</template>

<script>

export default {
    components: {
        
    },
    computed: {
      height() {
        switch (this.$vuetify.breakpoint.name) {
          case 'xs': return 75
          case 'sm': return 85
          case 'md': return 90
          case 'lg': return 95
          case 'xl': return 95
        } return 100
      }
    }
}
</script>

<style lang="scss" scoped>

</style>