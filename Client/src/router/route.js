import { createRouter, createWebHistory } from 'vue-router'

// import Webpages
import Home from '../views/Home.vue'
import LoginView from '../views/Login.vue'
import RegisterView from '../views/Register.vue'
import About from '../views/About.vue'
import NotFound from '../views/NotFound.vue'

import StudentHomeView from '../views/student/studentHome.vue'
import FormView from '../views/student/formView.vue'
import FormResultView from '../views/student/formResult.vue'
import buddyBView from '../views/student/buddyB.vue'
import buddyAView from '../views/student/buddyA.vue'

import AdminHomeView from '../views/oisp/adminHome.vue'
import MatchingView from '../views/oisp/matching.vue'
import BuddyResult from '../views/oisp/buddyResult.vue'
// import PR2152250 from '../views/OISPView/PR2152250'


//setting up addresses with their associated webpages
const routes = [
    { 
        path: '/',
        component: Home,
        meta: {
            title: 'Home - Smart Konbini',
        }
    },
    {
        path: '/login',
        component: LoginView,
        meta: {
            title: 'Login - Smart Konbini',
        }
    },
    {
        path: '/register',
        component: RegisterView,
        meta: {
            title: 'Register - Smart Konbini',
        }
    },
    {
        path: '/student',
        component: StudentHomeView,
        meta: {
            title: 'Home - Smart Konbini',
        }
    },
    {
        path: '/about',
        component: About,
        meta: {
            title: 'About - Smart Konbini',
        }
    },
    {
        path: '/form',
        component: FormView,
        meta: {
            title: 'Form - Smart Konbini',
        }
    },
    {
        path: '/form-result',
        component: FormResultView,
        meta: {
            title: 'Finish - Smart Konbini',
        }
    },
    {
        path: '/buddyB',
        component: buddyBView,
        meta: {
            title: 'Your Buddy B - Smart Konbini',
        }
    },
    {
        path: '/buddyA',
        component: buddyAView,
        meta: {
            title: 'Your Buddy A - Smart Konbini',
        }
    },
    {
        path: '/admin',
        component: AdminHomeView,
        meta: {
            title: 'Home - Smart Konbini',
        }
    },


    {
        path: '/buddy-result',
        component: BuddyResult,
        meta: {
            title: 'Buddy Result - Smart Konbini',
        }
    },
    // {
    //     path: '/pr2152250',
    //     component: PR2152250,
    //     meta: {
    //         title: 'Phoenix Result - Smart Konbini',
    //     }
    // },
    {
        path: '/match',
        component: MatchingView,
        meta: {
            title: 'Matching - Smart Konbini',
        }
    },

    {
        path: '/:pathMatch(.*)*',
        component: NotFound,
        meta: {
            title: '404 Not Found',
        },
    },
]

// create the router object with active class to highlight link that are currently visiting (client side)
const router = createRouter({
    history: createWebHistory(),
    routes,
    linkActiveClass: "active",
    linkExactActiveClass: "active",
})

// this is for loading the title of each page before routing to the actual page itself, we load it via the meta tag
import store from '../store'

router.beforeEach((to, from, next) => {

    document.title = to.meta?.title ?? 'Blank'
    const publicPages = ['/login', '/register', '/', '/about'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    const studentRoutes = ['/form', '/form-result', '/student-result', '/student']
    const adminRoutes = ['/match', '/oisp-result', '/admin']
    // const formPaths = ['/form', '/form-result']
  
    // trying to access a restricted page + not logged in
    // redirect to login page

    if (authRequired && !loggedIn) {
        next('/');
    } 
    else if (store.state.user && ['/login', '/register'].includes(to.path)) {
        next('/');
    } 
    else if (store.state.user && store.state.user.role === 'ROLE_STUDENT' && adminRoutes.includes(to.path)) {
        next('/');
    }
    else if (store.state.user && store.state.user.role === 'ROLE_OISP' && studentRoutes.includes(to.path)) {
        next('/');
    }
    else {
        next();
    }
})

export default router;