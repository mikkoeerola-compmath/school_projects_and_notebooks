// TODO: Copy the setCookies function from the previous exercise
function setCookies() {
  const form = document.getElementById("myForm");
  const txt1Content = document.getElementById("text1").value;
  const txt2Content = document.getElementById("text2").value;
  const checkContent = document.getElementById("checkbox").checked;
  let checkString = checkContent.toString();

  // TODO: Set cookie for each form value.

  document.cookie = `text1=${txt1Content}`;
  document.cookie = `text2=${txt2Content}`;
  document.cookie = `checkbox=${checkString}`;

  // form.submit();
}

// TODO: Implement the getCookie function. It should take a cookie name as an argument and return the cookie value.
function getCookie(name) {
  let cookies = document.cookie.split(';');

  console.log(cookies);

  for(let i=0; i < cookies.length; ++i) {
    let cookieName = cookies[i].split('=')[0].trim();
    let value = cookies[i].split('=')[1].trim();

    console.log(name);
    console.log(cookieName);
    console.log(value);

    if(cookieName === name) return value;
  }
}


// DO NOT MODIFY BELOW THIS LINE
document.getElementById('submitButton').addEventListener('click', function() {
  setCookies();
  displayCookies();
});

function displayCookies() {
  document.getElementById('text1Cookie').textContent = "Text1: " + getCookie('text1');
  document.getElementById('text2Cookie').textContent = "Text2: " + getCookie('text2');
  document.getElementById('checkboxCookie').textContent = "Checkbox: " + getCookie('checkbox');
}