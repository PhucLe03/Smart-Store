<template>
    <div class="diagonal-split-background min-h-screen w-full top-0 left-0 z-0" style="font-family: Comfortaa;">
        <div class="max-w-screen-xl flex flex-wrap justify-between items-center mx-auto p-4" >
            <div class="grid grid-cols-1 md:grid-cols-2 flex justify-center items-center w-full mr-10 mb-16 gap-2">
                <div class="mt-32 ml-36"> 
                    <img src="/images/intro.png" alt="print" style="height:400px; width:400px; transform: rotate(0deg);" >
                </div>
                <div>
                    <div class="text-white"> 
                        <div class="flex justify-center items-center text-4xl font-bold mb-8">Smart Konbini</div>
                        <div class="flex justify-center text-lg items-center">A website that manages smart convenient store with AI</div>
                        <div class="flex justify-center text-lg items-center">of Ho Chi Minh City University of Technology.</div>
                    </div>
                    <div class="flex justify-center items-center">
                        <button type="button" @click="$router.push('/login')" class="mt-12 w-40 bg-blue-500 transition duration-300 ease-in-out hover:bg-blue-600 text-white font-semibold rounded-full text-sm px-4 py-2 text-center">Get started</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="max-w-screen-xl flex flex-wrap justify-between items-center mx-auto p-4" >
            <div class="grid grid-cols-1 md:grid-cols-2 flex justify-center items-center w-full mb-12 mt-4 gap-16 ml-20 mr-20">
                <div>
                    <div class="text-gray-900 md:ml-16"> 
                        <div class="flex justify-end items-center text-2xl font-bold mb-4" style="color: #2d9881">Start Exploring</div>
                        <div class="flex justify-end text-lg items-end text-right">We provides a lot of features for users, and you can see our introductions page below to get through some of them.</div>
                    </div>
                    <div class="flex justify-end items-center">
                        <button type="button" @click="$router.push('/about')" class="mt-4 text-lg transition duration-300 ease-in-out text-blue-700 hover:text-blue-500 font-semibold text-center">Explore ></button>
                    </div>
                </div>
                <div>
                    <img src="/images/about_us.png" alt="about" style="scale:50%" >
                </div>
            </div>
        </div>
    </div>

    <hr class="relative">
    <img src="/images/hcmut.png" alt="Logo" class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2" style="width: 75px; height: 75px;">

    <div class="horizontal-split-background w-full top-0 left-0 z-0" style="font-family: Comfortaa;">
        <div class="max-w-screen-xl flex flex-wrap justify-between items-center mx-auto p-4">
            <div class="grid grid-cols-1 md:grid-cols-2 flex justify-center items-center w-full mt-16 gap-16 ml-20 mr-20 mb-16">
                <div>
                    <div class="text-gray-900 md:ml-16"> 
                        <svg class="w-12 h-12 mb-4" style="color: #777777" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" stroke="gray" stroke-width="0.5" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M7.324 9.917A2.479 2.479 0 0 1 7.99 7.7l.71-.71a2.484 2.484 0 0 1 2.222-.688 4.538 4.538 0 1 0-3.6 3.615h.002ZM7.99 18.3a2.5 2.5 0 0 1-.6-2.564A2.5 2.5 0 0 1 6 13.5v-1c.005-.544.19-1.072.526-1.5H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h7.687l-.697-.7ZM19.5 12h-1.12a4.441 4.441 0 0 0-.579-1.387l.8-.795a.5.5 0 0 0 0-.707l-.707-.707a.5.5 0 0 0-.707 0l-.795.8A4.443 4.443 0 0 0 15 8.62V7.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.12c-.492.113-.96.309-1.387.579l-.795-.795a.5.5 0 0 0-.707 0l-.707.707a.5.5 0 0 0 0 .707l.8.8c-.272.424-.47.891-.584 1.382H8.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1.12c.113.492.309.96.579 1.387l-.795.795a.5.5 0 0 0 0 .707l.707.707a.5.5 0 0 0 .707 0l.8-.8c.424.272.892.47 1.382.584v1.12a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1.12c.492-.113.96-.309 1.387-.579l.795.8a.5.5 0 0 0 .707 0l.707-.707a.5.5 0 0 0 0-.707l-.8-.795c.273-.427.47-.898.584-1.392h1.12a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5ZM14 15.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5Z"/>
                        </svg>

                        <div class="flex justify-start items-center text-2xl font-bold mb-4" style="color: #259AF3">Customer</div>
                        <div class="flex justify-start text-lg items-start">A person use FaceID to buy goods in convenient store.</div>
                    </div>
                </div>
                <div>
                    <div class="text-gray-900 md:mr-16"> 
                        <svg class="w-12 h-12 mb-4" style="color: #777777" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="20" stroke="gray" stroke-width="0.5" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M19.728 10.686c-2.38 2.256-6.153 3.381-9.875 3.381-3.722 0-7.4-1.126-9.571-3.371L0 10.437V18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-7.6l-.272.286Z"/>
                            <path d="m.135 7.847 1.542 1.417c3.6 3.712 12.747 3.7 16.635.01L19.605 7.9A.98.98 0 0 1 20 7.652V6a2 2 0 0 0-2-2h-3V3a3 3 0 0 0-3-3H8a3 3 0 0 0-3 3v1H2a2 2 0 0 0-2 2v1.765c.047.024.092.051.135.082ZM10 10.25a1.25 1.25 0 1 1 0-2.5 1.25 1.25 0 0 1 0 2.5ZM7 3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v1H7V3Z"/>
                        </svg>
                        <div class="flex justify-start items-center text-2xl font-bold mb-4" style="color: #B7892B">Manager</div>
                        <div class="flex justify-start text-lg items-start">A person who manages goods and customer by bar code and FaceID.</div>
                    </div>
                </div>
            </div>

            <div class="text-gray-900 mx-auto text-center mb-16"> 
                <svg class="w-20 h-20 mb-4" viewBox="0 -2 28 28" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" stroke-linecap="round" stroke-linejoin="round" fill="currentColor" stroke="gray" stroke-width="0.5" style="color: #777777; display: block; margin: auto">
                    <path d="m.482 24c-.215-.002-.389-.177-.389-.393v-1.783c0-.217.176-.393.393-.393h.001 1.346v-12.759s0 0 0-.001c0-.085.014-.167.039-.244l-.002.006c-.754-.216-1.379-.676-1.8-1.287l-.007-.011c-.04-.061-.063-.135-.063-.214 0 0 0 0 0-.001v-6.526c0-.217.176-.393.393-.394h27.013.001c.217 0 .393.176.393.393v.001 6.526c0 .079-.024.153-.064.215l.001-.002c-.611.855-1.582 1.418-2.687 1.468h-.008q0 .034 0 .069v12.76h1.09.001c.217 0 .393.176.393.393v1.783c0 .217-.176.393-.393.393h-.001zm22.99-2.965v-12.362c0-.07.009-.138.026-.202l-.001.006c-.596-.154-1.112-.444-1.53-.836l.002.002c-.676.607-1.574.978-2.56.978-.04 0-.08-.001-.12-.002h.006c-.034.001-.073.002-.113.002-.993 0-1.897-.378-2.577-.998l.003.003c-.677.617-1.581.995-2.574.995-.04 0-.079-.001-.119-.002h.006c-.034.001-.073.002-.112.002-.993 0-1.897-.378-2.578-.998l.003.003c-.677.617-1.582.995-2.575.995-.043 0-.085-.001-.128-.002h.006c-.034.001-.073.002-.112.002-.993 0-1.898-.378-2.578-.998l.003.003c-.643.594-1.499.967-2.441.993h-.005q0 .029 0 .058v12.359h1.156v-5.253c0-.217.176-.393.393-.393h.001 4.649.001c.217 0 .393.176.393.393v5.253zm-4.177-13.202c.03.001.065.002.1.002.813 0 1.553-.318 2.1-.837l-.001.001c-.006-.025-.009-.054-.009-.083v-6.129h-4.41v6.133c.001.008.001.017.001.027s0 .019-.001.028v-.001c.546.532 1.293.861 2.117.861.037 0 .073-.001.11-.002h-.005zm-10.758 0c.032.001.069.002.106.002.824 0 1.571-.328 2.118-.861l-.001.001c-.001-.008-.001-.017-.001-.027s0-.019.001-.028v.001-6.133h-4.448v6.133c.001.008.001.017.001.027s0 .019-.001.028v-.001c.546.532 1.293.861 2.117.861.038 0 .075-.001.112-.002h-.005zm2.873 10.495c-.217 0-.393-.176-.393-.393v-6.82-.001c0-.217.176-.393.393-.393h11.008.001c.217 0 .393.176.393.393v.001 6.821c0 .217-.176.393-.393.393h-.001z">
                    </path>
                </svg>

                <div class="flex justify-center items-center text-2xl font-bold mb-4" style="color: #1DA09C">Smart Shopping</div>
                <div class="flex justify-center text-lg items-center">Customers can register and log in to the app using FaceID </div>
                <div class="flex justify-center text-lg items-center">and their ID for purchasing goods and making payments.</div>
            </div>

            <!-- <div id="gallery" class="relative w-full mb-8 ml-16 mr-16" data-carousel="slide">
                <div class="relative overflow-hidden rounded-lg" style="height:600px">
                    <div class="hidden duration-700 ease-in-out" data-carousel-item>
                        <img src="/images/slider/1.png" class="absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="">
                    </div>
                    <div class="hidden duration-700 ease-in-out" data-carousel-item>
                        <img src="/images/slider/2.png" class="absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="">
                    </div>
                    <div class="hidden duration-700 ease-in-out" data-carousel-item="active">
                        <img src="/images/slider/3.png" class="absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="">
                    </div>
                    <div class="hidden duration-700 ease-in-out" data-carousel-item>
                        <img src="/images/slider/4.png" class="absolute block max-w-full h-auto -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2" alt="">
                    </div>
                </div>
                <button type="button" class="absolute top-0 start-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none" data-carousel-prev>
                    <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                        <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
                        </svg>
                        <span class="sr-only">Previous</span>
                    </span>
                </button>
                <button type="button" class="absolute top-0 end-0 z-30 flex items-center justify-center h-full px-4 cursor-pointer group focus:outline-none" data-carousel-next>
                    <span class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/30 group-hover:bg-white/50 group-focus:ring-4 group-focus:ring-white group-focus:outline-none">
                        <svg class="w-4 h-4 text-white dark:text-gray-800 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                        </svg>
                        <span class="sr-only">Next</span>
                    </span>
                </button>
            </div> -->
        </div>
    </div>
    <div class="horizontal-split-background2 w-full left-0 z-0 pb-8">
        <hr class="relative">
        <img src="/images/VNU_HCM.png" alt="Logo" class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2" style="width: 75px; height: 75px;">

        <div class="flex justify-center text-lg items-center text-red-500 font-semibold mt-12" style="font-family: Comfortaa;">Made with&nbsp;<span><svg class="w-6 h-6 text-red-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
            <path d="M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z"/>
            </svg></span>&nbsp;from&nbsp;<span style="color:#00cde8"> SmartKonbini </span>
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'

export default {
    name: "Home",
    data () {

    },

    beforeRouteEnter(to, from, next) {
        const store = useStore()
        store.dispatch('logout')
        next()
    },
}
</script>

<style>
.diagonal-split-background{
  background-color: #F7F9FC;
  background-image: -webkit-linear-gradient(80deg, #F7F9FC 50%, #303030 50.5%);
  background-repeat: no-repeat;
}

.horizontal-split-background{
  background-color: #ffffff;
}

.horizontal-split-background2{
  background-color: #F7F9FC;
}
</style>