use std::{
    fs::File,
    io::{BufReader, Read, Write},
    path::Path,
};

pub fn read_buf(input: &Path, on_read: &mut dyn FnMut(&[u8])) {
    let file = File::open(input).unwrap();
    let mut reader = BufReader::new(file);
    let mut buffer = [0u8; 8192];

    loop {
        let bytes_read = reader.read(&mut buffer).unwrap();
        if bytes_read == 0 {
            break;
        }
        // slice to length of what was read to prevent
        // stale bytes from previous reads
        on_read(&buffer[..bytes_read])
    }
}

pub fn write_file(output_path: &Path, data: String) -> Result<(), std::io::Error> {
    let mut file = File::options()
        .write(true)
        .create(true)
        .truncate(true)
        .open(output_path)?;
    write!(&mut file, "{data}")?;
    Ok(())
}
