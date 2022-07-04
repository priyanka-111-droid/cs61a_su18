; Q1
(define (sign x)
  (
    cond[(> x 0) 1]
    [(< x 0) -1]
    [else 0]
  )
)

; Q2
(define (square x) (* x x))

(define (pow b n)
  (
      cond[ (= n 0) 1]
      [(even? n) (square (pow b (/ n 2)))]
      [(odd? n) 
          (* b (square(pow b (/(- n 1) 2)))
      )]
  )
)

; Q3
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (
    car(cdr s)
  )
)

(define (caddr s)
  (
    car(cddr s)
  )
)

; Q4
(define (ordered? s)
  (
      cond[(null? s) #t]
      [(null? (cdr s)) #t]
      [(<= (car s) (car(cdr s))) 
          (ordered?(cdr s))]
      [else #f]
  )
)

; Q5
(define (nodots s)
  

)

; Q6
(define (empty? s) (null? s))

(define (add s v)
    'YOUR-CODE-HERE
    )

; Q7
; Sets as sorted lists
(define (contains? s v)
    'YOUR-CODE-HERE
    )

; Q8
(define (intersect s t)
    'YOUR-CODE-HERE
    )

(define (union s t)
    'YOUR-CODE-HERE
    )