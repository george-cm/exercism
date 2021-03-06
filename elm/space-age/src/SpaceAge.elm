module SpaceAge exposing (Planet(..), ageOn)


type Planet
    = Mercury
    | Venus
    | Earth
    | Mars
    | Jupiter
    | Saturn
    | Uranus
    | Neptune


ageOn : Planet -> Float -> Float
ageOn planet seconds =
    let
        secondsInAnEarthYear : Float
        secondsInAnEarthYear =
            31557600
    in
    case planet of
        _ ->
            1 / orbitalPeriod planet * seconds / secondsInAnEarthYear



-- ORBITAL PERIODS AS FRACTIONS OF EARTH ORBITAL PERIOD (1.0)


orbitalPeriod : Planet -> Float
orbitalPeriod planet =
    case planet of
        Mercury ->
            0.2408467

        Venus ->
            0.61519726

        Earth ->
            1.0

        Mars ->
            1.8808158

        Jupiter ->
            11.862615

        Saturn ->
            29.447498

        Uranus ->
            84.016846

        Neptune ->
            164.79132
