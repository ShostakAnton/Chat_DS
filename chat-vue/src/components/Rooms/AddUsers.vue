<template>
    <div>
        <select v-model="option">
            <option v-for="user in list"
                    :value="user.id">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button class="btn-send" round color="success" @click="addUser">Добавить пользователя</mu-button>
    </div>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: '',
        },
        data() {
            return {
                option: '',
                list: '',
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            loadUsers() {        // получение списка пользователей
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "GET",
                    success: (response) => {
                        this.list = response.data
                    },
                })
            },
            addUser() {     // добавление пользователя в комнату
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "POST",
                    data: {
                        room: this.room,
                        user: parseInt(this.option)     // parseInt: str -> int
                    },
                    success: (response) => {
                        alert("Пользователь добавлен")
                    },
                    error: (response) => {
                        alert("Error add user")
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
