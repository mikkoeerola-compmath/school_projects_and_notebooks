import Data.Char
import Data.List

main = do
    line <- getLine
    if line == "quit" then putStrLn "bye"
    else do
        if length (words line) < 2 
            then putStrLn "I cannot do that"
        else do
            let args = words line
                command = args !! 0
                shift = args !! 1
            if (not ((command == "encode" || command == "decode") && onlyDigits shift))
                then putStrLn "I cannot do that"
            else do
                let shift' = read shift :: Int
                    shiftedWordList = map ((matchFunction command) shift') args
                    result = unwords $ tail $ tail  shiftedWordList
                putStrLn result
        main

encode :: Int -> String -> String 
encode shift msg = 
 let ords = map ord msg 
     shifted = map (+ shift) ords 
 in map chr shifted


decode :: Int -> String -> String
decode shift msg = encode (negate shift) msg

matchFunction :: String -> (Int -> String -> String)
matchFunction st
  | st == "decode" = decode
  | st == "encode" = encode


onlyDigits :: String -> Bool
onlyDigits [] = True
onlyDigits (x:xt) = (x `elem` ['0'..'9']) && onlyDigits xt
