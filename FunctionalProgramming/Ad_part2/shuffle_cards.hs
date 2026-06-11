{-import System.Random
import Data.List

type Card = (Char,Int)

-- 's'pades, 'c'lubs, 'd'iamonds, 'h'hearts, Ace is 14.
cards = [(s,n) | s <- ['s','c','d','h'], n <- [2..14] ]

getGen seed = mkStdGen seed

main = do
 input1 <- getLine
 print $ shuffleCards (read input1 :: Int)

-- Your code starts here:

shuffleCards ::  Int -> [Card]
shuffleCards seed = let order = take 52 $ randoms (getGen seed) :: [Integer]
                        paired = zip order cards
                    in map snd $ sortOn fst paired-}