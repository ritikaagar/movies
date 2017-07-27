var api = 'http://data.tmsapi.com/v1.1/movies/showings?startDate=2017-07-25&zip=94544&api_key=sszbbjhadk82fc9nh469bs2k'
html = ''
$(document).ready(function(){

    $.get(api, function(data){
        for (var i = 0; i < 5; i++){
            for (var j = 0; j < data[i].showtimes.length; j++){
                movieInfo = {
                    title: data[i].title,
                    desc: data[i].shortDescription,
                    theatreName: data[i].showtimes[j].theatre.name,
                    showtime: data[i].showtimes[j].dateTime,
                    ratings: data[i].ratings[0].code,
                    zipcode:
                };
            }   

            html += '<div class= "movies">'
            html += '<p>Movie title: '+ movieInfo.title + '</p>'
            html += '<p>Description: '+ movieInfo.desc + '</p>'
            html += '<p>Theatre: '+ movieInfo.theatreName +'</p>'
            html += '<p>Showtimes: '+ movieInfo.showtime +'</p>'
            html += '<p>Rating: '+ movieInfo.ratings +'</p>'
            html += '</div>' 

            $('#movies').html(html);
        }
    })
})