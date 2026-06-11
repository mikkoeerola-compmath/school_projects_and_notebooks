points :: Int -> [(Int, Int)]
points x = [(s,t) | s <- [-x..x], t <- [-x..x], abs(s) + abs(t) <= x]
