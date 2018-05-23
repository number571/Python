{-# LANGUAGE MultiWayIf #-}

module Main where

import System.IO (hSetBuffering, stdout, BufferMode(..))
import Data.Char (chr, ord, toUpper, isAlpha, isDigit)

encrypt :: Char -> Int -> Char
encrypt c k = if  
    | isAlpha c -> chr $ (ord c' + k - 13) `mod` 26 + ord 'A'
    | isDigit c -> chr $ (ord c  + k - 13) `mod` 10 + ord '0'
    | otherwise -> c
    where c' = toUpper c

decrypt :: Char -> Int -> Char
decrypt c k = if  
    | isAlpha c -> chr $ (ord c' - k - 13) `mod` 26 + ord 'A'
    | isDigit c -> chr $ (ord c  - k - 13) `mod` 10 + ord '0'
    | otherwise -> c
    where c' = toUpper c

caesar :: Char -> String -> Int -> String
caesar m s k = if
    | m == 'e' || m == 'E' -> [encrypt c k | c <- s]
    | m == 'd' || m == 'D' -> [decrypt c k | c <- s]
    | otherwise -> "Mode is not found"

main :: IO()
main = do
    hSetBuffering stdout NoBuffering
    putStr "Mode: "   ; mode    <- getChar; getChar
    putStr "Message: "; message <- getLine
    putStr "Key: "    ; key     <- readLn :: IO Int
    putStrLn $ "Final: " ++ caesar mode message key
