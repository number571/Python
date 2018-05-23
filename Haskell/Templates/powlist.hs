module Main where

powlist :: [Integer] -> Integer -> [Integer]
powlist list y = [x ^ y | x <- list]

main :: IO()
main = print . powlist [0..10] $ 2
