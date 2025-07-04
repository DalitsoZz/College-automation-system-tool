import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
  },
  {
    path: '/student',
    name: 'Student',
    component: () => import('../views/Student.vue'),
  },
  {
    path: '/lecturer',
    name: 'Lecturer',
    component: () => import('../views/Lecturer.vue'),
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/Admin.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 