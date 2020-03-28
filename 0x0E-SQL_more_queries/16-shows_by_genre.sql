-- lists all shows, and all genres linked to that show
-- If a show doesn’t have a genre, display NULL in the genre column
SELECT tv_shows.title, tv_genres.name
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY 1, 2 ASC;