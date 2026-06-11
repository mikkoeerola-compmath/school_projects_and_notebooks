nextIsGreater :: [Int] -> [Int]
nextIsGreater xs = [x | x+1 `elem` xs]