-- Lists all shows from hbtn_0d_tvshows_rate by their ratings.

  SELECT s.title, SUM(r.rate) AS rating
    FROM tv_shows s
    JOIN tv_show_ratings r ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
