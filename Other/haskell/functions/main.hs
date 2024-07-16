e :: Double
e = exp 1

square :: Double -> Double
square x = x**2

cosSq :: Double -> Double
cosSq x = square (cos x)

cosSq' :: Double -> Double
cosSq' x = square $ cos x

cosSq'' :: Double -> Double
cosSq'' x = (square . cos) x

cosSq''' :: Double -> Double
cosSq''' = square . cos

f :: Double -> Double
f x = sqrt (x + 1)


