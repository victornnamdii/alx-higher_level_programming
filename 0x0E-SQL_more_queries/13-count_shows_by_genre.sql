-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record should display tv_genres.name, number of shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted descending order by number of shows linked
-- Can only use one SELECT statement
SELECT g.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres AS g
INNER JOIN tv_show_genres AS t ON g.id = t.genre_id
GROUP BY g.name ORDER BY number_of_shows DESC;
