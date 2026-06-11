function setCookies() {
  // TODO: Get form values. getElementById() might be useful here.
  const form = document.getElementById("myForm");
  const txt1Content = document.getElementById("text1").value;
  const txt2Content = document.getElementById("text2").value;
  const checkContent = document.getElementById("checkbox").checked;
  let checkString = checkContent.toString();

  // TODO: Set cookie for each form value.

  document.cookie = `text1=${txt1Content}`;
  document.cookie = `text2=${txt2Content}`;
  document.cookie = `checkbox=${checkString}`;

  form.action = '/';
  form.submit();
}
