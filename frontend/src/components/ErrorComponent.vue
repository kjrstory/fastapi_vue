<template>
  <div>
    <div v-if="typeof error.detail === 'string'" class="alert alert-danger" role="alert">
      <div>
        {{ error.detail }}
      </div>
    </div>
    <div v-else-if="typeof error.detail === 'object' && error.detail.length > 0" 
         class="alert alert-danger" role="alert">
      <div v-for="(err, i) in error.detail" :key="i">
        <div>
          <strong>{{ err.loc[1] }}</strong> : {{ err.msg }}
        </div>
      </div>
    </div>
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
