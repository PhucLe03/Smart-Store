<template> 
    <div class="max-w-screen-xl flex flex-wrap justify-between items-center mx-auto p-4">
        <div class="flex flex-col md:flex-row items-center justify-center">
            <div style="font-family: 'Comfortaa';">
                <p class="text-8xl font-bold text-gray-800 mb-10">Oops!</p>
                <p class="text-2xl font-semibold text-gray-600">Sorry, but we can't find the page</p>
                <p class="text-2xl font-semibold text-gray-600 mb-10"> you are looking for...</p>
                <p class="text-xl font-semibold text-gray-600 mb-10">Error code: <span class="text-xl font-bold text-gray-900">404</span></p>
                <button @click="goBack" class="text-xl text-blue-500 hover:underline mb-100">Go back</button>
            </div>
            <img class="object-scale-down w-full md:w-1/2 h-auto" src="/images/404.png" alt="404 Not Found">
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
    name: "NotFound",
    setup() {
        const store = useStore()
        const router = useRouter()

        const goBack = () => {
            if (store.state.user.role === 'ROLE_STUDENT') {
                router.push('/student')
            } else if (store.state.user.role === 'ROLE_OISP') {
                router.push('/admin')
            } else {
                router.push('/')
            }
        }

        return {
            goBack
        }
    }
}
</script>

<style>
</style>