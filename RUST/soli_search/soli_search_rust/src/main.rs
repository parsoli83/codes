use std::fs;
use std::env;


fn main() {
    let args: Vec<String> = env::args().collect();
    let l_inp:Vec<String> = read_input();
    
    let mut arg=String::new();
    for i in 1..args.len(){
        arg+=&args[i].to_string();
    }
    let mut best=0;
    let mut best_one=String::from("");
    for i in l_inp{
        let sco=sim_sent(&i, &arg);
        if sco>60 && sco>best{
            best=sco;
            best_one=i;
        }
    }
    if &best_one==""{
        println!("{}",false);
    }else{
        println!("{}",best_one);
    }
}
fn sim_word(word_1_: &str,word_2_: &str) -> i32{
    fn phrase(l: &Vec<char>,i1:usize,i2:usize) -> String{
        let mut fini=String::new();
        for i in i1..i2{
            fini+=&l[i].to_string();
        }
        fini
    }
    let word_1:Vec<_>=word_1_.chars().collect();
    let word_2:Vec<_>=word_2_.chars().collect();
    let mut best=0;
    for i11 in 0..word_1.len(){
        for i12 in i11..word_1.len()+1{
            let phrase_1=phrase(&word_1, i11, i12);
            for i21 in 0..word_2.len(){
                for i22 in i21..word_2.len()+1{
                    let phrase_2=phrase(&word_2, i21, i22);
                    if phrase_1==phrase_2 && phrase_1.len()>best as usize{
                        best=phrase_1.len();
                    }
                }
            }
        }
    }
    (best*100/(word_1.len()+word_2.len())) as i32
}
fn read_input() -> Vec<String>{
    let data = fs::read_to_string("/home/parsa/soli_search_rust/rust_database/input/inputs.txt")
    .unwrap();
    data.split("@").map(|x| x.to_string()).collect()
}
fn sim_sent(inp_1_: &str,inp_2_: &str) -> i32{
    let inp_1:Vec<String>=inp_1_.split_whitespace().map(|x| x.to_string()).collect();
    let inp_2:Vec<String>=inp_2_.split_whitespace().map(|x| x.to_string()).collect();
    let mut score=0;
    for i in &inp_1{
        for j in &inp_2{
            if sim_word(i,j)>60{
                score+=1;
            }
        }
    }
    //println!("sim_sent: {} , {}",inp_1_,inp_2_);
    score*200/(inp_1.len()+inp_2.len()) as i32
}
