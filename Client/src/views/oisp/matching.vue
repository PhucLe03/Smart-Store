<template>
    <div class="flex items-center justify-center text-5xl font-semibold mt-11" style="font-family: 'Comfortaa';">Matching</div>
    <div class="flex items-center justify-center text-xl mt-5 mb-20" style="font-family: 'Comfortaa';">Match the buddies together</div>

    <div class="max-w-screen-xl flex flex-wrap justify-center items-center mx-auto p-4"  style="font-family: 'Comfortaa';">
        <div class="grid grid-cols-1 md:grid-cols-2 mb-6 gap-10 w-full z-20">
            <div class="w-full relative">
                <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <input type="text" id="text" v-model="querySearch" @keyup.enter="searchName(querySearch)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pl-10" placeholder="Buddy A">
            </div>
            <div class="w-full relative">
                <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <input type="text" id="text" v-model="querySearch2" @keyup.enter="searchSubject(querySearch2)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pl-10" placeholder="Subject Code">
            </div>
        </div>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mb-8">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" class="px-6 py-3" style="width: 50px;">
                            <div class="flex items-center">
                                No.
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <div class="flex items-center" style="width: 125px;">
                                Buddy A
                                <a @click="() => changeOrder(0, 'name')" class="hover:cursor-pointer"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 200px;">
                            <div class="flex items-center">
                                Subject Code
                                <a @click="() => changeOrder(1, 'subjectCode')" class="hover:cursor-pointer"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 275px;">
                            <div class="flex items-center">
                                Buddy B
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 150px;">
                            <div class="flex items-center">
                                Max Buddy B
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 450px;">
                            <div class="flex items-center">
                                Actions
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b" v-for="(buddy, index) in toShow.slice((this.pagination.page - 1) * this.pagination.perPage, Math.min(this.pagination.page * this.pagination.perPage, this.buddiesA.length))" :key="index">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            {{ index + 1 }} 
                        </th>
                        <td class="px-6 py-4">
                            {{ buddy.name }}
                        </td>
                        <td class="px-6 py-4">
                            {{ buddy.subjectCode }}
                        </td>
                        <td class="px-6 py-4">
                            {{ buddy.buddiesB?.map(s => s.name).join(', ') }}
                        </td>
                        <td class="px-6 py-4">
                            {{ buddy.maxNoB }}
                        </td>
                        <td class="px-6 py-4">
                            <button @click="rejectFunc(buddy._id)" class="mr-8 text-blue-600 hover:text-blue-700 hover:underline" type="button">Reject</button>
                            <button @click="addBuddy(buddy._id, buddy.subjectCode)" class="mr-8 text-blue-600 hover:text-blue-700 hover:underline" type="button">Add Buddy B</button>
                            <button @click="removeBuddy(buddy)" class="mr-8 text-blue-600 hover:text-blue-700 hover:underline" type="button">Remove Buddy B</button>
                        </td>
                        
                    </tr>
                    <tr class="bg-white border-b" v-if="pagination.page === pagination.total" v-for="n in pagination.extra" :key="n">
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                            &nbsp;
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>  

        <div id="popup-background" tabindex="-1" v-if="isPopupOpen" class="z-50">
            <div id="popup-modal">
                <div class="relative p-4 w-full max-w-md max-h-full">
                    <div class="relative bg-white rounded-lg shadow">
                        <button @click="this.isPopupOpen = false" type="button" class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center">
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                            </svg>
                            <span class="sr-only">Close modal</span>
                        </button>
                        <div class="p-4 md:p-5 text-center">
                            <svg class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>
                            </svg>
                            <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Are you sure you want to reject this Buddy A?</h3>
                            <button @click="reject(selectedID)" type="button" class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center me-2">
                                Yes, I'm sure
                            </button>
                            <button @click="this.isPopupOpen = false" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-gray-200 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10">No, cancel</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="popup-background" tabindex="-1" v-if="isPopupOpen2" class="z-50">
            <div id="popup-modal">
                <div class="relative p-4 w-full max-h-full">
                    <div class="relative bg-white rounded-lg shadow">
                        <button @click="this.isPopupOpen2 = false" type="button" class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center">
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                            </svg>
                            <span class="sr-only">Close modal</span>
                        </button>
                        <div class="p-4 md:p-5 text-center">
                            <div class="font-bold text-xl mb-4">
                                Available Buddy B
                            </div>
                            <table class="w-full text-sm text-left rtl:text-right text-gray-500">
                                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                                    <tr>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                No.
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            <div class="flex items-center" style="width: 300px;">
                                                Buddy B
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 200px;">
                                            <div class="flex items-center">
                                                Student Code
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 200px;">
                                            <div class="flex items-center">
                                                Subject Code
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                Target
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                Action
                                            </div>
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="bg-white border-b" v-for="(buddy, index) in buddiesB" :key="index">
                                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                            {{ index + 1 }} 
                                        </th>
                                        <td class="px-6 py-4">
                                            {{ buddy.name }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.studentCode }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.subjectCode }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.scoreReq }}
                                        </td>
                                        <td class="px-6 py-4">
                                            <button @click="addThisBuddy(buddy._id)" class="mr-8 text-blue-600 hover:text-blue-700 hover:underline" type="button">Add</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="popup-background" tabindex="-1" v-if="isPopupOpen3" class="z-50">
            <div id="popup-modal">
                <div class="relative p-4 w-full max-h-full">
                    <div class="relative bg-white rounded-lg shadow">
                        <button @click="this.isPopupOpen3 = false" type="button" class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center">
                            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                            </svg>
                            <span class="sr-only">Close modal</span>
                        </button>
                        <div class="p-4 md:p-5 text-center">
                            <div class="font-bold text-xl mb-4">
                                Current Buddy B
                            </div>
                            <table class="w-full text-sm text-left rtl:text-right text-gray-500">
                                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                                    <tr>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                No.
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3">
                                            <div class="flex items-center" style="width: 300px;">
                                                Buddy B
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 200px;">
                                            <div class="flex items-center">
                                                Student Code
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 200px;">
                                            <div class="flex items-center">
                                                Subject Code
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                Target
                                            </div>
                                        </th>
                                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                                            <div class="flex items-center">
                                                Action
                                            </div>
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="bg-white border-b" v-for="(buddy, index) in currentBuddiesB" :key="index">
                                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
                                            {{ index + 1 }} 
                                        </th>
                                        <td class="px-6 py-4">
                                            {{ buddy.name }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.studentCode }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.subjectCode }}
                                        </td>
                                        <td class="px-6 py-4">
                                            {{ buddy.scoreReq }}
                                        </td>
                                        <td class="px-6 py-4">
                                            <button @click="removeThisBuddy(buddy._id)" class="mr-8 text-blue-600 hover:text-blue-700 hover:underline" type="button">Remove</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <nav aria-label="Page navigation">
            <ul class="flex items-center -space-x-px h-8 text-sm mb-16">
                <li>
                <a @click="pagination.page = Math.max(1, pagination.page - 1)" class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700">
                    <span class="sr-only">Previous</span>
                    <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
                    </svg>
                </a>
                </li>
                <li v-for="(page, index) in pagination.pageRange" :key="index">
                    <a v-if="page === -1" @click="pagination.page = page" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700">...</a>
                    <a v-else @click="pagination.page = page" :aria-current="pagination.page === page ? 'page' : null" :class="pagination.page === page ? 'z-10 flex items-center justify-center px-3 h-8 leading-tight text-blue-600 border border-blue-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700': 'flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700'">{{ page }}</a>
                </li>
                <li>
                <a @click="pagination.page = Math.min(pagination.total, pagination.page + 1)" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700">
                    <span class="sr-only">Next</span>
                    <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
                    </svg>
                </a>
                </li>
            </ul>
        </nav> 
    </div>

