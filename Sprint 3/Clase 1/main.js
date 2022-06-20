const p1 = document.getElementById("para1");
console.log(p1.textContent);
const h1Element = document.querySelector("h1");
console.log(h1Element);

const listItems = document.querySelectorAll("ul > li");
console.log(listItems);

listItems.forEach((item) => {
    console.log(item.textContent)
});
let textos = document.getElementById("texto")
console.log(textos.attributes[1])
textos.innerHTML = "cissad"
let listaSinOrden = document.createElement("ul");
let elemento1Lista = document.createElement("li");
let elemento2Lista = document.createElement("li");
document.body.appendChild(listaSinOrden);

elemento1Lista.textContent = "asdasdasdassadd";
elemento2Lista.textContent = "xczxccx";
listaSinOrden.appendChild(elemento1Lista);
listaSinOrden.appendChild(elemento2Lista);
h1Element.style.color = "blue";

var i = 1;

const button = document.getElementById("btn");
button.addEventListener("click", () => {
    if (i == 101) {
        alert("trolo")
    } else {
        alert("Gracias UwU apretaste: " + i + "/100");
        i++;
        textos.className += " centrado";
    };
});

