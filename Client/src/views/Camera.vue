<template>
    <body>
        <div class="justify-center flex items-center">
            <video ref="video" autoplay playsinline webkit-playsinline muted hidden @submit.prevent="onMounted"></video>
            <canvas ref="canvas" width="720" height="480" class = "bg-black rounded-3x1"></canvas>
            <br/>
            <!-- <div class="flex items-center justify-content py-4">
                <button @click="TakePicture" class="px-6 py-4 bg-green-500 rounded text-white text-2x1 uppercase font-bold hover:bg-green-600">Take Picture</button>
            </div> -->
        </div>
    </body>
</template>
<script setup>
    import {ref, onMounted} from "vue";
    const canvas = ref(null);
    const video = ref(null);
    const ctx = ref(null);
    const constrains = ref({
        audio: false,
        video: true
    });

    onMounted(async () => {
        if (video.value && canvas.value) {
            ctx.value = canvas.value.getContext("2d"),
            await navigator.mediaDevices
                .getUserMedia(constrains.value)
                .then(setStream)
                .catch(e => {
                    console.error(e);
                })
        }    
    });

    function setStream(stream) {
        video.value.srcObject = stream;
        video.value.play();

        requestAnimationFrame(Draw);
    };

    function Draw() {
        ctx.value.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height);
        requestAnimationFrame(Draw);
    };

    async function TakePicture() {
        var link = document.createElement('a');
        link.download = 'vue-cam-${new Date().toISOString()}.png';
        link.href = canvas.value.toDataURL();
        link.click();
    };
</script>
<script>
    export default {
        name: "CameraView",
        data() {
            return video;
        },
    };
</script>


<style scoped>
body {
  margin: 0;
  padding: 0;
}
</style>

<style>
body {
  margin: 0;
  padding: 0;
}

</style>
