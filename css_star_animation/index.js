const frame = document.querySelector(".frame");
// let circle = prompt("How many circle you want?");
let number_of_shapes = 9;

for (let shape_number = 0; shape_number < number_of_shapes; shape_number++) {
    let square = document.createElement("div");
    let style = document.createElement("style");
    style.innerHTML = `
    .a${shape_number}{
    	animation-name: a${shape_number};
    }

    @keyframes a${shape_number} {
        50%{
            transform: rotate(${shape_number * 20}deg);
            height: 2.5rem;
            border-radius: 50%;
        }
    }`;

    square.appendChild(style);
    square.classList.add("square", `a${shape_number}`);
    frame.append(square);
}
