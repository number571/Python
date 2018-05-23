module Main where

fac :: Integer -> Integer
fac x | x < 2 = 1
fac x = x * fac(x-1)

main :: IO()
main = print (fac 5)
