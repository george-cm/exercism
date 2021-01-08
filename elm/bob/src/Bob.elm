module Bob exposing (hey)


hey : String -> String
hey remark =
    let
        trimmedRemark : String
        trimmedRemark =
            String.trim remark

        allcapsRemark : String
        allcapsRemark =
            String.toUpper trimmedRemark
    in
    if String.isEmpty trimmedRemark then
        "Fine. Be that way!"

    else if allNumbers trimmedRemark then
        "Whatever."

    else if allNumbers (String.slice 0 -1 trimmedRemark) then
        "Sure."

    else if String.endsWith "?" trimmedRemark then
        if allcapsRemark == trimmedRemark then
            if noLetters trimmedRemark then
                "Sure."

            else
                "Calm down, I know what I'm doing!"

        else
            "Sure."

    else if allcapsRemark == trimmedRemark then
        "Whoa, chill out!"

    else
        "Whatever."


allNumbers : String -> Bool
allNumbers remark =
    let
        removedCommas : String
        removedCommas =
            String.replace "," "" remark

        splitRemark : List String
        splitRemark =
            String.split " " removedCommas
    in
    List.all isNumber splitRemark


isNumber : String -> Bool
isNumber str =
    case String.toFloat str of
        Just n ->
            True

        Nothing ->
            False


noLetters : String -> Bool
noLetters str =
    List.all (\char -> not (Char.isAlpha char)) (String.toList str)
