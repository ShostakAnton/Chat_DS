<template>
    <mu-col span="8" xl="9">
        <AddUsers :room="id"></AddUsers>
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs"
                    direction="column"
                    justify-content="start"
                    align-items="end">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>

                <mu-text-field v-model="form.textarea"
                               multi-line
                               :rows="4"
                               full-width
                               placeholder="Введите текст сообщения">
                </mu-text-field>
                <mu-button class="btn-send" round color="success" @click="sendMes">Отправить</mu-button>
            </mu-row>
        </mu-container>
    </mu-col>
</template>

<script>
    import AddUsers from './AddUsers.vue'

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        components: {
            AddUsers,
        },
        data() {                // хранение списка диалогов
            return {
                dialogs: '',
                form: {
                    textarea: '',
                },
            }
        },
        created() {
            $.ajaxSetup({                //  в ajaxSetup заносим в headers
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                // "Authorization": "Token 6a57d9af66fcf68b9fac066e67d4a450f5cf667a"
            });
            this.loadDialog()       // загрузка диалога
            setInterval(() => {     // обновление диалога, каждые 5 секунд
                this.loadDialog()
            }, 5000)
        },
        methods: {
            loadDialog() {      // загрузка диалогов
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data

                    },
                })
            },
            sendMes() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "POST",
                    data: {
                        room: this.id,
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()           //обновление диалога
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    .dialog {
        border: 1px solid #000;
    }

    .btn-send {
        margin: 60px 0 0 15;
    }
</style>
