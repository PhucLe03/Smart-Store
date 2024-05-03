<template>
    <template v-if="$route.path === '/'">
        <footer class="rounded-lg" style="font-family: 'Comfortaa'; background-color: #F7F9FC;">
            <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center">
                <span class="flex flex-col text-sm font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 bg-transparent">Copyright © 2023&nbsp;<a class="font-semibold" style="color: #00CDE8; margin-right: 50px;">SmartKonbini</a>
                </span>
                <ul class="flex flex-col text-sm font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 bg-transparent">
                    <li>
                        <a href="/hc" class="hover:underline me-4 md:me-6">Help Center</a>
                    </li>
                    <li>
                        <a href="/terms" class="hover:underline me-4 md:me-6">Terms and Conditions</a>
                    </li>
                    <li>
                        <a href="/privacy" class="hover:underline me-4 md:me-6">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="/contact" class="hover:underline me-4 md:me-6">Contact</a>
                    </li>
                </ul>
            </div>
        </footer>
    </template>
    <template v-else>
        <footer class="bg-white rounded-lg" style="font-family: 'Comfortaa';">
            <div class="w-full mx-auto max-w-screen-xl p-4 md:flex md:items-center">
                <span class="flex flex-col text-sm font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white">Copyright © 2023&nbsp;<a class="font-semibold" style="color: #00CDE8; margin-right: 50px;">SmartKonbini</a>
                </span>
                <ul class="flex flex-col text-sm font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white">
                    <li>
                        <a href="/hc" class="hover:underline me-4 md:me-6">Help Center</a>
                    </li>
                    <li>
                        <a href="/terms" class="hover:underline me-4 md:me-6">Terms and Conditions</a>
                    </li>
                    <li>
                        <a href="/privacy" class="hover:underline me-4 md:me-6">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="/contact" class="hover:underline me-4 md:me-6">Contact</a>
                    </li>
                </ul>
            </div>
        </footer>
    </template>
</template>