//------------DIDN'T WORK (*_*) -----//
//Gets the movie api ready for use
// $(document).ready( ()=> 
// {
//     $.ajax({url:"https://api.themoviedb.org/3/movie/now_playing?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1",
//     success:function(result)
//     {
//         for(var i = 0; i < 3; i++)
//         {
//             movie.push(result.results[i])
//             console.log(movie[i].title)
//         }
//     }
// });
// })




// var httpsMovieRequest = new XMLHttpRequest();
// httpsMovieRequest.open('get',"https://api.themoviedb.org/3/movie/now_playing?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1")
// httpsMovieRequest.send(null);

// //Interesting Note-- on the readystate change it should be the last XMLHttpRequest or else it won't load all of the other ones after
// var baseUrlHttpsRequest = new XMLHttpRequest();
// baseUrlHttpsRequest.open('get',"https://api.themoviedb.org/3/configuration?api_key=9b362e3e690674bb239092bc71c6c0a8")
// baseUrlHttpsRequest.send(null);

// baseUrlHttpsRequest.onreadystatechange = movieRequest;

// function movieRequest()
// {
//     if(httpsMovieRequest.readyState == 4 && httpsMovieRequest.status == 200)
//     {
//         movie = httpsMovieRequest.responseText;
//         movieObj = JSON.parse(movie);
        
//         if(baseUrlHttpsRequest.readyState == 4 && baseUrlHttpsRequest.status == 200)
//         {
//             baseUrl = baseUrlHttpsRequest.responseText;
//             baseUrlObj = JSON.parse(baseUrl)

//             for(var i = 0; i < 3; i++)
//             {
//                 var sec = document.createElement('section-list');
//                 var title = document.createElement('H1');
//                 var desc = document.createElement('H3')
//                 var img = document.createElement('IMG')
//                 var vueInfo = document.createElement('div')
//                 vueInfo.id = "app"
//                 vueInfo.innerHTML = "<plist v-modal = 'message'></plist>"

//                 title.innerHTML = movieObj.results[i].title;
//                 desc.innerHTML = movieObj.results[i].overview;
//                 img.src = baseUrlObj.images.base_url + baseUrlObj.images.poster_sizes[3] + movieObj.results[i].poster_path;
                
//                 sec.appendChild(img)
//                 sec.appendChild(title)
//                 sec.appendChild(desc)
//                 sec.appendChild(vueInfo)
                
//                 document.getElementById('Movie').appendChild(sec)
//             } 
//         }
//     }
    
// }


Vue.component('sectionlist',{
    props:["themovies"],
    template: `
    <list-item>
        <div v-for = "movie in themovies">
            <div class="card" id = "card" style="width: 30rem;">
                <img class="card-img-top" v-bind:src = "movie.imgsrc" v-bind:alt="movie.title">
                <div class="card-body">
                    <h5 class="card-title">{{movie.title}}</h5>
                    <p class="card-text">{{movie.desc}}</p>
                </div>
            </div>
        </div>
    </list-item>
    `
})

Vue.component('list-item',{
    template: `<div class = "topThreeMovies"><slot></slot></div>`
            
    
})

var movied = new Vue(
    {
        el: "#Movie",
        data:{
            message:"this hurt my head",
            movielist:[{title:"", desc:"",imgsrc:""},{title:"", desc:"",imgsrc:""},{title:"", desc:"",imgsrc:""}],
            httpsMovieRequest: "",
            baseUrlHttpsRequest: ""
            
        },
        methods:
        {
            //this gets the Xml https requests with the APIs
            movieRequest: function()
            {
                this.httpsMovieRequest = new XMLHttpRequest();
                this.httpsMovieRequest.open('get',"https://api.themoviedb.org/3/movie/now_playing?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1")
                this.httpsMovieRequest.send(null);
                
                //Interesting Note-- on the readystate change it should be the last XMLHttpRequest or else it won't load all of the other ones after
                this.baseUrlHttpsRequest = new XMLHttpRequest();
                this.baseUrlHttpsRequest.open('get',"https://api.themoviedb.org/3/configuration?api_key=9b362e3e690674bb239092bc71c6c0a8")
                this.baseUrlHttpsRequest.send(null);

                this.baseUrlHttpsRequest.onreadystatechange = this.movieRequestInside;
            },
            movieRequestInside: function()
            {
                if(this.httpsMovieRequest.readyState == 4 && this.httpsMovieRequest.status == 200)
                {
                    movie = this.httpsMovieRequest.responseText;
                    movieObj = JSON.parse(movie);
                    
                    if(this.baseUrlHttpsRequest.readyState == 4 && this.baseUrlHttpsRequest.status == 200)
                    {
                        baseUrl = this.baseUrlHttpsRequest.responseText;
                        baseUrlObj = JSON.parse(baseUrl)
            
                        for(var i = 0; i < 3; i++)
                        {
                            this.movielist[i].title = movieObj.results[i].title;
                            this.movielist[i].desc = movieObj.results[i].overview;
                            this.movielist[i].imgsrc = baseUrlObj.images.base_url + baseUrlObj.images.poster_sizes[5] + movieObj.results[i].poster_path;
                        } 
                    }
                }
                
            }
        },
    })