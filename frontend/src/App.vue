<template>
  <v-app>
    <NavBar />
    <div>
    <v-main class="ma-0 pt-0">
      <router-view class="ma-0 pt-0"></router-view>
    </v-main>
    </div>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'App',

  components: {
    NavBar,
  },

  data: () => ({
    //
  }),
};
</script>

<style >

</style>
