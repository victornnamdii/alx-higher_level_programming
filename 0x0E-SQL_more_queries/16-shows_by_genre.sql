-- List all shows and genres linked to show from 'hbtn_0d_tvshows'
-- If show doesn't have a genre, display NULL in genre column
-- Each record should display tv_shows.title, tv_genres.name
-- Results must be sorted in ascending order by show title
-- You can only use one SELECT statement
SELECT t.title, g.name FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s ON t.id = s.show_id
LEFT JOIN tv_genres AS g ON s.genre_id = g.id
ORDER BY t.title, g.name;
