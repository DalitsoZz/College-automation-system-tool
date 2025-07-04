<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div v-if="!loggedIn" class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-green-700">Student Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block mb-1 font-medium">Student ID</label>
          <input v-model="username" type="text" class="w-full border rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 font-medium">Password</label>
          <input v-model="password" type="password" class="w-full border rounded px-3 py-2" />
        </div>
        <div v-if="error" class="mb-4 text-red-600">{{ error }}</div>
        <button type="submit" class="w-full bg-green-700 text-white py-2 rounded font-bold hover:bg-green-800 transition">Login</button>
      </form>
    </div>
    <div v-else class="bg-white p-8 rounded shadow-md w-full max-w-3xl">
      <h2 class="text-2xl font-bold mb-4 text-green-700">Welcome, Student!</h2>
      <nav class="mb-6">
        <ul class="flex space-x-6">
          <li><button @click="section = 'assignments'" :class="sectionBtn('assignments')">Assignments</button></li>
          <li><button @click="section = 'grades'" :class="sectionBtn('grades')">Grades</button></li>
          <li><button @click="section = 'profile'" :class="sectionBtn('profile')">Profile</button></li>
        </ul>
      </nav>
      <div v-if="section === 'assignments'">
        <h3 class="text-lg font-bold mb-2">Assignments (Mock)</h3>
        <p class="text-gray-600 mb-4">View and submit assignments. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Math Assignment 1 - Due: 2025-06-30</li>
          <li>Science Project - Due: 2025-07-10</li>
        </ul>
      </div>
      <div v-else-if="section === 'grades'">
        <h3 class="text-lg font-bold mb-2">Grades (Mock)</h3>
        <p class="text-gray-600 mb-4">View your grades. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Math: A</li>
          <li>Science: B+</li>
        </ul>
      </div>
      <div v-else-if="section === 'profile'">
        <h3 class="text-lg font-bold mb-2">Profile (Mock)</h3>
        <p class="text-gray-600 mb-4">View and edit your profile. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Name: Dalitso Zulu</li>
          <li>Major: Computer Science</li>
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
const section = ref('assignments');

function login() {
  if (!username.value || !password.value) {
    error.value = 'Please enter both Student ID and password.';
    return;
  }
  error.value = '';
  loggedIn.value = true;
}
function logout() {
  loggedIn.value = false;
  username.value = '';
  password.value = '';
  section.value = 'assignments';
}
function sectionBtn(name) {
  return [
    'px-4 py-2 rounded',
    section.value === name ? 'bg-green-700 text-white' : 'bg-gray-100 text-green-700 hover:bg-green-100',
    'transition font-semibold'
  ].join(' ');
}
</script>

<style scoped>
body { background: #f3f4f6; }
</style> 