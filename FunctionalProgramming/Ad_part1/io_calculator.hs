import System.IO
import Control.Monad
import Data.List

main :: IO ()
main = calculateLoop ""

calculateLoop :: String -> IO ()
calculateLoop stack = do
    input <- getLine
    if input == "quit" then return ()
    else do
        let newStack = stack ++ " " ++ input
            calculatedStack = calculateStack newStack
            in do
                print calculatedStack
                calculateLoop $ unwords . reverse $ map show calculatedStack

calculateStack :: String -> [Float]
calculateStack = foldl foldingFunction [] . words
  where foldingFunction (x:y:ys) "*" = (x * y):ys
        foldingFunction (x:y:ys) "+" = (x + y):ys
        foldingFunction (x:y:ys) "-" = (y - x):ys
        foldingFunction (x:y:ys) "/" = (y / x):ys
        foldingFunction (x:y:ys) "^" = (y ** x):ys
        foldingFunction (x:xs) "ln" = log x:xs
        foldingFunction xs "sum" = [sum xs]
        foldingFunction xs numberString = read numberString:xs