class (Eq a) => Eq3 a where
 (===) :: a -> a -> Bool
 (===) x y = x == y

instance (Eq3 a) => Eq3 (Maybe a) where
 (===) (Just x) (Just y) = (===) x y
 (===) Nothing Nothing = True
 (===) _ _ = False