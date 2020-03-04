-- lists all Comedy shows in the database hbtn_0d_tvshows 
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
SELECT  tv_shows.title 
FROM tv_show_genres, tv_genres, tv_shows
WHERE tv_show_genres.genre_id = tv_genres.id and 
      tv_genres.name = 'Comedy' and
      tv_shows.id = tv_show_genres.show_id
ORDER BY 1 ASC;
