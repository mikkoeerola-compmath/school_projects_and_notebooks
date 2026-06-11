import Control.Applicative
import Data.Monoid

type Birds = Int 
type Pole = (Birds,Birds) 

logBirds :: (Int,Int) -> [(Char,Int)] -> Writer [String] (Int, Int) 

logBirds (x,y) [] = do
 tell ["No more birds landing."]
 return (x,y)

logBirds (x,y) (('l',inc):steps) = do
 logBirdLeft inc (x,y) steps
 
logBirds (x,y) (('r',inc):steps) = do
 logBirdRight inc (x,y) steps
 
logBirdLeft :: Birds -> Pole -> [(Char,Int)] -> Writer [String] (Int, Int)
logBirdLeft inc (left, right) steps
 | abs ((left + inc) - right) < 4 = do
              tell ["left: " ++ show (left + inc)]
              logBirds (left+inc, right) steps
 | otherwise = do
               tell [(show inc) ++ " birds landing on the left caused Pierre to fall down!"]
               return (0, 0)

logBirdRight :: Birds -> Pole -> [(Char,Int)] -> Writer [String] (Int, Int)
logBirdRight inc (left, right) steps
 | abs ((right + inc) - left) < 4 = do
                 tell ["right: " ++ show (right + inc)]
                 logBirds (left, right+inc) steps
 | otherwise = do
                tell [(show inc) ++ " birds landing on the right caused Pierre to fall down!"]
                return (0, 0)

main = do
 input1 <- getLine
 print $ runWriter $ logBirds (0,0) (read input1::[(Char,Int)] )


newtype Writer w a = Writer { runWriter :: (a, w) }

--here
instance Functor (Writer w)  where
    fmap f (Writer (a, w)) = Writer (f a, w)

instance Monoid w => Applicative (Writer w) where
    pure a = Writer (a, mempty)
    (Writer (af,wx)) <*> (Writer (a, wy)) = Writer (af a, wx <> wy )

instance Monoid w => Monad (Writer w) where
    Writer (a,w1) >>= f =
        let Writer (b, w2) = f a
        in Writer (b, w1 <> w2)


tell :: [String] -> Writer [String] ()
tell xs = Writer ((), xs)
