import Vue from 'vue'
import Router from 'vue-router'
import InteractiveView from '@/components/InteractiveView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'InteractiveView',
      component: InteractiveView
    }
  ]
})
