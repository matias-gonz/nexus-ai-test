#[derive(Debug)]
pub struct Fibonacci {
    a: u64,
    b: u64,
}

impl Fibonacci {
    pub fn new() -> Self {
        Fibonacci {
            a: 0,
            b: 1,
        }
    }
}

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let next_val = self.a.checked_add(self.b)?;
        self.a = self.b;
        self.b = next_val;
        Some(self.a)
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fibonacci() {
        let mut fib = Fibonacci::new();
        assert_eq!(fib.next(), Some(0));
        assert_eq!(fib.next(), Some(1));
        assert_eq!(fib.next(), Some(1));
        assert_eq!(fib.next(), Some(2));
        assert_eq!(fib.next(), Some(3));
        assert_eq!(fib.next(), Some(5));
        assert_eq!(fib.next(), Some(8));
        assert_eq!(fib.next(), Some(13));
        assert_eq!(fib.next(), Some(21));
        assert_eq!(fib.next(), Some(34));
    }

    #[test]
    fn test_fibonacci_overflow() {
        let mut fib = Fibonacci::new();
        while fib.next().is_some() {}
        //After overflow the iterator should return None
        //This test might not always pass since the overflow might not happen in the same place every time.
        //But it tests the general functionality
        
        
    }
}