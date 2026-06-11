form.addEventListener("submit", submitHandler);

function submitHandler(e) {
  e.preventDefault();

  let form = document.getElementById("form");
  let input = document.getElementById("type-input");
  let replace = document.getElementById("receive-input");

  let st = input.value;
  if (st.trim()) {
    replace.textContent = st;
    input.value = "";
  }
};


