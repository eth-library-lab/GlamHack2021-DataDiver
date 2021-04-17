<template>
    <div>
        <v-container class='mt-0'>
            <v-col 
                class='tight' 
                align="center">
                <p class='tight' >
                    select a zip file to view a summary of the contents
                </p>
            </v-col>
        </v-container>
      <v-container class="my-0 py-0" >
       <v-row class="mt-0 pt-0" align="center" justify="center">
        <v-col 
            class="mt-0 pt-0" 
            xs="12" 
            sm="11" 
            md="10" 
            lg="8" 
            align="center">
            <v-card >
                <v-card-text class="font-weight-bold my-1 pb-1">Input File</v-card-text>
                <v-row align="center" justify="center">
                    <v-col class="ma-0 py-0"
                        
                        align-self="end">
                        <v-file-input
                            v-model="selectedFile"
                            class="ma-0 py-0"
                            show-size
                            accept=".zip"
                            placeholder="Select an  Archive File (.zip)"
                            prepend-icon="mdi-folder-zip"
                            color="primary"
                            @change="selectFile(selectedFile)"
                            @click:clear="clearResults()"
                        ></v-file-input>
                    </v-col>
                </v-row>
                </v-card>
            </v-col>
        </v-row>
        <!-- <v-row v-if="isFileSelected & !(resultsLoaded | getIsLoading)" 
            align="center"
            justify="center"> -->
        <v-row v-if="isFileSelected  & !(resultsLoaded | getIsLoading)" 
            align="center"
            justify="center">
            <v-col cols="10" align="center">
            <v-btn 
                class="align-center"
                color="primary"
                elevation="2"
                @click="uploadFile">
                Generate Preview
            </v-btn>
            </v-col>
        </v-row>
    </v-container>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    data: () => ({
        selectedFile: null
    }),
    computed: {
        ...mapGetters(['resultsLoaded', 'isFileSelected','getIsLoading']),
        fpath() {
            var path = require("path");
            var absolutePath = path.resolve("./");
            return absolutePath
        }
    },
    methods: {
        ...mapActions(['changeFileSelectedStatus',
                        'changeResultsLoadedStatus',
                        'requestFilePreview',
                        'changeIsLoadingStatus']),

        clearResults() {
            this.selectedFile = null
            this.changeIsLoadingStatus(false)
            this.changeResultsLoadedStatus(false)
            this.changeFileSelectedStatus(false)
        },
        selectFile(selectedFile){
            // remove previous files and preview
            this.clearResults()
            this.selectedFile = selectedFile
            this.changeFileSelectedStatus(true)
        },
        uploadFile() {
            this.changeIsLoadingStatus(true)
            this.requestFilePreview(this.selectedFile)
        },
    }
}
</script>

<style lang="css" scoped>

.tight {
  padding:3px;
  padding-top:3px;
  margin-bottom:3px;
}
.v-file-input{
  width: 95%;
  padding-left: 50px;
  padding-right: 50px;
}
.img-preview-container{
  min-height: 0vh;
  max-height: 55vh;
}
.image-border{
  border: black;
  border-width: 10px;
}
.img-preview{
    height: 50px;
    display: flex;
}
.circle {
    width: 100px;
    height: 100px;
    background: red;
    -moz-border-radius: 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px;
}
</style>