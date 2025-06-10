pub struct Fibonacci {
    a: u32,
    b: u32,
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
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        let next = self.a.checked_add(self.b)?;
        self.a = self.b;
        self.b = next;
        Some(self.a)
    }
}
