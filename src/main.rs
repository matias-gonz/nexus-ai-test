use clap::Parser;

/// Sums two numbers from the command line
#[derive(Parser, Debug)]
#[command(author = "Your Name", version = "0.1", about = "Sums two numbers", long_about = None)]
struct Args {
    /// The first number to sum
    #[arg(short, long)]
    num1: i32,

    /// The second number to sum
    #[arg(short, long)]
    num2: i32,
}

fn main() {
    let args = Args::parse();

    let sum = args.num1 + args.num2;

    println!("The sum of {} and {} is {}", args.num1, args.num2, sum);
}
