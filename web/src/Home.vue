<template>
    <div class="container">
        <form>
            <div class="form-row">
                <div class="form-group col-6">
                    <label>First name</label>
                    <input class="form-control" type="text" v-model="first_name">
                </div>
                <div class="form-group col-6">
                    <label>First name</label>
                    <input class="form-control" type="text" v-model="last_name">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-12">
                    <label>Full name</label>
                    <input class="form-control" type="text" v-model="full_name" readonly />
                </div>
            </div>
            <div class="form-row">
                <div class="form-group col-12 text-end">
                    <button class="btn btn-primary w-50">Send</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
module.exports = {
    data: function(){
        return {
            first_name: '',
            last_name: ''
        }
    },
    methods: {
    },
    computed: {
        full_name: function(){
            return this.first_name + ' ' + this.last_name
        }
    },
    created: function(){}
}
</script>