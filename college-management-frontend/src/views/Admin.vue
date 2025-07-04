<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div v-if="!loggedIn" class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h2 class="text-2xl font-bold mb-6 text-blue-900">Admin Login</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block mb-1 font-medium">Username</label>
          <input v-model="username" type="text" class="w-full border rounded px-3 py-2" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 font-medium">Password</label>
          <input v-model="password" type="password" class="w-full border rounded px-3 py-2" />
        </div>
        <div v-if="error" class="mb-4 text-red-600">{{ error }}</div>
        <button type="submit" class="w-full bg-blue-900 text-white py-2 rounded font-bold hover:bg-blue-800 transition">Login</button>
      </form>
    </div>
    <div v-else class="bg-white p-8 rounded shadow-md w-full max-w-3xl">
      <h2 class="text-2xl font-bold mb-4 text-blue-900">Welcome, Admin!</h2>
      <nav class="mb-6">
        <ul class="flex space-x-6">
          <li><button @click="section = 'users'" :class="sectionBtn('users')">User Management</button></li>
          <li><button @click="section = 'reports'" :class="sectionBtn('reports')">Reports</button></li>
          <li><button @click="section = 'settings'" :class="sectionBtn('settings')">Settings</button></li>
        </ul>
      </nav>
      <div v-if="section === 'users'">
        <h3 class="text-lg font-bold mb-2">User Management (Mock)</h3>
        <p class="text-gray-600 mb-4">View, add, or remove users. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>John Doe (Student)</li>
          <li>Jane Smith (Lecturer)</li>
          <li>Admin User (Admin)</li>
        </ul>
      </div>
      <div v-else-if="section === 'reports'">
        <h3 class="text-lg font-bold mb-2">Reports (Mock)</h3>
        <p class="text-gray-600 mb-4">View system reports and analytics. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Monthly Login Report</li>
          <li>Assignment Submission Stats</li>
          <li>System Health Overview</li>
        </ul>
      </div>
      <div v-else-if="section === 'settings'">
        <h3 class="text-lg font-bold mb-2">Settings (Mock)</h3>
        <p class="text-gray-600 mb-4">Change system settings. (This is a mock section.)</p>
        <ul class="list-disc pl-6 text-gray-700">
          <li>Change Password</li>
          <li>Notification Preferences</li>
          <li>Theme Selection</li>
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
const section = ref('users');

function login() {
  if (!username.value || !password.value) {
    error.value = 'Please enter both username and password.';
    return;
  }
  error.value = '';
  loggedIn.value = true;
}
function logout() {
  loggedIn.value = false;
  username.value = '';
  password.value = '';
  section.value = 'users';
}
function sectionBtn(name) {
  return [
    'px-4 py-2 rounded',
    section.value === name ? 'bg-blue-900 text-white' : 'bg-gray-100 text-blue-900 hover:bg-blue-100',
    'transition font-semibold'
  ].join(' ');
}
</script>

<style scoped>
body { background: #f3f4f6; }
</style> 