module CollatzConjecture exposing (collatz)


collatz : Int -> Result String Int
collatz start =
    if start > 0 then
        Ok (collatzSteps start)

    else
        Err "Only positive numbers are allowed"


collatzSteps : Int -> Int
collatzSteps val =
    case val of
        1 ->
            0

        _ ->
            1 + collatzSteps (nextStep val)


nextStep : Int -> Int
nextStep n =
    if modBy 2 n == 0 then
        n // 2

    else
        3 * n + 1
