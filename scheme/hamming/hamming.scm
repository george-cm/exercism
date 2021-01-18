(import (rnrs))

(define (hamming-distance strand-a strand-b)
  (define (sum-list lst)
    (if (not (pair? lst)) 0
        (+ (car lst) (sum-list (cdr lst)))))
  (assert (= (string-length strand-a) (string-length strand-b)))
  (sum-list 
    (map (lambda (l1 l2) (if (equal? l1 l2) 0 1)) 
      (string->list strand-a) (string->list strand-b))))