</template>

<script>
    import axios from '../../api/api'

    export default {
        name: "OISPMatching",
        data () {
            return {
                buddiesA: [],
                toShow: [],
                sort_list: [0, 0],
                selectedID: null,
                addBuddyAID: null,
                removeBuddyAID: null,
                buddiesB: [],
                currentBuddiesB: [],
                filterName: '',
                filterSubject: '',
                isPopupOpen: false,
                isPopupOpen2: false,
                isPopupOpen3: false,
                pagination: {
                    page: 1,
                    perPage: 20,
                    total: 0,
                    extra: 0,
                    pageRange: []
                },
            }
        },
        mounted() {
          this.getBuddyA();
        },
        methods: {
            rejectFunc(id) {
                this.selectedID = id;
                this.isPopupOpen = true;
            },
            totalPages() {
                if(this.toShow.length === 0)  this.pagination.total = 1;
                else this.pagination.total = Math.ceil(this.toShow.length / this.pagination.perPage);
                
                this.pagination.extra = this.pagination.total * this.pagination.perPage - this.toShow.length;
            },
            pageNumbers() {
                if(this.pagination.total <= 5) {
                    this.pagination.pageRange = Array.from({length: this.pagination.total}, (_, i) => i + 1);
                }
                else {
                    this.pagination.pageRange = [1, 2, -1, this.pagination.total - 1, this.pagination.total];
                }
            },
            changeOrder(idx, columnName) {
                this.sort_list[idx] === 0? this.getBuddyA('asc', columnName): this.getBuddyA('desc', columnName);
                this.sort_list = this.sort_list.map((value, index) => index === idx ? value ^ 1 : 0);
            },
            async getBuddyA(order=null, columnName=null) {
                let res = null
                if(order === null || columnName === null) {
                    res = await axios.get(`/buddiesA`)
                } 
                else {
                    res = await axios.get(`/buddiesA?order=${order}&column=${columnName}`)
                }
                this.buddiesA = res.data
                this.toShow = this.buddiesA
                console.log(this.toShow)
                this.totalPages()
                this.pageNumbers() 
                
            },
            async getBuddyB(subjectCode) {
                const res = await axios.get(`/buddiesB/${subjectCode}`)
                this.buddiesB = res.data;
                console.log(this.buddiesB);
            },
            async addBuddy(id, subjectCode) {
                await this.getBuddyB(subjectCode);
                this.isPopupOpen2 = true;
                this.addBuddyAID = id;
            },
            async removeBuddy(_buddyA) {
                this.currentBuddiesB = _buddyA.buddiesB;
                this.isPopupOpen3 = true;
                this.removeBuddyAID = _buddyA._id;
            },
            async searchName(name) {
                this.filterName = name;
                await this.filter();
            },
            async searchSubject(subject) {
                this.filterSubject = subject;
                await this.filter();
            },
            async filter() {
                await this.getBuddyA();
                if(this.filterName !== '' && this.filterName !== null){
                    let filteredBuddies = this.buddiesA.filter(buddy => buddy.name.includes(this.filterName));
                    this.buddiesA = filteredBuddies;
                }
                if(this.filterSubject !== '' && this.filterSubject !== null){
                    let filteredBuddies = this.buddiesA.filter(buddy => buddy.subjectCode.includes(this.filterSubject));
                    this.buddiesA = filteredBuddies;
                }
                console.log(this.buddiesA);
                this.toShow = this.buddiesA;
                this.totalPages()
                this.pageNumbers() 
            },
            async reject(_id) {
                await axios.delete(`/buddyA/${_id}`)
                await this.getBuddyA()
                this.isPopupOpen = false;
            },
            async addThisBuddy(_id) {
                await axios.put(`/createMatch/${this.addBuddyAID}/${_id}`)
                await this.getBuddyA()
                this.isPopupOpen2 = false;
            },
            async removeThisBuddy(_id) {
                await axios.put(`/deleteMatch/${this.removeBuddyAID}/${_id}`)
                await this.getBuddyA()
                this.isPopupOpen3 = false;
            }
        },
    }
</script>

<style>
#popup-background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    pointer-events: none;
}
#popup-modal {
    pointer-events: auto;
}
</style>