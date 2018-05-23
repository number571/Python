module Main where

summ :: [Integer] -> Integer
summ [] = 0
summ (x:xs) = do
    summ xs + x

main :: IO()
main = print . summ $ [0..5]
