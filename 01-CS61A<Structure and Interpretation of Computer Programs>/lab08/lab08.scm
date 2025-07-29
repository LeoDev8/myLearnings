(define (over-or-under num1 num2) (cond ((< num1 num2) -1) ((= num1 num2) 0) ((> num1 num2) 1)))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) (if (= 0 (modulo (max a b) (min a b))) (min a b) (gcd (modulo (max a b) (min a b)) (min a b))))

(define (remove item lst) (filter (lambda (x) (not (= x item))) lst))

(define (duplicate lst) 
    (if (null? lst)
        '()
        (cons (car lst) 
            (cons (car lst) (duplicate (cdr lst)))
        )
    )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (composed f g) (lambda (x) (f (g x))))

(define (repeat f n)
    (if (= n 1)
        (lambda (x) (f x))
        (lambda (x) ((repeat f (- n 1)) (f x)))
    )
)
