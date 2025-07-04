<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div v-if="!loggedIn" class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-purple-700">Lecturer Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block mb-1 font-medium">Lecturer ID</label>
          <input v-model="username" type="text" class="w-full border rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 font-medium">Password</label>
          <input v-model="password" type="password" class="w-full border rounded px-3 py-2" />
        </div>
        <div v-if="error" class="mb-4 text-red-600">{{ error }}</div>
        <button type="submit" class="w-full bg-purple-700 text-white py-2 rounded font-bold hover:bg-purple-800 transition">Login</button>
      </form>
    </div>
    <div v-else class="bg-white p-8 rounded shadow-md w-full max-w-3xl">
      <h2 class="text-2xl font-bold mb-4 text-purple-700">Welcome, Lecturer!</h2>
      <nav class="mb-6">
        <ul class="flex space-x-6">
          <li><button @click="section = 'dashboard'" :class="sectionBtn('dashboard')">Dashboard</button></li>
          <li><button @click="section = 'students'" :class="sectionBtn('students')">Students</button></li>
          <li><button @click="section = 'assignments'" :class="sectionBtn('assignments')">Assignments</button></li>
        </ul>
      </nav>
      <div v-if="section === 'dashboard'">
        <h3 class="text-lg font-bold mb-2">Dashboard (Mock)</h3>
        <p class="text-gray-600 mb-4">Overview of your teaching activities. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Upcoming Classes: 2</li>
          <li>Pending Assignments: 5</li>
        </ul>
      </div>
      <div v-else-if="section === 'students'">
        <h3 class="text-lg font-bold mb-2">Students (Mock)</h3>
        <p class="text-gray-600 mb-4">Manage your students. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Dalitso Zulu</li>
          <li>Jane Smith</li>
        </ul>
      </div>
      <div v-else-if="section === 'assignments'">
        <h3 class="text-lg font-bold mb-2">Assignments (Mock)</h3>
        <p class="text-gray-600 mb-4">View and grade assignments. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Math Assignment 1 - Needs Grading</li>
          <li>Science Project - Graded</li>
        </ul>
      </div>
      <button @click="logout" class="mt-8 bg-gray-200 px-4 py-2 rounded hover:bg-gray-300">Log out</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const username = ref('');
const password = ref('');
const error = ref('');
const loggedIn = ref(false);
const section = ref('dashboard');

function login() {
  if (!username.value || !password.value) {
    error.value = 'Please enter both Lecturer ID and password.';
    return;
  }
  error.value = '';
  loggedIn.value = true;
}
function logout() {
  loggedIn.value = false;
  username.value = '';
  password.value = '';
  section.value = 'dashboard';
}
function sectionBtn(name) {
  return [
    'px-4 py-2 rounded',
    section.value === name ? 'bg-purple-700 text-white' : 'bg-gray-100 text-purple-700 hover:bg-purple-100',
    'transition font-semibold'
  ].join(' ');
}
</script>

<style scoped>
body { background: #f3f4f6; }
</style> 