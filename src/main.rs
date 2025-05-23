use std::io;

fn main() {
    println!("Enter the first number:");
    let mut num1 = String::new();
    io::stdin().read_line(&mut num1)
        .expect("Failed to read line");
    let num1: i32 = num1.trim().parse()
        .expect("Please type a number!");

    println!("Enter the second number:");
    let mut num2 = String::new();
    io::stdin().read_line(&mut num2)
        .expect("Failed to read line");
    let num2: i32 = num2.trim().parse()
        .expect("Please type a number!");

    let sum = num1 + num2;
    println!("The sum is: {}", sum);
}
