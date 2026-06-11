module Eq3 (Eq3,(===)) where

import Bool3
import MaybeNull as Mn

class Eq3 a where
 (===) :: a -> a -> Bool3

instance (Eq3 a) => Eq3 (MaybeNull a) where
 (===) (JustVal x) (JustVal y) = (===) x y
 (===) Null _ = Unk3
 (===) _ Null = Unk3
 (===) _ _ = False3

instance Eq3 Bool3 where
 (===) x y = (x &&& y) ||| ((not3 x) &&& (not3 y))
 (===) _ _ = False3