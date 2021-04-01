<template>
<div id="vs"></div>
</template>

<script>
import Player from 'xgplayer';

export default {
  name: "Video",
  mounted() {
    new Player({
        id: 'vs',
        url: 'http://s2.pstatp.com/cdn/expire-1-M/byted-player-videos/1.0.0/xgplayer-demo.mp4'
    })
  }
}
</script>

<style scoped>

</style>