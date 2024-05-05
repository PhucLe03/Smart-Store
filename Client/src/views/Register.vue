<template>
    <body>
        <div class="max-w-md mx-auto bg-white rounded-lg p-6 shadow-md mt-16 mb-16" style="font-family: 'Comfortaa';">
            <div class="flex items-center justify-center text-2xl font-semibold whitespace-nowrap mb-4" style="color: #00CDE8; ">SmartKonbini</div>  
            <div class="flex items-center justify-center text-xl font-semibold whitespace-nowrap mb-8" style="">Smart Shopping System</div>  
            <form class="mb-4" @submit.prevent="handleRegister">
                <div class="mb-6">
                    <input type="text" id="name" v-model="register.name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Username" required>
                </div>
                <div class="mb-6">
                    <input type="password" id="password" v-model="register.password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Password" required>
                </div>
                <div class="mb-6">
                    <input type="Fullname" id="Fullname" v-model="register.Fullname" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Fullname" required>
                </div>
                <div class="mb-6">
                    <input type="email" id="email" v-model="register.email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Email" required>
                </div>
                <div class="mb-6">
                    <input type="dateofbirth" id="dateofbirth" v-model="register.dateofbirth" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Date of birth(dd/mm/yyyy)" required>
                </div>
                <div class="mb-6" style="display: flex; justify-content: center;">
                    <form class="text-black-500 border border-blue-500 hover:bg-blue-500 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-semibold rounded-lg text-sm px-4 py-2 text-center">
                        <input style="display: none;"  id="file_upload" @change="getinputfile" type="file" accept="image/png, image/gif, image/jpeg, image.jpg"/> 
                        <label style="display: block;" for="file_upload">Upload your ID</label>
                    </form>
                </div>

                <button type="submit" class="w-full text-blue-500 border border-blue-500 hover:bg-blue-500 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-semibold rounded-lg text-sm px-4 py-2 text-center">Sign Up</button>
            </form>
            <div class="flex justify-center text-sm mb-4" style="cursor: pointer;">
                <div>
                    Have an account? <a href="/login" class="hover:underline text-blue-500">Sign In</a>
                </div>
            </div>

        </div>
    </body>
</template>

<script>
//   import axios from "../api/api.js";
//   import swal from "sweetalert";
    export default {
        name: "RegisterView",
        data() {
            return {
                successful: false,
                retypepassword: "",
                message: "",
                register: {
                    role: "",
                    username: "",
                    name: "",
                    email: "",
                    password: "",
                    classCode: "",
                    studentCode: "",
                    bankBranch: "",
                    bankNum: "",
                    OISPCode: "",
                    file_upload: ""
                },
            };
        },
        computed: {
            renderStudent() {
                return this.register.role
            },
            loggedIn() {
                return this.$store.state.status.loggedIn;
            },
        },
        methods: {
            getinputfile(event) {
               let files = event.target.files;
               if (files.length) this.register.file_upload = files[0];
           },
            handleRegister() {
                console.log(this.register)
                this.$store.dispatch("register", this.register).then(
                    (data) => {
                        this.message = data.message;
                        this.successful = true;
                        setTimeout(() => {
                            this.$router.push("/login");
                        }, 2000);
                    },
                    (error) => {
                        this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                        this.successful = false;
                    }
                );
            }
        }
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