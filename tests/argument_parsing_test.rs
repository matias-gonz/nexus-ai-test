use std::process::Command;

#[test]
fn test_missing_arguments()
{
    let status = Command::new("cargo")
        .args(&["run"]) // No source and destination
        .status()
        .expect("Failed to execute command");

    assert!(!status.success());
}

#[test]
fn test_invalid_source_file()
{
    let source_file = "non_existent_file.txt";
    let destination_file = "destination.txt";

    let status = Command::new("cargo")
        .args(&["run", "--", source_file, destination_file])
        .status()
        .expect("Failed to execute command");

    assert!(!status.success());
}
