module Main where

exerc1 :: Int -> Int
exerc1 x = x*3

exerc2 :: Int -> Int
exerc2 n
  | n > 0     = factorial n
  | otherwise = n * 2

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n - 1)

main = do
  print(reverse(map exerc1 [20,19..1]))

  print(map exerc2 [10])