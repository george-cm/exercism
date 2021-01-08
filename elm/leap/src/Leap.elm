module Leap exposing (isLeapYear)


isLeapYear : Int -> Bool
isLeapYear year =
    case ( isDivisibleByN 4 year, isDivisibleByN 100 year, isDivisibleByN 400 year ) of
        ( False, _, _ ) ->
            False

        ( True, False, _ ) ->
            True

        ( True, True, False ) ->
            False

        ( True, True, True ) ->
            True


isDivisibleByN : Int -> Int -> Bool
isDivisibleByN n year =
    modBy n year == 0
