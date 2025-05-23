use clap::Parser;

/// A simple adder CLI
#[derive(Parser, Debug)]
#[command(author = "Your Name", version = "0.1", about = "Adds two numbers", long_about = None)]
struct Args {
    /// The first number to add
    #[arg(short, long)]
    a: i32,

    /// The second number to add
    #[arg(short, long)]
    b: i32,
}

fn main() {
    let args = Args::parse();

    let sum = args.a + args.b;

    println!("The sum of {} and {} is {}", args.a, args.b, sum);
}
