{-import Data.List

type Triangle = (Int,Int,Int)

main = do
 input1 <- getLine
 print $ exhaustive_triangle_check prop_sorted_triangles rightTriangles (read input1 :: Int)
 print $ exhaustive_triangle_check prop_right_triangles rightTriangles (read input1 :: Int)
 print $ exhaustive_triangle_check prop_correct_perimeters rightTriangles (read input1 :: Int)
 print $ exhaustive_triangle_check prop_sorted_triangles someTriangles (read input1 :: Int)
 print $ exhaustive_triangle_check prop_right_triangles someTriangles (read input1 :: Int)
 print $ exhaustive_triangle_check prop_correct_perimeters someTriangles (read input1 :: Int)

-- triangle-computing functions to use in the testing:

rightTriangles :: Int -> [Triangle]
rightTriangles length = [(a,b,c) | c <- [1..length], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == length]

someTriangles :: Int -> [Triangle]
someTriangles length
 | length < 10 = []
 | otherwise = [(length-8,3,4)]

-- exhaustive_triangle_check prop f max
-- prop = property to be tested. Given an (Int, [Triangle]) pair, returns True if the property holds, False otherwise
-- f = function that, given an int n, finds the right triangles with perimeter n.
-- max = maximum value for which triangles are computed using f and tested using prop.
-- the function evaluates to a list [(Int,[Triangle])] such that if (n,trs) is in the list, then
-- f i == trs and (i,trs) fails to satisfy property prop.

exhaustive_triangle_check :: (Int -> [Triangle] -> Bool) -> (Int -> [Triangle]) -> Int -> [(Int,[Triangle])]
exhaustive_triangle_check prop f max = [(i,f i) | i <- [1..max], not $ prop i (f i)]

-- Your code starts here:
prop_sorted_triangles :: Int -> [Triangle] -> Bool
prop_sorted_triangles n trs = trs == sort trs

prop_right_triangles :: Int -> [Triangle] -> Bool
prop_right_triangles n trs = foldl (\acc (a,b,c) -> acc && (a^2+b^2==c^2 || b^2+c^2==a^2)) True trs

prop_correct_perimeters :: Int -> [Triangle] -> Bool
prop_correct_perimeters n trs = foldl (\acc (a,b,c) -> acc && (a+b+c==n)) True trs-}
