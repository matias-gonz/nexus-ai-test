use std::process::Command;
use std::fs;
use std::path::Path;

#[test]
fn test_file_copy()
{
    // Create a dummy source file
    let source_file = "test_source.txt";
    let destination_file = "test_destination.txt";
    let content = "This is a test file.";
    fs::write(source_file, content).expect("Unable to write to source file");

    // Run the file_copier CLI
    let status = Command::new("cargo")
        .args(&["run", "--", source_file, destination_file])
        .status()
        .expect("Failed to execute command");

    // Assert that the command was successful
    assert!(status.success());

    // Verify that the destination file exists
    assert!(Path::new(destination_file).exists());

    // Verify that the destination file contains the same content as the source file
    let destination_content = fs::read_to_string(destination_file).expect("Unable to read destination file");
    assert_eq!(content, destination_content);

    // Clean up the created files
    fs::remove_file(source_file).expect("Unable to remove source file");
    fs::remove_file(destination_file).expect("Unable to remove destination file");
}
