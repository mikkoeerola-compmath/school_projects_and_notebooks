let list = document.getElementsByTagName("ul")[0];
addItemCount(list);

/**
 * 
 * @param {HTMLUListElement} list 
 */
function addItemCount(list) {
    let items = list.querySelectorAll(":scope > li");
    items.forEach(element => {
        let num = element.getElementsByTagName("li").length;
        if (num !== 0) element.firstChild.nodeValue += " (" + num + ")";

        let nextlist = element.querySelector("ul:first-child");
        if (nextlist) addItemCount(nextlist);
        console.log(nextlist);
    });
}