module Main where

for :: [Integer] -> IO() -> IO()
for [] _ = return ()
for (x:xs) code = do
    code
    for xs code

main :: IO()
main = for range $ print message
    where 
        range = [0..10]
        message = "Hello World"
