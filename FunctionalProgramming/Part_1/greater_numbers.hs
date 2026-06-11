nextIsGreater :: [Int] -> [Int]
nextIsGreater [] = []
nextIsGreater [_] = []
nextIsGreater (x:xs)
  | x < head(xs) = x : nextIsGreater xs
  | otherwise = nextIsGreater xs