<template>
  <v-app>
    <v-content>
      <Search />
    </v-content>
  </v-app>
</template>

<script>
import Search from './components/Search';

export default {
  name: 'App',

  components: {
    Search,
  }
};
</script>
