<template>
    <body>
        <div class="max-w-md mx-auto bg-white rounded-lg p-6 shadow-md mt-16" style="font-family: 'Comfortaa';">
            <div class="flex items-center justify-center text-2xl font-semibold whitespace-nowrap mb-4" style="color: #00CDE8; ">Galacticos</div>  
            <div class="flex items-center justify-center text-xl font-semibold whitespace-nowrap mb-8" style="">Buddy Matching System</div>  
            <a class="flex items-center justify-center text-xl font-semibold whitespace-nowrap mb-8" style="" href="/camera">Camera</a>
            <form class="mb-4" @submit.prevent="handleLogin">
                <div class="mb-6">
                    <input type="email" id="email" v-model="loginUser.email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Your email" required>
                </div>
                <div class="mb-6">
                    <input type="password" id="password" v-model="loginUser.password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Your password" required>
                </div>
                <div class="flex items-start mb-6">
                    <div class="flex items-center h-5">
                    <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300">
                    </div>
                    <label for="remember" class="ms-2 text-sm text-gray-900">Remember me</label>
                </div>
                <p v-if="message" class="text-sm text-red-500 mb-4 text-semibold">{{ message }}</p>
                <button type="submit" class="w-full text-blue-500 border border-blue-500 hover:bg-blue-500 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-semibold rounded-lg text-sm px-4 py-2 text-center">Sign in</button>
            </form>
            <div class="flex justify-between text-sm mb-4" style="cursor: pointer;">
                <a class="hover:underline">Forgot password?</a>
                <a href="/register" class="hover:underline">Sign up</a>
            </div>

            <div class="flex items-center justify-center text-sm mb-3">
                or you can sign in with
            </div>

            <div class="flex justify-center space-evenly">
                <div class="mx-5">
                    <svg class="w-8 h-8 text-white text-bold rounded-full bg-gray-400 hover:bg-red-600 transition duration-300" style="cursor: pointer; padding: 5px;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 19">
                        <path fill-rule="evenodd" d="M8.842 18.083a8.8 8.8 0 0 1-8.65-8.948 8.841 8.841 0 0 1 8.8-8.652h.153a8.464 8.464 0 0 1 5.7 2.257l-2.193 2.038A5.27 5.27 0 0 0 9.09 3.4a5.882 5.882 0 0 0-.2 11.76h.124a5.091 5.091 0 0 0 5.248-4.057L14.3 11H9V8h8.34c.066.543.095 1.09.088 1.636-.086 5.053-3.463 8.449-8.4 8.449l-.186-.002Z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <div>
                    <svg class="w-8 h-8 text-white text-bold rounded-full bg-gray-400 hover:bg-blue-500 transition duration-300" style="cursor: pointer; padding: 5px;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 8 19">
                        <path fill-rule="evenodd" d="M6.135 3H8V0H6.135a4.147 4.147 0 0 0-4.142 4.142V6H0v3h2v9.938h3V9h2.021l.592-3H5V3.591A.6.6 0 0 1 5.592 3h.543Z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <div class="mx-5">
                    <svg class="w-8 h-8 text-gray-400 text-bold hover:text-black transition duration-300" style="cursor: pointer;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 .333A9.911 9.911 0 0 0 6.866 19.65c.5.092.678-.215.678-.477 0-.237-.01-1.017-.014-1.845-2.757.6-3.338-1.169-3.338-1.169a2.627 2.627 0 0 0-1.1-1.451c-.9-.615.07-.6.07-.6a2.084 2.084 0 0 1 1.518 1.021 2.11 2.11 0 0 0 2.884.823c.044-.503.268-.973.63-1.325-2.2-.25-4.516-1.1-4.516-4.9A3.832 3.832 0 0 1 4.7 7.068a3.56 3.56 0 0 1 .095-2.623s.832-.266 2.726 1.016a9.409 9.409 0 0 1 4.962 0c1.89-1.282 2.717-1.016 2.717-1.016.366.83.402 1.768.1 2.623a3.827 3.827 0 0 1 1.02 2.659c0 3.807-2.319 4.644-4.525 4.889a2.366 2.366 0 0 1 .673 1.834c0 1.326-.012 2.394-.012 2.72 0 .263.18.572.681.475A9.911 9.911 0 0 0 10 .333Z" clip-rule="evenodd"/>
                    </svg>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
//import axios from "../api/api.js";
//import swal from "sweetalert";

export default {
    name: "LoginView",
    data() {
        return {
            message: "",
            loginUser: {
                email: "",
                password: ""
            }
        };
    },
    methods: {
        async handleLogin() {
            try {
                await this.$store.dispatch("login", this.loginUser);
                const user = this.$store.state.user;
                console.log("Before if: ",user);
                if (user) {
                    console.log(user);
                    console.log("Role: ", user.role);
                    if (user.role === 'ROLE_STUDENT') {
                        this.$router.push({path: "/student"});
                    } else if (user.role === 'ROLE_OISP') {
                        this.$router.push({path: "/admin"});
                    }else{
                        this.$router.push({path: "/"});
                    }
                }
            } catch (error) {
                this.message =
                (error.response &&
                    error.response.data &&
                    error.response.data.message) ||
                error.message ||
                error.toString();
            }
        }
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
