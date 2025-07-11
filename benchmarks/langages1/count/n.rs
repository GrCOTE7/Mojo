use std::fs::read_to_string;
use std::path::Path;
// use std::num::ParseIntError;

fn main() {
    // Chemin du fichier dans le même dossier
    let path = Path::new("langages1/count/n.txt");

    if !path.exists() {
        eprintln!("❌ Erreur : Le fichier 'n.txt' est introuvable");
        return;
    }

    match read_to_string(path) {
        Ok(content) => match content.trim().parse::<u64>() {
            Ok(n) => {
                let n_plus = n + 1;
                for i in 1..n_plus {
                    if i < 4 {
                        print!("{}, ", i);
                    }
                }
                println!();
            }
            Err(_e) => {
                eprintln!("❌ Erreur : Le fichier 'n.txt' ne contient pas un entier valide");
            }
        },
        Err(_e) => {
            eprintln!("❌ Erreur : Impossible de lire le fichier 'n.txt'");
        }
    }
}
