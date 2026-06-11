findAndCut :: Char -> String -> String
findAndCut x (y:xs)
  | not (x `elem` (y:xs)) = ""
  | x == y = xs
  | otherwise = findAndCut x xs

commonSubstring :: String -> String -> String
commonSubstring "" _ = ""
commonSubstring _ "" = ""
commonSubstring (x:xs) (y:ys)
  | isCommon x (y:ys) = x : commonSubstring xs (findAndCut x (y:ys))
  | isCommon y (x:xs) = y : commonSubstring (findAndCut y (x:xs)) ys
  | otherwise = commonSubstring xs ys
  where isCommon x xs = x `elem` xs