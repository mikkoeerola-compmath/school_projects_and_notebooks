let input = document.getElementById("type-input");
let list = document.getElementById("todo");
let form = document.getElementById("form");

form.addEventListener("submit", submitHandler);
list.addEventListener("click", listClickHandler);

function addListItem(text) {
  let item = document.createElement("li");
  item.textContent = text;
  list.append(item);
};

function submitHandler(e) {
 e.preventDefault();

 let st = input.value;
  if (st.trim()) {
    addListItem(st);
    input.value = "";
  }
}

function listClickHandler(e) {
  let item = e.target;
  if(item.tagName == "LI") {
    if(item.classList.contains("done")) {
      item.remove();
    } else {
      item.classList.add("done");
    }
  }
}
