--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. 
--  Each record should display: <TV Show genre> - <Number of shows linked to this genre>
SELECT tv_genres.name,count(*) number_of_shows
FROM tv_show_genres, tv_genres
WHERE tv_show_genres.genre_id = tv_genres.id
group by tv_genres.name
ORDER BY 2 DESC;
