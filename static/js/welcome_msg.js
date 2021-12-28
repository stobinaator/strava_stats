function welcome_user() {
  let getBody = document.body;

  let h1Element = document.querySelector(".welcome-msg");

  let date = new Date();
  let currentHour = date.getHours();

  let createTxtMsg;

  if (currentHour >= 4 && currentHour < 10) {
    createTxtMsg = "Good morning!";
  } else if (currentHour >= 10 && currentHour < 12) {
    createTxtMsg = "Good day!";
  } else if (currentHour >= 12 && currentHour < 18) {
    createTxtMsg = "Good afternoon!";
  } else if (currentHour >= 18 && currentHour < 22) {
    createTxtMsg = "Good evening!";
  } else if (currentHour >= 22 && currentHour < 4) {
    createTxtMsg = "Good night!";
  } else {
    createTxtMsg = "Are you from different planet!";
  }

  let createEleText = document.createTextNode(createTxtMsg);
  h1Element.appendChild(createEleText);
  getBody.appendChild(h1Element);
}