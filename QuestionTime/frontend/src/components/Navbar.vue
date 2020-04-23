<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
            <router-link class="navbar-brand" :to="{name: 'Home' }">QuestionTime</router-link>

            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <router-link class="btn" :to="{name: 'Home' }">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="btn" :to="{name: 'QuestionEditor' }">Ask Question</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="btn" href="/accounts/logout/">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavbarComponent"
};
</script>

<style scoped>
.my-navbar {
    background-color: transparent !important;
}
.navbar-brand {
    font-weight: bold;
    font-size: 130%;
}
.navbar-brand:hover {
    color: #1b5299;
}
.btn {
    display: inline-block;
    padding: 10px;
    margin: 0 5px;
    border-radius: 10px;
    border: 2px solid #111111;
    transition: 0.1s ease;
}
.btn:hover {
    border-radius: 10px;
    border: 2px solid #1b5299;
    background-color: #1b5299;
    color: white;
}
</style>