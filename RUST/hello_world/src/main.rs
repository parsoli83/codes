use std::io;

fn main() {
    let mut l=vec![11,1,1,1,1,1,3,2,0];
    dbg!(&l);
    for i in 1..l.len(){
        println!("here");
        let ii=l[i]*1;
        for j in 0..i{
            let jj=l[j]*1;
            if l[j]>i{
                println!("{} ------ {}",ii,jj);
                l[i]=jj;
                l[j]=ii;
                break;
            }
        }
    }dbg!(l);
}

fn read() -> String{
    let mut input=String::new();
    io::stdin().read_line(&mut input).expect("unable to read");
    input.trim().to_string()
}

fn input() -> Vec<char>{
    read().chars().collect()
}
/*  let n=read().parse::<i32>().expect("Failed to parse");
    let inp=read();
    (n,inp.split_whitespace().map(|x| x.parse::<i32>().expect("Failed to parse")).collect())
    let list: Vec<_>=inp.split_whitespace().collect();
    let qu: Vec<_>=read().chars().collect();
    (list[0].parse::<i32>().expect("Failed to parse"),
    list[1].parse::<i32>().expect("Failed to parse"),qu)
*/

