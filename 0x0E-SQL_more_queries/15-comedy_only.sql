-- Uses the hbtn_0d_tvshows database to llists all Comedy shows.

  SELECT s.title
    FROM (tv_genres g JOIN tv_show_genres sg ON g.id = sg.genre_id)
    JOIN tv_shows s ON sg.show_id = s.id
   WHERE g.name = "Comedy"
ORDER BY s.title ASC;
