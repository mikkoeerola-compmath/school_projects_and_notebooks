import Control.Applicative -- this line may be unnecessary in your local testing if you have a more recent version of the Haskell platform

data BinaryTree a = Empty | Node a (BinaryTree a) (BinaryTree a) deriving (Show, Read, Eq)

makeFunc ('+',x) = (+x)
makeFunc ('*',x) = (*x)
makeFunc _ = \x -> 0

main = do
 input1 <- getLine
 input2 <- getLine
 print $ (fmap makeFunc (read input1 :: (BinaryTree (Char,Int)) ) )
  <*>
  (read input2:: (BinaryTree Int))

instance Functor BinaryTree where
    fmap f Empty = Empty
    fmap f (Node a left right) = Node (f a) (fmap f left) (fmap f right)

instance Applicative BinaryTree where
    pure a = Node a Empty Empty
    Empty <*> _ = Empty
    _ <*> Empty = Empty
    (Node f leftF rightF) <*> (Node x left right) = 
        Node (f x) (leftF <*> left) (rightF <*> right)