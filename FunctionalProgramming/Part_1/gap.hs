gap :: (Char, Char) -> Int -> String -> Int
gap (_,_) x _
  | x < 0 = error "gap has to be positive"
gap (_,_) _ "" = 0
gap (a,b) y (x:xs)
  | length xs <= y = 0
  | x == a && b == last( take (y + 1) xs) = 1 + tailGap
  | otherwise = tailGap
  where tailGap = gap (a,b) y xs