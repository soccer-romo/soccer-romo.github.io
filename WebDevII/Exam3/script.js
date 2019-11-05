httpsTvPopRequest = new XMLHttpRequest();
httpsTvPopRequest.open('get',"https://api.themoviedb.org/3/tv/popular?api_key=9b362e3e690674bb239092bc71c6c0a8&language=en-US&page=1")
httpsTvPopRequest.send(null);

httpsTvPopRequest.onreadystatechange = TvRequest;

function TvRequest()
{
    if (httpsTvPopRequest.readyState == 4 && httpsTvPopRequest.status == 200)
    {
        tvShows = httpsTvPopRequest.responseText;
        tvShowsObj = JSON.parse(tvShows);

        for(var i = 0; i < 3; i++)
        {
            var sec = document.createElement('section');
            var img = document.createElement('img');
            var title = document.createElement('h1');
            var desc = document.createElement('p');
            var rating = document.createElement('p')
            var hr = document.createElement('hr')
            var moreInfo = document.createElement('a')

            img.src = "https://image.tmdb.org/t/p/" + "original" + tvShowsObj.results[i].poster_path;
            title.innerHTML = tvShowsObj.results[i].original_name;
            desc.innerHTML = tvShowsObj.results[i].overview
            rating.innerHTML = "Rating: " + tvShowsObj.results[i].vote_average * 10 + "%"
            moreInfo.innerHTML = "More Info";
            moreInfo.href = "https://www.themoviedb.org/tv/" + tvShowsObj.results[i].id + "-" + tvShowsObj.results[i].name;

            sec.style = "border: solid 2px black; width: 430px; text-align: center; margin: 1%; float: left;"
            img.style = "width: 400px;";
            title.style = "width: 400px";
            desc.style = "width: 400px";


            sec.appendChild(img);
            sec.appendChild(title);
            sec.appendChild(desc);
            sec.appendChild(rating)
            sec.appendChild(hr);
            sec.appendChild(moreInfo)

            document.getElementById("Movie").appendChild(sec)
        }

    }
}
