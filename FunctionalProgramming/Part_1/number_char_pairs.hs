charsDivisibleBy :: Int -> [Char]
charsDivisibleBy n
  |  n <= 0 || n > 26 = []
  | otherwise = let pairlist = zip ['a'..'z'] [1..26]
                    divisible xp = rem (snd xp) n == 0
                in map fst (filter divisible pairlist)


charsProductOf :: [Int] -> [Char]
charsProductOf ns
  | null ns = []
  | otherwise = let  pairlist' = zip ['a'..'z'] [1..26]
                     comb [] = []
                     comb (x:xs) = (map (*x) xs) ++ (comb xs)
                in [fst(xp) | xp <- pairlist', elem (snd xp) (comb ns)]