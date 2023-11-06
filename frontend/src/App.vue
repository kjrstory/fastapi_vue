<template>
  <h1>{{ message }}</h1>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
    };
  },
  mounted() {
    axios.get('http://localhost:8000/hello')
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>

