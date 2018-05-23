module Main where

len :: [Int] -> Int
len [] = 0
len (x:xs) = 1 + len xs

ind :: [Int] -> [Int]
ind xs = [(len xs-1), (len xs-2) .. 0]

rev :: [Int] -> [Int]
rev xs = [ xs !! x | x <- ind xs]

main :: IO()
main = print $ rev [0,2..10]
