import { createRouter, createWebHashHistory } from 'vue-router'
// import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    redirect: '/index'
    // name: 'Home',
    // component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/create',
    name: 'create',
    component: () => import('../components/Create.vue')
  },
  {
    path: '/edit/:id',
    name: 'edit',
    component: () => import('../components/Edit.vue')
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('../components/Index.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
