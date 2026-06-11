{-existsInTree :: (BinaryTree a) -> (a -> Bool) -> Any
existsInTree bt f = evalOr $ fmap (Any . f) bt 

instance Functor BinaryTree where
    fmap f Empty = Empty
    fmap f (Node x left right) = Node (f x) (fmap f left) (fmap f right)

instance Foldable BinaryTree where
    foldMap f Empty = mempty
    foldMap f (Node x l r) = (foldMap f l <> f x) <> foldMap f r-}