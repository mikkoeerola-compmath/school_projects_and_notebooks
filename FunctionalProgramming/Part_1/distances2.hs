distanceFilter :: (String -> String -> Float) -> Float -> String -> [String] -> [String]
distanceFilter f d s ss = foldl (\acc x -> if f x s <= d then acc ++ [x] else acc) [] ss

distance3 :: String -> String -> Float
distance3 x y = fromIntegral $ abs $ length x - length y