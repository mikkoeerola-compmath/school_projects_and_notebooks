import Data.List ( sort )
import Control.Monad ( guard )

sortTriangle (a,b,c) = (x,y,z)
  where x:y:[z] = sort [a,b,c]

main = do
 input1 <- getLine
 print $ sort $ map sortTriangle $ rightTriangles (read input1 :: Int)

rightTriangles :: Int -> [(Int,Int,Int)]
rightTriangles length = do
   a <- [1..length]
   b <- [a..length]
   c <- [5..length]
   guard ((a^2 + b^2 == c^2) && (a+b+c==length))
   return (a,b,c)
