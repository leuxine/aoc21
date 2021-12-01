
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

let main1 = 
    let fl = read_lines "input.in" in
    let _, inc = List.fold_left (fun (last, acc) x ->     
        try (
            let n = int_of_string x in 
            if n > last then (n, acc + 1) else (n, acc)
        ) with _ -> last, acc
        ) (max_int, 0) fl
    in

    Printf.printf "star 1: %d\n" inc

let main2 = 
    let fl = read_lines "input.in" in
    let _,_,_, inc = List.fold_left (fun (f, s, t, acc) x ->
        try (
            let sum = if f <> max_int && s <> max_int && t <> max_int then 
                f + s + t else max_int in
            let n = int_of_string x in
            let new_sum = sum - f + n in
            if new_sum > sum then s, t, n, acc + 1 else s, t, n, acc
        ) with _ -> f, s, t, acc
    ) (max_int, max_int, max_int, 0) fl in

    Printf.printf "star 2: %d\n" inc

let () = main2;;

