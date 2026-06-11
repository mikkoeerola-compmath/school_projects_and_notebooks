document.addEventListener("userDataReady", function(event) {
    let stringData = event.detail.jsonText;
    let parD = JSON.parse(stringData);
    let temp = document.querySelector("#user-card-template");
    let contactsDiv = document.querySelector("#contacts");

    parD.forEach(emt => {
        let tempCl = temp.content.cloneNode(true);
        let avatar = tempCl.querySelector("img");
        avatar.src = emt.avatar;
        avatar.alt = emt.firstName + " " + emt.lastName;

        tempCl.querySelector("h1").innerHTML = emt.firstName + " " + emt.lastName;
        tempCl.querySelector(".title.email").innerHTML = emt.email;
        let phone = document.createElement("span");
        phone.textContent = emt.phoneNumber;
        tempCl.querySelector(".phone").removeChild(tempCl.querySelector(".phone > span"));
        tempCl.querySelector(".phone").appendChild(phone);

        let address = tempCl.querySelector(".address");
        address.children[0].innerHTML = emt.address.streetAddress;
        address.children[1].innerHTML = emt.address.zipCode + " " + emt.address.city;
        address.children[2].innerHTML = emt.address.country;

        let hpage = tempCl.querySelector(".homepage > a");
        hpage.href = emt.homepage;
        hpage.textContent = emt.homepage;

        contactsDiv.appendChild(tempCl.querySelector(".card"));
    });

})

fetchUserData();