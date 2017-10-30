isqrt :: Integer -> Float
isqrt n = sqrt $ fromInteger n

isPrime :: Integer -> Bool
isPrime n = null [x | x <- 2 : [3,5..(ceiling $ isqrt n)], n `mod` x == 0]

primes :: [Integer]
primes = 2 : filter isPrime [3,5..]

main = print $ primes !! 10000
