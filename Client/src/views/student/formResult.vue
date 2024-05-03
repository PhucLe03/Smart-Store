<template>
    <div class="flex items-center justify-center text-5xl font-semibold mt-11" style="font-family: 'Comfortaa';">Buddy Matching</div>
    <div class="flex items-center justify-center text-xl mt-5 mb-12" style="font-family: 'Comfortaa';">Thank you for using our website</div>
    <div class="max-w-screen-xl flex flex-col items-center justify-center mx-auto p-4" style="font-family: 'Comfortaa';">
        <div class="text-center text-xl mt-5 mb-4 block"><span class="font-semibold">Note:</span>&nbsp;Kindly check out our&nbsp;<router-link to="/result" class="text-blue-700 hover:text-blue-500" style="cursor: pointer;">Result</router-link>&nbsp;page to keep track of the form results.</div>
        <button type="button" @click="$router.push('/student')" class="mb-24 mt-2 w-60 text-blue-500 border border-blue-500 hover:bg-blue-500 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-semibold rounded-lg text-sm px-4 py-2 text-center">Return to Homepage</button>

        <div class="grid grid-cols-1 md:grid-cols-3" style="font-family: 'Comfortaa';"> 
            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0 md:mr-10">
                <span class="text-xl font-bold block">Buddy Matching System</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #F2E67C 0%, #FFFFFF 100%); height: 2px"></span>
                <span>A place to learn, grow and adapt together. From this system you can build up social relationships and help other people.</span>
            </div>

            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0">
                <span class="text-xl font-bold block">Security Guaranteed</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #FF3F38 0%, #FFFFFF 100%); height: 2px"></span>
                <span>All of the data you provided to us will be protected carefully. We promise to not sharing them anywhere beyond our website.</span>
            </div>
                
            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0 md:ml-10">
                <span class="text-xl font-bold block">Easy To Use</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #00CDE8 0%, #FFFFFF 100%); height: 2px"></span>
                <span>Matching buddies will be way easier using our friendly user interface and easy-to-follow instructions on this website.</span>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 mt-2 md:mt-20 mb-20" style="font-family: 'Comfortaa';"> 
            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0 md:mr-10">
                <span class="text-xl font-bold block">Integrated Payout System</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #5cfa79 0%, #FFFFFF 100%); height: 2px"></span>
                <span>We also provide an integrated payout system for OISP in order to send rewards to people who eager to help others. </span>
            </div>

            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0">
                <span class="text-xl font-bold block">Privilege Account System</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #fa5cf2 0%, #FFFFFF 100%); height: 2px"></span>
                <span>Any students who want to join the community can register for an account. But only verified OISP members can register for one.</span>
            </div>
                
            <div class="w-4/5 mx-auto text-left mb-8 md:mb-0 md:ml-10">
                <span class="text-xl font-bold block">Accessible Anywhere</span>
                <span style="display:block; margin-top:5px; margin-bottom:20px; background: linear-gradient(90deg, #f7a828 0%, #FFFFFF 100%); height: 2px"></span>
                <span>You can get access to this website anywhere, anytime and in any situations possible. We will not limit the distance for your convenience.</span>
            </div>
        </div>
    </div>
</template>
  

<script>
import { render } from 'vue';

//   import axios from "../api/api.js";
//   import swal from "sweetalert";
    export default {
        name: "FormResultView",
        data() {

        },
        methods: {

        }
    };
</script>
