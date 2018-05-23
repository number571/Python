module Main where

len :: [Integer] -> Integer
len [] = 0
len (x:xs) = 1 + len xs

main :: IO()
main = print . len $ [0..100]
