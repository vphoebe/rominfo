use std::path::PathBuf;

use clap::Parser;
use rominfo::{file::write_file, format::format_data, hashes::get_hashes};

#[derive(Parser)]
#[command(version, about, long_about = None)]
struct Cli {
    /// Binary files to hash
    input_files: Vec<PathBuf>,

    #[arg(short, long, default_value = "hashes.txt")]
    output_file: PathBuf,

    #[arg(short, long, default_value_t = false)]
    /// Output Redump DAT lines
    dat: bool,
}

fn main() {
    let cli = Cli::parse();
    let mut lines: Vec<String> = Vec::new();
    if cli.input_files.is_empty() {
        println!("No input files specified.");
        std::process::exit(1);
    }

    for input in &cli.input_files {
        let data = get_hashes(input);
        let line = format_data(&data, cli.dat);
        lines.push(line);
    }

    write_file(&&cli.output_file, lines.join("\n")).expect("failed to write output file");
    println!(
        "Wrote info for {} file(s) to {}",
        &cli.input_files.len(),
        &cli.output_file.display()
    )
}
