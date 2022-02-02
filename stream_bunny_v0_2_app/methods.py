def get_movie_info(curr_movies):
    movie_array = []
    for movie in curr_movies:
        if movie.get('votes'):
            testIfCast = movie.get('cast')
            cast_subarray = []
            if testIfCast:
                for person in testIfCast[:3]:
                    cast_subarray.append(person['name'])
            movie_array.append( {
                'title': movie.get('title'),
                'year': movie.get('year'),
                'cast': cast_subarray,
                'rating': movie.get('rating'),
                'genre': movie.get('genre'),
                'poster_link': movie.get('cover url'),
                'votes': movie.get('votes'),
                'id': movie.getID(),
                } )
    return movie_array