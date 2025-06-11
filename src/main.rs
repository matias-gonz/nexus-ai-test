se clap::Parser;
use std::fs;
use std::path::Path;

/// A simple file copy tool
#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    /// The source file to copy
    #[arg(short, long)]
    source: String,

    /// The destination file to copy to
    #[arg(short, long)]
    destination: String,
}

fn main() {
    let args = Args::parse();

    let source_path = Path::new(&args.source);
    let dest_path = Path::new(&args.destination);

    if let Err(e) = fs::copy(source_path, dest_path) {
        eprintln!("Error copying file: {}", e);
        std::process::exit(1);
    }

    println!("File copied successfully from {} to {}", args.source, args.destination);
}
