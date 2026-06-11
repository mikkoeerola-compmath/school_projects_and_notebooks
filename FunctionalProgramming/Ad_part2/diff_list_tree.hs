import qualified Data.Monoid as Mon
import Control.Arrow (ArrowChoice(right))

main = do
 input1 <- getLine 
 input2 <- getLine 
 print $ makeDiffTree (read input1::[(String,String)] ) EmptyTree
 print $ findElems (read input2 :: [String]) ( makeDiffTree (read input1::[(String,String)] ) EmptyTree ) []

makeDiffTree :: [(String,String)] -> Tree String Char -> Tree String Char
makeDiffTree [] tree = tree
makeDiffTree ((key,val):inputs ) tree = makeDiffTree inputs (treeInsert key val tree)

findElems :: [String] -> Tree String Char -> [(String,String)] -> [(String,String)]
findElems [] tree founds = founds
findElems (key:keys) tree founds = findElems keys tree updatedFounds
 where updatedFounds = case (treeElem key tree) of 
                            Nothing -> founds
                            Just found -> (key,found):founds

-- DiffList 

newtype DiffList a = DiffList { getDiffList :: [a] -> [a] }

instance (Eq a) => Eq (DiffList a) where
 (DiffList x) == (DiffList y) = fromDiffList (DiffList x) == fromDiffList (DiffList y)

instance (Show a) => Show (DiffList a) where
 show (DiffList x) = show (fromDiffList (DiffList x))

toDiffList :: [a] -> DiffList a 
toDiffList xs = DiffList (xs++) 
 
fromDiffList :: DiffList a -> [a] 
fromDiffList (DiffList f) = f [] 

instance Semigroup (DiffList a) where
(<>) :: DiffList a -> DiffList a -> DiffList a
(DiffList f) <> (DiffList g) = DiffList (\xs -> f (g xs))
 
instance Monoid (DiffList a) where 
 mempty = DiffList (\xs -> [] ++ xs) 
(DiffList f) `mappend` (DiffList g) = DiffList (\xs -> f (g xs)) 

-- Data definition for a tree storing (k, DiffList v) pairs.
-- In our case, v is Char so DiffList v is like a string, but using DiffList, not List

data Tree k v = EmptyTree | Node k (DiffList v) (Tree k v) (Tree k v) deriving (Eq, Show)

-- Your code starts here:-}

treeInsert :: (Ord k) => k -> [v] -> Tree k v -> Tree k v
--treeInsert "" _ tree = tree
treeInsert key [] tree = tree
treeInsert key val EmptyTree = Node key (toDiffList val) EmptyTree EmptyTree
treeInsert key val (Node k dl left right)
   | k == key = Node k (toDiffList val `Main.mappend` dl) left right
   | key < k = Node k dl (treeInsert key val left) right
   | key > k = Node k dl left (treeInsert key val right)


treeElem :: (Ord k) => k -> Tree k v -> Maybe [v]
treeElem key EmptyTree = Nothing
--treeElem mempty _ = Nothing
treeElem key (Node k dl left right)
  | key == k = Just (fromDiffList dl)
  | key < k = treeElem key left
  | key > k = treeElem key right