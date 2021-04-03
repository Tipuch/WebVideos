<template>
<div id="vs"></div>
</template>

<script>
import Player from 'xgplayer';
import axios from 'axios';

export default {
  name: "Video",
  download_url: "",
  download_url_promise: null,
  async beforeCreate() {
    this.download_url_promise = axios
        .get('/video')
        .then(response => {
          this.download_url = response.data.download_url
        })
        .catch(error => console.log(error))
  },
  mounted() {
    this.download_url_promise.then(() => {
      new Player({
          id: 'vs',
          url: this.download_url
      })
    })
  }
}
</script>

<style scoped>

</style>