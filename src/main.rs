use clap::Parser;
use std::fs;
use std::path::Path;
use std::process;

/// A simple file copier CLI application
#[derive(Parser, Debug)]
#[clap(version, about, long_about = None)]
struct Args {
    /// The path to the source file
    #[clap(value_parser)]
    source: String,

    /// The path to the destination file
    #[clap(value_parser)]
    destination: String,
}

fn main() {
    let args = Args::parse();

    let source_path = Path::new(&args.source);
    let dest_path = Path::new(&args.destination);

    if !source_path.exists() {
        eprintln!("Error: Source file '{}' does not exist.", args.source);
        process::exit(1);
    }

    match fs::read_to_string(source_path) {
        Ok(contents) => {
            match fs::write(dest_path, contents) {
                Ok(_) => {
                    println!("File copied successfully from '{}' to '{}'.", args.source, args.destination);
                }
                Err(err) => {
                    eprintln!("Error: Failed to write to destination file '{}': {}", args.destination, err);
                    process::exit(1);
                }
            }
        }
        Err(err) => {
            eprintln!("Error: Failed to read source file '{}': {}", args.source, err);
            process::exit(1);
        }
    }
}
