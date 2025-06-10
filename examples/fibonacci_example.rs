use fibonacci_rs::Fibonacci;

fn main() {
    let mut fib = Fibonacci::new();
    for i in 0..100 {
        match fib.next() {
            Some(n) => println!("Fibonacci number {}: {}", i, n),
            None => {
                println!("Overflow occurred, stopping iteration.");
                break;
            }
        }
    }
}