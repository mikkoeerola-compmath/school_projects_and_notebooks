{-import System.Random
import Data.List
import Data.Char


main = do
 input1 <- getLine
 input2 <- getLine
 input3 <- getLine
 print $ random_sort_check prop_idempotent qsort ( random_strings input1 input2 input3 )
 print $ random_sort_check prop_smallest_first qsort ( random_strings input1 input2 input3 )
 print $ random_sort_check prop_model qsort ( random_strings input1 input2 input3 )
 print $ random_sort_check prop_idempotent bubbleOnce ( random_strings input1 input2 input3 )
 print $ random_sort_check prop_smallest_first bubbleOnce ( random_strings input1 input2 input3 )
 print $ random_sort_check prop_model bubbleOnce ( random_strings input1 input2 input3 )

random_strings in1 in2 in3 =
 genStrings (randoms (getGen (read in1 :: Int)) :: [Int]) -- seed
 (read in2 :: Int) -- maxStrings
 (read in3 :: Int) -- maxLength of string 

makeChar rand = chr (65 + (mod rand 58))

getGen seed = mkStdGen seed

-- From task 2.2
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

-- sorting functions to use in the testing:

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x:xs) = qsort lhs ++ [x] ++ qsort rhs
 where lhs = filter (< x) xs
       rhs = filter (>= x) xs

-- one round of bubble sort, works sometimes:
bubbleOnce :: Ord a => [a] -> [a]
bubbleOnce [] = []
bubbleOnce [x] = [x]
bubbleOnce (x:y:xs) =
 if x < y
 then x : bubbleOnce (y:xs)
 else y : bubbleOnce (x:xs)

-- random_sort_check prop f strings
-- prop = property to be tested. Given an (sorting_function, input_string) pair,
-- returns True if the property holds, False otherwise
-- f = function that, given a string to be sorted, tries to sort it.
-- the function evaluates to a list of strings for which the property did not hold
-- strings is the test set of strings

random_sort_check :: ((String -> String) -> String -> Bool) -> (String -> String) -> [String] -> [String]
random_sort_check prop f strings = [xs | xs <- strings, not (prop f xs)]
-- Your code starts here:

prop_idempotent :: (String -> String) -> String -> Bool
prop_idempotent f xs = f (f xs) == f xs

prop_smallest_first :: (String -> String) -> String -> Bool
prop_smallest_first _ [] = True
prop_smallest_first f xs = (head (f xs) == minimum xs)

prop_model :: (String -> String) -> String -> Bool
prop_model f xs = sort xs == f xs-}