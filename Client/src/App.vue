<template>
    <body>
    <div id="page-container">
      <div id="content-container">
          <appNavbar id="navbar"/>
          <RouterView />
      </div>
      <appFooter id="footer"/>
    </div>
  </body>
</template>

<script setup>
import appNavbar from './components/Navbar.vue'
import appFooter from './components/Footer.vue'
</script>

<style>
html, body {
  margin: 0;
  width: 100%;
  padding: 0;
  min-height: 100%;
}

#page-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

#content-container {
  flex: 1;
}

#footer {
  flex-shrink: 0; 
}
</style>