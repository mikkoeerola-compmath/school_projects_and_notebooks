data BinaryTree a = Empty | Node a (BinaryTree a) (BinaryTree a) deriving (Show, Read, Eq)

-- please notice that if the tree is empty, then all elements "trivially" fulfill the condition, thus True

evalAnd :: (BinaryTree Bool) -> Bool
evalAnd Empty = True
evalAnd (Node x y z) = x && ((evalAnd y) && (evalAnd z))

-- however for Or we require one True, so for us (evalOr Empty) gives False
evalOr :: (BinaryTree Bool) -> Bool
evalOr Empty = False
evalOr (Node x y z) = x || ((evalAnd y) || (evalAnd z))

instance Functor BinaryTree where
    fmap f Empty = Empty
    fmap f (Node x left right) = Node (f x) (fmap f left) (fmap f right)

main = do
 input1 <- getLine
 input2 <- getLine
 print $ allInTree
  (read input1 :: (BinaryTree Int))
  (>(read input2 :: Int))
 print $ existsInTree
  (read input1 :: (BinaryTree Int))
  (>(read input2 :: Int))


allInTree :: (BinaryTree a) -> (a -> Bool) -> Bool 
allInTree bt p = evalAnd $ fmap p bt

existsInTree :: (BinaryTree a) -> (a -> Bool) -> Bool
existsInTree bt p = evalOr $ fmap p bt
