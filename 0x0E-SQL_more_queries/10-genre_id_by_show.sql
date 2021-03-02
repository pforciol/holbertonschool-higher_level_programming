-- Lists all shows from hbtn_0d_tvshows that have at least one genre linked.

    SELECT s.title, g.genre_id
      FROM tv_shows s
INNER JOIN tv_show_genres g
        ON s.id = g.show_id
  ORDER BY s.title, g.genre_id ASC;
