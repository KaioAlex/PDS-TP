<script setup>
import HomeBanner from "@/components/home/HomeBanner.vue";
import HomeInfoSection from "@/components/home/HomeInfoSection.vue";
import HomeFeatures from "@/components/home/HomeFeatures.vue";
import HomeExplore from "@/components/home/HomeExplore.vue";
import HomeContact from "@/components/home/HomeContact.vue";
import Footer from "@/components/FooterVue.vue";
</script>

<template>
  <main>
    <HomeBanner />
    <HomeInfoSection />
    <HomeFeatures />
    <HomeExplore />
    <HomeContact />
    <Footer />
  </main>
</template>

<style scoped>
main {
  display: block;
}
</style>
