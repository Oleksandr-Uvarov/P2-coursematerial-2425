def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    # xs_in_ys = {x for x in xs if x in ys}
    # ys_in_xs = {y for y in ys if y in xs}
  
    # return xs_in_ys | ys_in_xs
    return {x for x in xs if x in ys}


common_elements([1, 2, 3], [3,4, 3])