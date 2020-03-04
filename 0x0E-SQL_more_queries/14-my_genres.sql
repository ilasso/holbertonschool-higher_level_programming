-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
SELECT distinct tv_genres.name 
FROM tv_show_genres, tv_genres, tv_shows
WHERE tv_shows.id = tv_show_genres.show_id and 
      tv_genres.id = tv_show_genres.genre_id and 
      tv_shows.title = 'Dexter'
ORDER BY 1 ASC;
