num :: Integer
num = 100

sumOfSquares :: Integer -> Integer
sumOfSquares x = sum $ map (\a -> a * a) [1..x]

squareOfSums :: Integer -> Integer
squareOfSums x = do
  let a = sum [1..x]
  a * a

main = print $ (squareOfSums num) - (sumOfSquares num)
