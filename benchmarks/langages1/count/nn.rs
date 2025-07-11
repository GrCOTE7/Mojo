use std::fs::read_to_string;
use std::time::Instant;

fn main() {
    let n: u64 = read_to_string("apps/count/n.txt").unwrap().trim().parse().unwrap();

    let start = Instant::now();
    let mut count = 0;
    for _ in 0..n {
        count += 1;
    }
    let duration = start.elapsed().as_secs_f64();

    println!("✅ Rust → Counted to {} in {:.3}s", count, duration);
}
