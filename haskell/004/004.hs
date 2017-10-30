isPal :: Integer -> Bool
isPal x = (show x) == (reverse $ show x)

main = print $ maximum [a * b | a <- [100..999], b <- [100..999], isPal $ a * b]
