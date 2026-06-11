import Data.Monoid

-- MaybeNull:

data MaybeNull a = JustVal a | Null deriving (Show, Read)

-- Bool3:

data Bool3 = False3 | Unk3 | True3 deriving (Eq,Show,Read) 

(&&&) :: Bool3 -> Bool3 -> Bool3
(&&&) x y
 | x == True3 && y == True3 = True3
 | x == False3 || y == False3 = False3
 |otherwise = Unk3

(|||) :: Bool3 -> Bool3 -> Bool3
(|||) x y
 | x == True3 || y == True3 = True3
 | x == False3 && y == False3 = False3
 |otherwise = Unk3

not3 :: Bool3 -> Bool3
not3 x
 | x == True3 = False3
 | x == False3 = True3
 |otherwise = Unk3

main = do
 input1 <- getLine
 print (mappendMaybeNullBool3s
  (read input1 :: [(MaybeNull Bool3)] ))

mappendMaybeNullBool3s bs = foldl (\acc b -> mappend acc b) mempty bs

instance Semigroup Bool3 where
    (<>) = (&&&)

instance Monoid Bool3 where
    mempty = False3

instance Semigroup a => Semigroup (MaybeNull a) where
    (<>) :: Semigroup a => MaybeNull a -> MaybeNull a -> MaybeNull a
    Null <> _ = Null
    _ <> Null = Null
    JustVal a <> JustVal b = JustVal (a <> b)

instance Monoid a => Monoid (MaybeNull a) where
    mempty = Null
