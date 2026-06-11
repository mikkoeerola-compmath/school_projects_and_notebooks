onlyDigits :: String -> Bool
onlyDigits "" = True
onlyDigits (x:xs) = (elem x j) && onlyDigits xs
  where j = ['0'..'9']