import Vue from 'vue'
import Router from 'vue-router'
import Exemplo from '@/components/exemplo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Exemplo',
      component: Exemplo
    }
  ]
})
