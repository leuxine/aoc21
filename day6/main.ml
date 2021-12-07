let read_lines filename =
    let f = open_in filename in
    let rec loop () =
        try
            let next = input_line f in
            next :: loop ()
        with End_of_file ->
            close_in f;
      []
            in loop ()

let explode (input : string) : char list = List.init (String.length input) (String.get input) 

let rec make_list (s:char list) : int list = 
    match s with
        | [] -> []
        | c::cs -> (
            if c = ',' then make_list cs
            else (
                let i = int_of_string (String.make 1 c) in
                [i] @ make_list cs
            )
        )

let rec update (fish : int list) : int list = 
    match fish with
        | [] -> []
        | x::[] -> [0]
        | x::y::xs -> []

let rec iter (fish : int list) (i : int) : int =
    if i = 0 then List.fold_left (+) 0 fish  
    else (
        let update = List.fold_left (fun acc f -> 
                if f = 0 then acc @ [6;8] else acc @ [f-1]
            ) [] fish in
        iter update (i-1)
    )

let rec get_amount (il : int list) (i : int) : int =
    match il with
        | [] -> 0
        | x::xs -> if x = i then 1 + get xs i else get xs i 

let main =
    let fl = read_lines "input.in" in
    let fish = make_list (explode (List.nth fl 0)) in
    let zero = List.init 9 (fun x -> 0) in
    let _, start = List.fold_left (fun (i, acc) z ->
        (i + 1, acc @ [get_amount fish i])
    ) (0,[]) zero in 
    let res1 = iter start 80 in
    let res2 = iter start 256 in
    Printf.printf "star1: %d\nstar2: %d\n" res1 res2

let () = main;;
