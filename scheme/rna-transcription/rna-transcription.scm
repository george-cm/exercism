(import (rnrs))

(define (transform-nucleotide n)
  (cond ((equal? n "G") "C")
        ((equal? n "C") "G")
        ((equal? n "T") "A")
        ((equal? n "A") "U")))

(define (dna->rna dna)
  (if (= (string-length dna) 0)
    "" 
    (string-append 
      (transform-nucleotide (substring dna 0 1)) 
      (dna->rna (substring dna 1 (string-length dna))))))
