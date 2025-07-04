<template>
  <div>
    <!-- Top Bar -->
    <div class="bg-blue-900 text-white text-sm">
      <div class="container mx-auto px-4 py-2 flex justify-between items-center">
        <div class="hidden md:block">
          <span class="mr-4"><i class="fas fa-map-marker-alt mr-1"></i> Lusaka, Education City</span>
          <span><i class="fas fa-clock mr-1"></i> Mon-Fri: 8:00AM - 6:00PM</span>
        </div>
        <div class="flex space-x-4">
          <a href="tel:+260 978943880" class="hover:text-blue-200 transition"><i class="fas fa-phone mr-1"></i> +1 (260) 9567-890</a>
          <a href="mailto:info@cast.edu" class="hover:text-blue-200 transition"><i class="fas fa-envelope mr-1"></i> info@cast.edu</a>
        </div>
      </div>
    </div>
    <!-- Main Header -->
    <header class="bg-white shadow-sm">
      <div class="container mx-auto px-4 py-6 flex flex-col md:flex-row justify-between items-center">
        <div class="flex items-center mb-4 md:mb-0">
          <img src="https://via.placeholder.com/60" alt="C.A.S.T Logo" class="h-12 mr-4">
          <div>
            <h1 class="text-2xl font-bold text-blue-900">C.A.S.T</h1>
            <p class="text-sm text-gray-600 font-medium">College Automation System Tool</p>
          </div>
        </div>
        <nav class="hidden md:flex space-x-6">
          <router-link to="/" class="font-medium text-blue-900 hover:text-blue-700 transition">Home</router-link>
          <a href="#" class="font-medium text-gray-600 hover:text-blue-700 transition">About</a>
          <a href="#" class="font-medium text-gray-600 hover:text-blue-700 transition">Features</a>
          <a href="#" class="font-medium text-gray-600 hover:text-blue-700 transition">Departments</a>
          <a href="#" class="font-medium text-gray-600 hover:text-blue-700 transition">Contact</a>
        </nav>
        <button class="md:hidden text-gray-600">
          <i class="fas fa-bars text-xl"></i>
        </button>
      </div>
    </header>
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-800 to-blue-600 text-white py-16">
      <div class="container mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">Transform Your Institution With Digital Automation</h2>
        <p class="text-xl mb-8 max-w-3xl mx-auto">C.A.S.T provides comprehensive solutions for modern educational institutions to streamline operations and enhance learning experiences.</p>
        <div class="flex flex-col sm:flex-row justify-center gap-4">
          <a href="#" class="bg-white text-blue-800 font-bold py-3 px-6 rounded-lg hover:bg-gray-100 transition">Explore Features</a>
          <a href="#" class="bg-transparent border-2 border-white font-bold py-3 px-6 rounded-lg hover:bg-white hover:text-blue-800 transition">Request Demo</a>
        </div>
      </div>
    </section>
    <!-- Portal Access -->
    <section class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl font-bold text-center mb-12 text-gray-800">Access Your Portal</h2>
        <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <router-link to="/admin" class="group bg-gray-50 rounded-xl shadow-md hover:shadow-lg transition p-8 text-center">
            <div class="bg-blue-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-blue-200 transition">
              <i class="fas fa-user-shield text-blue-600 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-800">Administrator</h3>
            <p class="text-gray-600">Manage institution-wide operations and analytics</p>
            <button class="mt-4 text-blue-600 font-medium hover:text-blue-800 transition">Login <i class="fas fa-arrow-right ml-1"></i></button>
          </router-link>
          <router-link to="/student" class="group bg-gray-50 rounded-xl shadow-md hover:shadow-lg transition p-8 text-center">
            <div class="bg-green-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-green-200 transition">
              <i class="fas fa-user-graduate text-green-600 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-800">Student</h3>
            <p class="text-gray-600">Access courses, grades, and campus resources</p>
            <button class="mt-4 text-green-600 font-medium hover:text-green-800 transition">Login <i class="fas fa-arrow-right ml-1"></i></button>
          </router-link>
          <router-link to="/lecturer" class="group bg-gray-50 rounded-xl shadow-md hover:shadow-lg transition p-8 text-center">
            <div class="bg-purple-100 w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-purple-200 transition">
              <i class="fas fa-chalkboard-teacher text-purple-600 text-2xl"></i>
            </div>
            <h3 class="text-xl font-bold mb-2 text-gray-800">Lecturers</h3>
            <p class="text-gray-600">Manage courses, attendance, and student progress</p>
            <button class="mt-4 text-purple-600 font-medium hover:text-purple-800 transition">Login <i class="fas fa-arrow-right ml-1"></i></button>
          </router-link>
        </div>
      </div>
    </section>
    <!-- Announcements, News, Footer (unchanged) -->
    <section class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
          <h2 class="text-2xl font-bold text-gray-800 mb-4 md:mb-0">Latest Announcements</h2>
          <a href="#" class="text-blue-600 font-medium hover:text-blue-800 transition">View All Announcements <i class="fas fa-arrow-right ml-1"></i></a>
        </div>
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <div class="divide-y divide-gray-200">
            <div class="p-6 hover:bg-gray-50 transition">
              <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
                <div>
                  <h3 class="font-bold text-lg text-gray-800 mb-1">Admission Deadline Extended</h3>
                  <p class="text-gray-600">Due to popular demand, we've extended the admission deadline to June 30, 2025.</p>
                </div>
                <div class="mt-2 sm:mt-0 text-sm text-gray-500 font-medium">June 15, 2025</div>
              </div>
            </div>
            <div class="p-6 hover:bg-gray-50 transition">
              <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
                <div>
                  <h3 class="font-bold text-lg text-gray-800 mb-1">Course Registration Opens</h3>
                  <p class="text-gray-600">Fall semester course registration will begin on July 1, 2025 at 9:00 AM.</p>
                </div>
                <div class="mt-2 sm:mt-0 text-sm text-gray-500 font-medium">June 25, 2025</div>
              </div>
            </div>
            <div class="p-6 hover:bg-gray-50 transition">
              <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center">
                <div>
                  <h3 class="font-bold text-lg text-gray-800 mb-1">Semester Exams Schedule</h3>
                  <p class="text-gray-600">The examination schedule for the current semester has been published.</p>
                </div>
                <div class="mt-2 sm:mt-0 text-sm text-gray-500 font-medium">August 10, 2025</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <h2 class="text-2xl font-bold text-center mb-12 text-gray-800">Campus News & Updates</h2>
        <div class="grid md:grid-cols-3 gap-8">
          <article class="rounded-xl overflow-hidden shadow-md hover:shadow-lg transition">
            <img src="https://source.unsplash.com/random/600x400/?university,technology" alt="Digital Campus" class="w-full h-48 object-cover">
            <div class="p-6">
              <span class="text-xs font-semibold text-blue-600 uppercase tracking-wider">Innovation</span>
              <h3 class="text-xl font-bold mt-2 mb-3 text-gray-800">C.A.S.T Launches Digital Campus</h3>
              <p class="text-gray-600 mb-4">Our new digital campus initiative brings automation modules to all departments, streamlining operations campus-wide.</p>
              <a href="#" class="text-blue-600 font-medium hover:text-blue-800 transition">Read More <i class="fas fa-arrow-right ml-1"></i></a>
            </div>
          </article>
          <article class="rounded-xl overflow-hidden shadow-md hover:shadow-lg transition">
            <img src="https://source.unsplash.com/random/600x400/?ai,education" alt="AI Curriculum" class="w-full h-48 object-cover">
            <div class="p-6">
              <span class="text-xs font-semibold text-green-600 uppercase tracking-wider">Academics</span>
              <h3 class="text-xl font-bold mt-2 mb-3 text-gray-800">AI Curriculum Integration</h3>
              <p class="text-gray-600 mb-4">Machine learning and AI courses now available across all technology programs starting Fall 2025.</p>
              <a href="#" class="text-green-600 font-medium hover:text-green-800 transition">Read More <i class="fas fa-arrow-right ml-1"></i></a>
            </div>
          </article>
          <article class="rounded-xl overflow-hidden shadow-md hover:shadow-lg transition">
            <img src="https://source.unsplash.com/random/600x400/?business,meeting" alt="Placements" class="w-full h-48 object-cover">
            <div class="p-6">
              <span class="text-xs font-semibold text-purple-600 uppercase tracking-wider">Careers</span>
              <h3 class="text-xl font-bold mt-2 mb-3 text-gray-800">Placement Season 2025</h3>
              <p class="text-gray-600 mb-4">This year's placement season breaks records with international offers increasing by 35% over last year.</p>
              <a href="#" class="text-purple-600 font-medium hover:text-purple-800 transition">Read More <i class="fas fa-arrow-right ml-1"></i></a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <footer class="bg-gray-900 text-white pt-16 pb-8">
      <div class="container mx-auto px-4">
        <div class="grid md:grid-cols-4 gap-8 mb-12">
          <div>
            <h3 class="text-lg font-bold mb-4">About C.A.S.T</h3>
            <p class="text-gray-400">The College Automation System Tool is a comprehensive platform designed to modernize educational institution management through digital transformation.</p>
          </div>
          <div>
            <h3 class="text-lg font-bold mb-4">Quick Links</h3>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-400 hover:text-white transition">Admissions</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Academic Calendar</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Library Resources</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Career Services</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-bold mb-4">Support</h3>
            <ul class="space-y-2">
              <li><a href="#" class="text-gray-400 hover:text-white transition">Help Center</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">System Status</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Contact IT</a></li>
              <li><a href="#" class="text-gray-400 hover:text-white transition">Feedback</a></li>
            </ul>
          </div>
          <div>
            <h3 class="text-lg font-bold mb-4">Connect With Us</h3>
            <div class="flex space-x-4 mb-4">
              <a href="#" class="bg-gray-700 w-10 h-10 rounded-full flex items-center justify-center hover:bg-blue-600 transition"><i class="fab fa-facebook-f"></i></a>
              <a href="#" class="bg-gray-700 w-10 h-10 rounded-full flex items-center justify-center hover:bg-blue-400 transition"><i class="fab fa-twitter"></i></a>
              <a href="#" class="bg-gray-700 w-10 h-10 rounded-full flex items-center justify-center hover:bg-red-600 transition"><i class="fab fa-youtube"></i></a>
              <a href="#" class="bg-gray-700 w-10 h-10 rounded-full flex items-center justify-center hover:bg-blue-500 transition"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <p class="text-gray-400">Subscribe to our newsletter for updates</p>
          </div>
        </div>
        <div class="border-t border-gray-800 pt-8 text-center text-gray-400 text-sm">
          <p>&copy; 2025 C.A.S.T - College Automation System Tool. All rights reserved.</p>
          <p class="mt-2">Designed for full-scale digital campus management.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
// No script needed for static homepage
</script>

<style scoped>
/* Add any custom styles here if needed */
</style> 