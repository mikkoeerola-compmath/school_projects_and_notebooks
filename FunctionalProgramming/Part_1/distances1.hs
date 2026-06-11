-- a)
distance1 :: String -> String -> Float
distance1 [] [] = 0
distance1 xs ys = let not_in_s2 = [x | x <- xs, not (x `elem` ys)]
                      not_in_s1 = [y | y <- ys, not (y `elem` xs)]
                  in fromIntegral(length (not_in_s2 ++ not_in_s1)) / fromIntegral (length( xs ++ ys))

-- b)
distance2 :: String -> String -> Float
distance2 [] [] = 0
distance2 xs ys = let not_a_num zs = [z | z <- zs, not (z `elem` ['0'..'9'])]
                  in fromIntegral(length( not_a_num xs ++ not_a_num ys)) / fromIntegral(length (xs ++ ys))