module RNATranscription exposing (toRNA)


toRNA : String -> Result String String
toRNA dna =
    case String.all isValidDnaChar dna of
        True ->
            Ok (String.map changeDnaChar dna)

        False ->
            Err "Invalid input"


changeDnaChar : Char -> Char
changeDnaChar c =
    case c of
        'G' ->
            'C'

        'C' ->
            'G'

        'T' ->
            'A'

        'A' ->
            'U'

        _ ->
            c


isValidDnaChar : Char -> Bool
isValidDnaChar c =
    let
        validDnaChars : String
        validDnaChars =
            "GCTA"
    in
    String.contains (String.fromChar c) validDnaChars
