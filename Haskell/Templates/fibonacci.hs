module Main where

fib :: Integer -> Integer
fib x | x <= 3 = 1
fib x = fib(x-1) + fib(x-2)

main :: IO()
main = print (fac 5)
