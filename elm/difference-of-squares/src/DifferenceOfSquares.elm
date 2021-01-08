module DifferenceOfSquares exposing (difference, squareOfSum, sumOfSquares)


squareOfSum : Int -> Int
squareOfSum n =
    let
        numbersToSum : List Int
        numbersToSum =
            List.range 1 n
    in
    squareF (List.sum numbersToSum)


sumOfSquares : Int -> Int
sumOfSquares n =
    let
        numbersToSquare : List Int
        numbersToSquare =
            List.range 1 n
    in
    List.sum (List.map (\num -> num ^ 2) numbersToSquare)


difference : Int -> Int
difference n =
    squareOfSum n - sumOfSquares n


squareF : Int -> Int
squareF num =
    num * num
