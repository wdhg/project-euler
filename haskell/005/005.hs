main = print $ head [x | x <- [20,40..], all (\a -> x `mod` a == 0) [2..20]]
