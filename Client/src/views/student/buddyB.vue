<template>
    <div class="flex items-center justify-center text-5xl font-semibold mt-11" style="font-family: 'Comfortaa';">Buddy B</div>
    <div class="flex items-center justify-center text-xl mt-5 mb-20" style="font-family: 'Comfortaa';">All of your buddy B in one place</div>
    <div class="max-w-screen-xl flex flex-wrap justify-center items-center mx-auto p-4 mb-16"  style="font-family: 'Comfortaa';">
        <div class="grid grid-cols-1 md:grid-cols-2 mb-6 gap-10 w-full z-20">
            <div class="w-full relative">
                <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <input type="text" id="text" v-model="querySearch" @keyup.enter="searchName(querySearch)" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm font-semibold rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pl-10" placeholder="Buddy B">
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
                        <th scope="col" class="px-6 py-3" style="width: 100px;">
                            <div class="flex items-center">
                                No.
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <div class="flex items-center" style="width: 250px;">
                                Buddy B
                                <a @click="() => changeOrder(0, 'name')" class="hover:cursor-pointer"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            <div class="flex items-center" style="width: 200px;">
                                Student ID
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
                        <th scope="col" class="px-6 py-3" style="width: 135px;">
                            <div class="flex items-center">
                                Grade
                                <a @click="() => changeOrder(2, 'semesterScore')" class="hover:cursor-pointer"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 135px;">
                            <div class="flex items-center">
                                Target
                                <a @click="() => changeOrder(3, 'scoreReq')" class="hover:cursor-pointer"><svg class="w-3 h-3 ms-1.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M8.574 11.024h6.852a2.075 2.075 0 0 0 1.847-1.086 1.9 1.9 0 0 0-.11-1.986L13.736 2.9a2.122 2.122 0 0 0-3.472 0L6.837 7.952a1.9 1.9 0 0 0-.11 1.986 2.074 2.074 0 0 0 1.847 1.086Zm6.852 1.952H8.574a2.072 2.072 0 0 0-1.847 1.087 1.9 1.9 0 0 0 .11 1.985l3.426 5.05a2.123 2.123 0 0 0 3.472 0l3.427-5.05a1.9 1.9 0 0 0 .11-1.985 2.074 2.074 0 0 0-1.846-1.087Z"/>
                                    </svg>
                                </a>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3" style="width: 135px;">
                            <div class="flex items-center">
                                Passed
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-white border-b" v-for="(buddy, index) in toShow.slice((this.pagination.page - 1) * this.pagination.perPage, Math.min(this.pagination.page * this.pagination.perPage, this.buddies.length))" :key="index">
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
                            {{ buddy.semesterScore }}
                        </td>
                        <td class="px-6 py-4">
                            {{ buddy.scoreReq }}
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
import axios from '../../api/api.js'

export default {
    name: 'StudentResult',
    data () {
        return {
            buddies: [],
            toShow: [],
            sort_list: [0, 0, 0, 0],
            filterName: '',
            filterSubject: '',
            pagination: {
                page: 1,
                perPage: 20,
                total: 0,
                extra: 0,
                pageRange: []
            },
        }
    },
    async mounted() {
        this.getBuddiesB();
    },
    computed: {
        currentUser() {
        return this.$store.state.user;
        }
    },
    methods: {
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
        async getBuddiesB(order=null, columnName=null) {
            let _id = this.currentUser.id;
            let res = null;
            if(order === null || columnName === null) {
                res = await axios.get(`/buddyBbyA/${_id}`);
                // res = await axios.get(`/buddiesB`);
            } 
            else {
                res = await axios.get(`/buddyBbyA/${_id}?order=${order}&column=${columnName}`);
                // res = await axios.get(`/buddiesB?order=${order}&column=${columnName}`);
            }
            console.log(res.data)
            this.buddies = res.data;
            this.toShow = this.buddies
            console.log(this.toShow)
            this.totalPages()
            this.pageNumbers() 
        },
        changeOrder(idx, columnName) {
            this.sort_list[idx] === 0? this.getBuddiesB('asc', columnName): this.getBuddiesB('desc', columnName);
            this.sort_list = this.sort_list.map((value, index) => index === idx ? value ^ 1 : 0);
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
            await this.getBuddiesB();
            if(this.filterName !== '' && this.filterName !== null){
                let filteredBuddies = this.buddies.filter(buddy => buddy.name.includes(this.filterName));
                this.buddies = filteredBuddies;
            }
            if(this.filterSubject !== '' && this.filterSubject !== null){
                let filteredBuddies = this.buddies.filter(buddy => buddy.subjectCode.includes(this.filterSubject));
                this.buddies = filteredBuddies;
            }
            console.log(this.buddies);
            this.toShow = this.buddies;
            this.totalPages()
            this.pageNumbers() 
        }
    }
}
</script>