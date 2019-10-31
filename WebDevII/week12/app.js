var aryMovies = ["matrix","Mulan", "Don't Ask Me"];

Vue.component('section-list', {
    props:["themovies"],
    template: `
    <section>
        <h1><slot></slot></h1>
        <img v-bind:src = "imgsrc" width = "300px">
        <list-item  v-for = "movie in themovies">{{movie}}</list-item>
    </section>
    `,

    data: function()
    {
        return{
            imgsrc: "images/Endgame.jpg"
        }
    }
})

Vue.component("list-item", {
    template: `
    <p><slot></slot></p>
    `
})

new Vue(
    {
        el:"#app",
        data:
        {
            mess: "Alo Lume",
            movies:  aryMovies,
            aryTvShows: ["Sirens","New Amsterdam","The Dragon Prince"]
        }
        
    }
)