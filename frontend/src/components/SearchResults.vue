<template>
    <v-container 
        justify="center"
        align="center"
        align-self="center"
        align-contents="center"
        >
        <div >
        <v-row justify="center" >
            <h3>Search Results</h3>
        </v-row>
        <v-row 
            justify="center"
            align="center">
            <v-col 
                class="results-wrapper"
                justify="center"
                align="center"
                xs="12" 
                sm="11" 
                md="10" 
                lg="8">
                <v-card
                    class="d-flex align-content-start flex-wrap justify-center"
                    color="white"
                    flat
                    over
                    >
                    IMAGE COLLAGE
                </v-card>
            </v-col>    
        </v-row>
        </div>
    </v-container>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
    props: {
        searchResults: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
        }
    },
    components:{ },
    computed: {
        ...mapGetters(['getIsLoading'])
    }

}
</script>

<style lang="css" scoped>
.results-wrapper {
  overflow-y: auto;
  height: 45vh;
  display: flex;
  flex-flow: column;
  align-items: center;
  margin: 10px;
  padding: 4px;
}
</style>