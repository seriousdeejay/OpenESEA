<template>
<div class="content">
  <div class="p-d-flex p-jc-center" style="width: 1000px">
      <Button type="Button" icon="pi pi-check" class="p-mr-2" />
      <Button type="Button" icon="pi pi-trash" class="p-button-danger"/>
      <Button type="Button" icon="pi pi-search" class="p-ml-auto p-button-help"/>
  </div>

  <Card style="width: 1000px; margin-bottom: 2em" class="p-d-block p-mx-auto p-text-center">
    <template #title>
        Simple Card
    </template>
    <template #content>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
        quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!</p>
    </template>
</Card>
        <h2><router-link to="dashboard">Subscriptions</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add subscription</router-link>
        <div class="p-d-block p-mx-auto">
        <router-view />
        </div>
</div>
</template>

<style>
.content {
  max-width: 1000px;
  margin:auto;
}

</style>
<!--
</div>
    <div class="container">
      <div class="col-md-8">
      </div>
    </div>
</template> -->

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
</style>
-->
