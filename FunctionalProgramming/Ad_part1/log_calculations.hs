import Data.Monoid
import Distribution.Simple.Program.HcPkg (list)

makeFunc :: Num b => (Char, b) -> b -> b
makeFunc ('+',x) = (+x)
makeFunc ('*',x) = (*x)
makeFunc _ = \x -> 0

main = do
 input1 <- getLine
 print $ myFunc (read input1 :: [(Char,Int)]) (1,"")

applyLog :: Monoid b => (a,b) -> (a -> (a,b)) -> (a,b) 
applyLog (x,log) f = let (y,logEntry) = f x in (y,log `mappend` logEntry) 

--myFunc :: [(Char,Int)] -> (Int,String) -> (Int,String)
myFunc [] state = state
myFunc ((op,n):xs) state =
  let f val = (makeFunc (op,n) val, "Applied function '" ++ [op] ++ "'" ++ show n ++ ";")
  in myFunc xs (applyLog state f)