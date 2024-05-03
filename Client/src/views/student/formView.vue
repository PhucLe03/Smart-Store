<template>
    <body>
        <div class="max-w-md mx-auto bg-white rounded-lg p-6 shadow-md mt-16 mb-16" style="font-family: 'Comfortaa';">
            <div class="flex items-center justify-center text-2xl font-semibold whitespace-nowrap mb-4" style="color: #00CDE8; ">Galacticos</div>  
            <div class="flex items-center justify-center text-xl font-semibold whitespace-nowrap mb-8" style="">Become a Buddy!</div>  
            <form class="mb-4" @submit.prevent="Submit">
                <div class="mb-6">
                    <fieldset>
                        <legend class="sr-only">Role?</legend>
                        <div class="flex justify-between">
                            <div class="flex items-center mb-4">
                                <input id="buddyA" v-model="Btype" type="radio" name="buddyStatus" value="A" class="w-4 h-4 border-gray-300 focus:ring-2 focus:ring-blue-300" required>
                                <label for="buddyA" class="block ms-2 text-sm font-medium text-gray-900">
                                    I want to be Buddy A!
                                </label>
                            </div>

                            <div class="flex items-center mb-4">
                                <input id="buddyB" v-model="Btype" type="radio" name="buddyStatus" value="B" class="w-4 h-4 border-gray-300 focus:ring-2 focus:ring-blue-300" required>
                                <label for="buddyB" class="block ms-2 text-sm font-medium text-gray-900">
                                    I want to be Buddy B!
                                </label>
                            </div>
                        </div>
                    </fieldset>
                </div>

                <div v-if="renderBuddy === 'A'" class="mb-6">
                    <div class="mb-6">
                        <input type="text" id="subjectCode" v-model="formA.subjectCode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Subject Code (e.g. CO1003)" required>
                    </div>
                    <div class="mb-6">
                        <input type="text" id="subjectGrade" v-model="formA.subjectGrade" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Your Grade (e.g. 8.5)" required>
                    </div>
                    <div class="mb-6">
                        <input type="text" id="naxNoB" v-model="formA.maxNoB" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Maximum No. of Buddy B" required>
                    </div>
                </div>

                <div v-if="renderBuddy === 'B'" class="mb-6">
                    <div class="mb-6">
                        <input type="text" id="subjectCode" v-model="formB.subjectCode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Subject Code (e.g. CO1003)" required>
                    </div>
                    <div class="mb-6">
                        <input type="text" id="scoreReq" v-model="formB.scoreReq" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" placeholder="Your Desired Grade (e.g. 5.0, maximum 7.0)" required>
                    </div>
                </div>
                <p v-if="message" class="text-sm mb-4 text-semibold text-red-500">{{ message }}</p>

                <button type="submit" class="w-full text-blue-500 border border-blue-500 hover:bg-blue-500 hover:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 font-semibold rounded-lg text-sm px-4 py-2 text-center">Send</button>
            </form>

        </div>
    </body>
</template>

<script>
import axios from "../../api/api.js";
//   import swal from "sweetalert";
export default {
    name: "FormView",
    data() {
        return {
            Btype: "",
            formA: {
                name: "",
                classCode: "",
                studentCode: "",
                OCBAccountNo: "",
                OCBBankBranch: "",
                subjectCode: "",
                subjectGrade: "",
                maxNoB: "",
            },
            formB: {
                name: "",
                classCode: "",
                studentCode: "",
                subjectCode: "",
                scoreReq: "",
            },
            message: ""
        };
    },
    computed: {
        renderBuddy() {
            return this.Btype
        },
        currentUser() {
            return this.$store.state.user;
        }
    },
    methods: {
        async Submit() {
            try {
                console.log(this.currentUser)
                if (this.Btype === "A") {
                    const data = this.formA;
                    data.name = this.currentUser.name;
                    data.studentCode = this.currentUser.studentCode;
                    data.classCode = this.currentUser.classCode;
                    data.OCBAccountNo = this.currentUser.bankNum;
                    data.OCBBankBranch = this.currentUser.bankBranch;
                    data.accountId = this.currentUser.id;

                    if (data.subjectGrade < 0 || data.subjectGrade > 10) {
                        throw new Error("The grade should be between 0 and 10!");
                    }

                    await axios.post("/buddyA", data);
                    this.sendForm();
                } 
                else if (this.Btype === "B") {
                    const data = this.formB;
                    data.name = this.currentUser.name;
                    data.studentCode = this.currentUser.studentCode;
                    data.classCode = this.currentUser.classCode;
                    data.accountId = this.currentUser.id;

                    if (data.scoreReq < 0 || data.scoreReq > 7) {
                        throw new Error("The grade should be between 0 and 7!");
                    }

                    await axios.post(`/buddyB`, data);
                    this.sendForm();
                } 
                else {
                    this.message = "Please fill in the form!";
                }
            }
            catch (error) {
                if (error.response && error.response.data) {
                    this.message = error.response.data.message;
                } else {
                    this.message = error.message;
                }
            }
            
        },
        sendForm() {
            this.$router.push("/form-result")
        }
    }
};
</script>
