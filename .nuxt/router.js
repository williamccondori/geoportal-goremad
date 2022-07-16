import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _655c105c = () => interopDefault(import('../pages/geonetwork.vue' /* webpackChunkName: "pages/geonetwork" */))
const _79121305 = () => interopDefault(import('../pages/geoserver.vue' /* webpackChunkName: "pages/geoserver" */))
const _46a3b2cc = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _2fcc64de = () => interopDefault(import('../pages/rasterlayers.vue' /* webpackChunkName: "pages/rasterlayers" */))
const _12130182 = () => interopDefault(import('../pages/settings.vue' /* webpackChunkName: "pages/settings" */))
const _2d46cc81 = () => interopDefault(import('../pages/styles.vue' /* webpackChunkName: "pages/styles" */))
const _4c956124 = () => interopDefault(import('../pages/vectorlayers.vue' /* webpackChunkName: "pages/vectorlayers" */))
const _13068383 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/geonetwork",
    component: _655c105c,
    name: "geonetwork"
  }, {
    path: "/geoserver",
    component: _79121305,
    name: "geoserver"
  }, {
    path: "/login",
    component: _46a3b2cc,
    name: "login"
  }, {
    path: "/rasterlayers",
    component: _2fcc64de,
    name: "rasterlayers"
  }, {
    path: "/settings",
    component: _12130182,
    name: "settings"
  }, {
    path: "/styles",
    component: _2d46cc81,
    name: "styles"
  }, {
    path: "/vectorlayers",
    component: _4c956124,
    name: "vectorlayers"
  }, {
    path: "/",
    component: _13068383,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
