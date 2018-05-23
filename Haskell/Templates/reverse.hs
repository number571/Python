module Main where

len :: [Int] -> Int
len [] = 0
len (x:xs) = 1 + len xs

fun :: [Int] -> [Int]
fun xs = [(len xs-1), (len xs-2) .. 0]

rev :: [Int] -> [Int]
rev xs = [ xs !! x | x <- fun xs]

main :: IO()
main = print $ rev [0,2..10]
