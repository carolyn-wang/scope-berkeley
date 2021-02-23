(define (split-at lst n)
  (cond 
;     ((<= (length (lst)) n)
;      (cons lst nil))
((= n 0) (cons nil lst))
    ((null? lst)
     (cons nil lst))
 (else (let ((end (split-at (cdr lst) (- n 1))))
            (cons (cons (car lst) (car end)) (cdr end))))))
;     (else
;      (let end
;           (split-at
;           (cdr lst)
;           (- n 1)))
;      (cons (cons (car lst) (car end)) (cdr lst)))))

(define (compose-all funcs)
  (lambda (x)
    (if (null? funcs)
        x
        ((compose-all (cdr funcs)) ((car funcs) x)))))
