import { createRouter, createWebHistory } from 'vue-router'

// import Webpages
import Home from '../views/Home.vue'
import LoginView from '../views/Login.vue'
import RegisterView from '../views/Register.vue'
import About from '../views/About.vue'
import NotFound from '../views/NotFound.vue'

import StudentHomeView from '../views/student/studentHome.vue'
import FormView from '../views/Student/formView.vue'
import FormResultView from '../views/Student/formResult.vue'
import buddyBView from '../views/Student/buddyB.vue'
import buddyAView from '../views/Student/buddyA.vue'

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
            title: 'Home - Buddy Matching System',
        }
    },
    {
        path: '/login',
        component: LoginView,
        meta: {
            title: 'Login - Buddy Matching System',
        }
    },
    {
        path: '/register',
        component: RegisterView,
        meta: {
            title: 'Register - Buddy Matching System',
        }
    },
    {
        path: '/student',
        component: StudentHomeView,
        meta: {
            title: 'Home - Buddy Matching System',
        }
    },
    {
        path: '/about',
        component: About,
        meta: {
            title: 'About - Buddy Matching System',
        }
    },
    {
        path: '/form',
        component: FormView,
        meta: {
            title: 'Form - Buddy Matching System',
        }
    },
    {
        path: '/form-result',
        component: FormResultView,
        meta: {
            title: 'Finish - Buddy Matching System',
        }
    },
    {
        path: '/buddyB',
        component: buddyBView,
        meta: {
            title: 'Your Buddy B - Buddy Matching System',
        }
    },
    {
        path: '/buddyA',
        component: buddyAView,
        meta: {
            title: 'Your Buddy A - Buddy Matching System',
        }
    },
    {
        path: '/admin',
        component: AdminHomeView,
        meta: {
            title: 'Home - Buddy Matching System',
        }
    },


    {
        path: '/buddy-result',
        component: BuddyResult,
        meta: {
            title: 'Buddy Result - Buddy Matching System',
        }
    },
    // {
    //     path: '/pr2152250',
    //     component: PR2152250,
    //     meta: {
    //         title: 'Phoenix Result - Buddy Matching System',
    //     }
    // },
    {
        path: '/match',
        component: MatchingView,
        meta: {
            title: 'Matching - Buddy Matching System',
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