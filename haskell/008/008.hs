import Data.List.Split

getData :: String -> [[Char]]
getData filename = map (\a -> splitOn "" a) $ splitOn "\n" $ readFile filename

main = do
  let contents = getData "data.txt"
  print contents
