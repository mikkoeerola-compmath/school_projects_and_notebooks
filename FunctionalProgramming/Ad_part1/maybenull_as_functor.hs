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
 input2 <- getLine
 print (applyToMaybeNull
  (&&& (read input1))
  (read input2 :: [(MaybeNull Bool3)]) )

applyToMaybeNull f xs = fmap (fmap f) xs

instance Functor MaybeNull where
    fmap f (JustVal a) = JustVal (f a) 
    fmap f Null = Null