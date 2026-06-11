{-import System.Random
import Data.List
import Data.Char
import Control.Monad.Trans.Accum (accum)


main = do
 input1 <- getLine
 input2 <- getLine
 input3 <- getLine
 print $ genStrings (randoms (getGen (read input1 :: Int)) :: [Int]) -- seed
   (read input2 :: Int) -- maxStrings
   (read input3 :: Int) -- maxLength of string


makeChar rand = chr (30 + (mod rand 92))

getGen seed = mkStdGen seed

-- Your code starts here-}

genStrings :: [Int] -> Int -> Int -> [String]
genStrings (x:xs) maxStrings maxLength = 
    let numOfStrs = mod x (maxStrings+1)
    in buildStrings numOfStrs maxLength xs []

buildStrings :: Int -> Int -> [Int] -> [String] -> [String]
buildStrings 0 _ rands acc = reverse acc
buildStrings n maxLen (lenRand:restRands) acc =
    let len = mod lenRand (maxLen + 1)
        (charRands, rest) = splitAt len restRands
        str = map makeChar charRands
    in buildStrings (n-1) maxLen rest (str : acc)