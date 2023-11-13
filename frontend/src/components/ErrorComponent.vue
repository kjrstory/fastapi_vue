<template>
  <div>
    <ul v-if="typeof error.detail === 'string'">
      <li>{{ error.detail }}</li>
    </ul>
    <ul v-else-if="typeof error.detail === 'object' && error.detail.length > 0">
      <li v-for="(err, i) in error.detail" :key="i">
        <strong>{{ err.loc[1] }}</strong> : {{ err.msg }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    error: {
      type: Object,
      default: () => ({})
    }
  }
};
</script>
