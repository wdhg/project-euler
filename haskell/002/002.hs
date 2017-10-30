fibs :: [Integer]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

main = do
  print (sum [x | x <- takeWhile (<4000000) fibs, x `mod` 2 == 0])
