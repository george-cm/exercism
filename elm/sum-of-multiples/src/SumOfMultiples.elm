module SumOfMultiples exposing (sumOfMultiples)

import Html exposing (text)


sumOfMultiples : List Int -> Int -> Int
sumOfMultiples divisors limit =
    let
        ints : List Int
        ints =
            List.range 1 (limit - 1)
    in
    List.sum (List.filter (isMultiple divisors) ints)


isMultiple : List Int -> Int -> Bool
isMultiple divisors num =
    if List.any (\n -> modBy n num == 0) divisors then
        True

    else
        False
