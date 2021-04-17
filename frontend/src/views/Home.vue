<template>
<div>
    <FileSelector class="mt-1" />  
    <SearchResults v-if="resultsLoaded" :searchResults="searchResults" />

    <Spinner
      v-if="getIsLoading" 
      message="generating preview"
    />
    <Snackbar />
    <Footer v-if="!isFileSelected" />
</div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import FileSelector from '@/components/FileSelector.vue';
import Footer from '@/components/Footer.vue';
import SearchResults from '@/components/SearchResults.vue';
import Snackbar from '@/components/Snackbar.vue';
import Spinner from '@/components/Spinner.vue';

export default {
  components: {
    FileSelector,
    Footer,
    SearchResults,
    Snackbar,
    Spinner
  },
  computed: {
    ...mapGetters(['isFileSelected', 'resultsLoaded','getIsLoading',]),
    searchResults() {
      return this.$store.getters.getSearchResults
    },
  },
  methods: {
    ...mapActions(['showSnackbar',]),

  },
}

</script>

<style scoped>

.tight {
  padding:3px;
  margin-bottom:3px;
}
</style>
