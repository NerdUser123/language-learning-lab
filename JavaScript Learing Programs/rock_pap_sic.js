function rps(user,comp){
    if ( user === comp ) return " tie ";
    else if ( user === "rock" && comp === "paper" ) return " comp with paper wins over user with rock ";
    else if ( user === "paper" && comp === "scissor" ) return " comp with sis wins over user with paper ";
    else if ( user === "scissor" && comp === "rock" ) return " comp with rock wins over user with sis  ";
    else if ( user === "paper" && comp === "rock" ) return " user with paper wins over comp with rock ";
    else if ( user === "scissor" && comp === "paper" ) return " user with sis wins over comp with paper ";
    else if ( user === "rock" && comp === "scissor" ) return " user with rock wins over comp with sis  ";

}

console.log(rps("paper","rock"));