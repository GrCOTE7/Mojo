use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("langages1/count/n.txt").unwrap();
    let reader = BufReader::new(file);
    let n: u64 = reader.lines().next().unwrap().unwrap().parse().unwrap();

    let mut count = 0u64;
    for _ in 0..n {
        count += 1;
    }

    println!("Rust counted to {}", count);
}

// Compilation:
// rustc -C opt-level=3 -o langages1/count/n_rs langages1/count/n.rs
// -C opt-level=3 : demande une optimisation maximale (comme -O3 en C++)
// -o langages1/count/n_rs : crée un exécutable nommé n_rs dans le dossier langages1/count/

// Exécution:
// ./langages1/count/n_rs
