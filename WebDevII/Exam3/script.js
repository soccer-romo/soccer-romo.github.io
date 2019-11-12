// httpsTvPopRequest = new XMLHttpRequest();
// httpsTvPopRequest.open('get',"https://api.themoviedb.org/3/tv/popular?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1")
// httpsTvPopRequest.send(null);

// httpsTvPopRequest.onreadystatechange = TvRequest;



// function TvRequest()
// {
//     if (httpsTvPopRequest.readyState == 4 && httpsTvPopRequest.status == 200)
//     {
//         tvShows = httpsTvPopRequest.responseText;
//         tvShowsObj = JSON.parse(tvShows);

//         for(var i = 0; i < 3; i++)
//         {
//             var sec = document.createElement('section');
//             var img = document.createElement('img');
//             var title = document.createElement('h1');
//             var desc = document.createElement('p');
//             var rating = document.createElement('p')
//             var hr = document.createElement('hr')
//             var moreInfo = document.createElement('a')

//             img.src = "https://image.tmdb.org/t/p/" + "original" + tvShowsObj.results[i].poster_path;
//             title.innerHTML = tvShowsObj.results[i].original_name;
//             desc.innerHTML = tvShowsObj.results[i].overview
//             rating.innerHTML = "Rating: " + tvShowsObj.results[i].vote_average * 10 + "%"
//             moreInfo.innerHTML = "More Info";
//             moreInfo.href = "https://www.themoviedb.org/tv/" + tvShowsObj.results[i].id + "-" + tvShowsObj.results[i].name;

//             sec.style = "border: solid 2px black; width: 430px; text-align: center; margin: 1%; float: left;"
//             img.style = "width: 400px;";
//             title.style = "width: 400px";
//             desc.style = "width: 400px";


//             sec.appendChild(img);
//             sec.appendChild(title);
//             sec.appendChild(desc);
//             sec.appendChild(rating)
//             sec.appendChild(hr);
//             sec.appendChild(moreInfo)

//             document.getElementById("Movie").appendChild(sec)
//         }

//     }
// }


var movied = new Vue(
    {
        el: "#Movie",
        // name:
        // {
            
        // },
        data:{
             //To probably update this in the future make find a way to make the movie index varied
            movielist:[],
            httpsTvShowsRequest: "",
            baseUrlHttpsRequest: ""
            
        },
        //The calls the function as soon as it's loaded
        mounted: function(){
            this.movieRequest();
        },
        methods:
        {
            //this gets the Xml https requests with the APIs
            movieRequest: function()
            {
                this.httpsTvShowsRequest = new XMLHttpRequest();
                this.httpsTvShowsRequest.open('get',"https://api.themoviedb.org/3/tv/popular?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1")
                this.httpsTvShowsRequest.send(null);
                
                //Interesting Note-- on the readystate change it should be the last XMLHttpRequest or else it won't load all of the other ones after
                this.baseUrlHttpsRequest = new XMLHttpRequest();
                this.baseUrlHttpsRequest.open('get',"https://api.themoviedb.org/3/configuration?api_key=9b362e3e690674bb239092bc71c6c0a8")
                this.baseUrlHttpsRequest.send(null);

                //This will call the movieRequestInside function in vue script
                this.baseUrlHttpsRequest.onreadystatechange = this.movieRequestInside;
            },
            //This fuction sets the different variables into the movielist which only has three index
            //One way to update this is to be able to decided what api database you're going to use for the site
            //So custom XML Request and maybe also set a number for how many movies you want returned
            movieRequestInside: function()
            {
                if(this.httpsTvShowsRequest.readyState == 4 && this.httpsTvShowsRequest.status == 200)
                {
                    movie = this.httpsTvShowsRequest.responseText;
                    movieObj = JSON.parse(movie);
                    
                    if(this.baseUrlHttpsRequest.readyState == 4 && this.baseUrlHttpsRequest.status == 200)
                    {
                        baseUrl = this.baseUrlHttpsRequest.responseText;
                        baseUrlObj = JSON.parse(baseUrl)
            
                        for(var i = 0;i < movieObj.results.length; i++)
                        {
                            //populates the movielist array
                            this.movielist.push({
                                title: movieObj.results[i].name,
                                desc: movieObj.results[i].overview,
                                imgsrc: baseUrlObj.images.base_url + baseUrlObj.images.poster_sizes[5] + movieObj.results[i].poster_path,
                                rating: movieObj.results[i].vote_average,
                                date: movieObj.results[i].first_air_date,
                                moreInfo: "https://www.themoviedb.org/tv/" + movieObj.results[i].id + "-" + movieObj.results[i].name})
                        }
                    }
                }
                
            },
            displayInfo(id)
            {
                if(id.style.display === "none")
                {
                    id.style.display == "block"
                }
                else {
                    id.style.display = "none";
                  }
            }
        },
    })

Vue.component('sectionlist',{
    props:["themovies"],
    template: `
    <list-item>
        <div v-for = "movie in themovies">
            <div class="card" id = "card">
                <img class="card-img-top" v-bind:src = "movie.imgsrc" v-bind:alt="movie.title">
                <div class="card-body">
                    <h2 class="card-title">{{movie.title}}</h2>
                    <p class="card-text" id = "tvDesc">{{movie.desc}}</p>
                    <p class="card-text">Rating: {{movie.rating * 10}}% <br> Date Aired: {{movie.date}}</p>
                    <hr>
                    <a v-bind:href= "movie.moreInfo" class="card-text" id="moreInfo">More Info</a>
                </div>
            </div>
        </div>
    </list-item>
    `
})

Vue.component('list-item',{
    template: `<div class = "topThreeMovies"><slot></slot></div>`
            
    
})
