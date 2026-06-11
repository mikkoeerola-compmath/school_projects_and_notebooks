onlyDigits' :: String -> Bool
onlyDigits' "" = True
onlyDigits' (x:xs) = (elem x j) && onlyDigits' xs
  where j = ['0'..'9']

startsWith' :: String -> String -> Bool
startsWith' "" _ = False
startsWith' _ "" = True
startsWith' (x:xs) (y:ys)
  | x /= y = False
  | head xs /= head ys = False
  | otherwise = True

replaceNumLet :: Char -> Int
replaceNumLet x
  | x `elem` ['A'..'Z'] = head [snd xt | xt <- gg, x == fst xt]
  | otherwise = head [snd xt | xt <- jj, x == fst xt]
  where gg = zip ['A'..'Z'] [10..35]
        jj = zip ['0'..'9'] [0..9]

replaceAndMove :: String -> String
replaceAndMove (x:xs) = xs ++ show (replaceNumLet x)

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f( f( f( f x) ) )

replaceAndMoveFour :: String -> String
replaceAndMoveFour xs = applyTwice replaceAndMove xs

divideBy97 :: String -> Int
divideBy97 x = rem (read x) 97

validate :: String -> Bool
validate xs
  | length xs /= 18 = False
  | not (startsWith' xs "FI") = False
validate (x:y:xs)
  | not (onlyDigits' xs) = False
validate xs
  | divideBy97 (replaceAndMoveFour xs) == 1 = True
  | otherwise = False
