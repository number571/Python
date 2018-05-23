-- RSA ШИФРОВАНИЕ START --

module Main where

getN :: Integer -> Integer -> Integer 
getN p q = (*) p q   

getN' :: Integer -> Integer -> Integer
getN' p q = (*) ((-) p 1) ((-) q 1) 

getD :: Integer -> Integer -> Integer -> Integer
getD k n' e = div ((+) 1 ((*) k n')) e

enc :: Integer -> Integer -> Integer -> Integer
enc m c n = mod ((^) m c) n 

main :: IO()
main = do
    let _M = 111 

    let p = 101;        q = 53
    let n = getN p q;   n' = getN' p q

    let e = 3;      k = 2
    let d = getD k n' e

    let _E = enc _M e n;    _D = enc _E d n 
    print [_M, _E, _D]

-- RSA ШИФРОВАНИЕ END --
