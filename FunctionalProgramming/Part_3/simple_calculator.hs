-- Simple calculator

main = do
    line <- getLine
    if line == "quit" then putStrLn "bye"
    else do
        let args = words line
            num1 = args !! 0
            oper = args !! 1
            num2 = args !! 2
        if ( not (onlyDigits num1 && onlyDigits num2 && oper `elem` ["+", "-", "*"]))
            then
			putStrLn "I cannot calculate that"
            else do
                let num1' = read num1 :: Int
                    num2' = read num2 :: Int
                case oper of "+" -> putStrLn (show (num1' + num2'))
                             "-" -> putStrLn (show (num1' - num2'))
                             "*" -> putStrLn (show (num1' * num2'))
        main


onlyDigits :: String -> Bool
onlyDigits [] = True
onlyDigits (x:xt) = (x `elem` ['0'..'9']) && onlyDigits xt

