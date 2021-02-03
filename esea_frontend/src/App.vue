<template>
    <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Subscriptions</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add subscription</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
  <!-- <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>

  <router-view/>
    <div>
    <InputText />
    <Button label="Greet"></Button>
  </div>
  <div>
    <InputText v-model="text"/>
    <Button label="Greet" icon="pi pi-user" @click="greet"></Button>
    <Toast />
    {{text}}
  </div>

<script>
import { defineComponent, ref } from 'vue'
import { useToast } from 'primevue/usetoast'

export default defineComponent({
  setup () {
    const toast = useToast();
    const text = ref('Hi');
    const greet = () => {
      toast.add({ severity: 'info', summary: 'Hello', detail: text })
    };
    return {
      text,
      greet
    }
  }
});

//   data () {
//     return {
//       text: null
//     }
//   },
//   methods: {
//     greet () {
//       this.$toast.add({ severity: 'info', summary: 'Hello', detail: this.text })
//     }
//   }
// }
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style> -->
