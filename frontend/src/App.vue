<template>
  <div class="app-shell">
    <aside class="sidebar" :class="{ open: menuOpen }">
      <router-link to="/" class="brand" @click="menuOpen = false"><span class="brand-mark"><AppIcon name="car" /></span><span>Flipper<span>Complete</span></span></router-link>
      <nav class="main-nav" aria-label="Main navigation">
        <router-link v-for="item in navItems" :key="item.to" :to="item.to" @click="menuOpen = false"><AppIcon :name="item.icon" /><span>{{ item.label }}</span></router-link>
      </nav>
      <div class="sidebar-foot"><div class="workspace-avatar">FC</div><div><strong>My Workspace</strong><small>Inventory manager</small></div></div>
    </aside>
    <button v-if="menuOpen" class="nav-scrim" aria-label="Close menu" @click="menuOpen = false"></button>
    <div class="main-column">
      <header class="topbar">
        <button class="icon-button menu-button" aria-label="Open menu" @click="menuOpen = true"><AppIcon name="menu" /></button>
        <div class="mobile-brand">Flipper<span>Complete</span></div><div class="topbar-spacer"></div>
        <button class="theme-toggle" :aria-label="`Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`" @click="toggleTheme"><AppIcon :name="theme === 'dark' ? 'sun' : 'moon'" /><span>{{ theme === 'dark' ? 'Light' : 'Dark' }}</span></button>
      </header>
      <main class="content"><router-view /></main>
      <footer class="footer">FlipperComplete <span>·</span> Built for the next flip.</footer>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref, watch } from 'vue'
import AppIcon from './components/AppIcon.vue'
const navItems = [{to:'/',label:'Overview',icon:'dashboard'},{to:'/vehicles',label:'Vehicles',icon:'car'},{to:'/parts',label:'Parts inventory',icon:'box'},{to:'/view-listing',label:'Listings',icon:'tag'}]
const menuOpen=ref(false); const theme=ref('light')
onMounted(()=>{const saved=localStorage.getItem('flipper-theme');theme.value=saved||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')})
watch(theme,value=>document.documentElement.setAttribute('data-theme',value),{immediate:true})
function toggleTheme(){theme.value=theme.value==='dark'?'light':'dark';localStorage.setItem('flipper-theme',theme.value)}
</script>
<style scoped>
.app-shell{min-height:100vh;display:grid;grid-template-columns:250px 1fr}.sidebar{position:fixed;inset:0 auto 0 0;width:250px;z-index:20;display:flex;flex-direction:column;padding:24px 18px;background:var(--surface);border-right:1px solid var(--border)}.brand{display:flex;align-items:center;gap:10px;padding:0 7px;text-decoration:none;color:var(--text);font:800 1.03rem Manrope,sans-serif;letter-spacing:-.04em}.brand>span:last-child span,.mobile-brand span{color:var(--brand)}.brand-mark{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;color:#fff;background:var(--brand);box-shadow:0 8px 20px color-mix(in srgb,var(--brand) 25%,transparent)}.main-nav{display:flex;flex-direction:column;gap:5px;margin-top:42px}.main-nav a{height:45px;padding:0 13px;display:flex;align-items:center;gap:12px;border-radius:11px;text-decoration:none;color:var(--muted);font-size:.9rem;font-weight:700}.main-nav a:hover{color:var(--text);background:var(--surface-2)}.main-nav a.router-link-exact-active{color:var(--brand);background:var(--brand-soft)}.sidebar-foot{margin-top:auto;padding:17px 8px 0;border-top:1px solid var(--border);display:flex;align-items:center;gap:10px}.workspace-avatar{width:35px;height:35px;display:grid;place-items:center;border-radius:50%;background:var(--surface-2);color:var(--brand);font-size:.73rem;font-weight:800}.sidebar-foot strong,.sidebar-foot small{display:block}.sidebar-foot strong{font-size:.82rem}.sidebar-foot small{color:var(--muted);font-size:.7rem;margin-top:1px}.main-column{grid-column:2;min-width:0;display:flex;min-height:100vh;flex-direction:column}.topbar{height:72px;display:flex;align-items:center;padding:0 clamp(22px,4vw,54px);border-bottom:1px solid var(--border);background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(12px);position:sticky;top:0;z-index:10}.topbar-spacer{flex:1}.theme-toggle{display:flex;align-items:center;gap:8px;border:1px solid var(--border);background:var(--surface);color:var(--muted);padding:8px 11px;border-radius:10px;font-weight:700;font-size:.77rem;cursor:pointer}.theme-toggle .app-icon{width:17px}.content{width:100%;max-width:1460px;margin:0 auto;padding:42px clamp(22px,4vw,54px);flex:1}.footer{padding:18px 30px 26px;text-align:center;color:var(--muted);font-size:.72rem}.footer span{padding:0 5px}.menu-button,.mobile-brand,.nav-scrim{display:none}@media(max-width:860px){.app-shell{display:block}.sidebar{transform:translateX(-105%);transition:transform .22s ease;box-shadow:var(--shadow)}.sidebar.open{transform:translateX(0)}.nav-scrim{display:block;position:fixed;inset:0;z-index:15;border:0;background:rgba(0,0,0,.38)}.main-column{display:flex}.menu-button{display:grid;margin-right:12px}.mobile-brand{display:block;font:800 .93rem Manrope,sans-serif;letter-spacing:-.04em}.topbar{height:64px;padding:0 18px}.content{padding:30px 18px}.theme-toggle span{display:none}}
</style>
