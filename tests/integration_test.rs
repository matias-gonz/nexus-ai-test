#[test]
fn test_fibonacci_sequence() {
    let mut fibonacci = fibonacci_rs::Fibonacci::new();
    assert_eq!(fibonacci.next(), Some(0));
    assert_eq!(fibonacci.next(), Some(1));
    assert_eq!(fibonacci.next(), Some(1));
    assert_eq!(fibonacci.next(), Some(2));
    assert_eq!(fibonacci.next(), Some(3));
    assert_eq!(fibonacci.next(), Some(5));
    assert_eq!(fibonacci.next(), Some(8));
    assert_eq!(fibonacci.next(), Some(13));
    assert_eq!(fibonacci.next(), Some(21));
    assert_eq!(fibonacci.next(), Some(34));

    // Test for overflow. The iterator should stop before overflowing.
    let mut fibonacci_overflow = fibonacci_rs::Fibonacci::new();
    let mut last_value = 0;
    while let Some(value) = fibonacci_overflow.next() {
        if value < last_value {
            // Overflow detected
            assert_eq!(fibonacci_overflow.next(), None);
            break;
        }
        last_value = value;
    }
}
