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

let rec iter (fish : int list) (i : int) : int =
    if i = 0 then List.length fish 
    else (
        let update = List.fold_left (fun acc f -> 
                if f = 0 then acc @ [6;8] else acc @ [f-1]
            ) [] fish in
        iter update (i-1)
    )

let main1 =
    let fl = read_lines "input.in" in
    Printf.printf "read lines\n";
    let fish = make_list (explode (List.nth fl 0)) in
    let res = iter fish 80 in
    Printf.printf "star1: %d\n" res

let () = main1;;
