headOrLast:: [String] -> Char -> [String]
headOrLast xs x = [st | st <- xs, head(st) == x || last(st) == x]