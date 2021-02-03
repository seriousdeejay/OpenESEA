<template>
    <div>
        <form @submit.prevent="update" method="post">
            <div class="">
                <label for="name">Name</label>
                <input
                    type="text"
                    id="name"
                    v-model="subscription.name"
                    name="name"
                    placeholder="Enter name"
                >
            </div>
            <div class="">
                <label for="currency">Currency</label>
                <select
                    name="currency"
                    id="currency"
                    v-model="subscription.currency"
                >
                    <option value="EUR">EUR</option>
                    <option value="USD">USD</option>
                </select>
            </div>
            <div class="">
                <label for="amount">Amount</label>
                <input
                    type="number"
                    name="amount"
                    id="amount"
                    v-model="subscription.amount"
                    placeholder="Enter amount"
                 >
            </div>
            <div class="">
                <label for="description">Description</label>
                <textarea
                    name="description"
                    id="description"
                    v-model="subscription.description"
                    cols="30"
                    rows="2"
                ></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data () {
        return {
            subscription: {
                name: '',
                currency: '',
                amount: '',
                description: ''
            },
            submitted: false
        }
    },
    mounted () {
        axios.get(`http://127.0.0.1:8000/api/subscriptions/${this.$route.params.id}/`)
            .then(response => {
                console.log(response.data)
                this.subscription = response.data
            });
    },
    methods: {
        update: function (e) {
                axios
                    .put(`http://127.0.0.1:8000/api/subscriptions/${this.subscription.id}/`,
                        this.subscription
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
        }
    }
}
</script>
