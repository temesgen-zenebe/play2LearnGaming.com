$(document).ready(function() {
    const sender_name = document.querySelector("#id_full_name")
    const emailTo = document.querySelector('#id_email')
    const user_name = document.querySelector(".user_name")
    const user_email = document.querySelector(".user_email")
    
    const ownerButton1 = document.querySelector(".ownerButton1")
    const ownerButton2 = document.querySelector(".ownerButton2")
    const ownerButton3 = document.querySelector(".ownerButton3")
    const ownerButton4 = document.querySelector(".ownerButton4")
    const ownerButton5 = document.querySelector(".ownerButton5")
    const ownerEmailTitle = document.querySelector('.ownerEmailTitle') 
    
    ownerButton1.addEventListener("click", () => myFunction(ownerButton1.value));
    ownerButton2.addEventListener("click", () => myFunction(ownerButton2.value));
    ownerButton3.addEventListener("click", () => myFunction(ownerButton3.value));
    ownerButton4.addEventListener("click", () => myFunction(ownerButton4.value));
    ownerButton5.addEventListener("click", () => myFunction(ownerButton5.value));

    function myFunction(n){
      //console.log(n)
      if(user_email){ emailTo.value = user_email.innerHTML;}
      if(user_name){sender_name.value = user_name.innerHTML;}
      
      switch (n) {
        case "1":
          ownerEmailTitle.innerHTML = document.querySelector(".ownerName1").innerHTML; 
          break;
        case "2":
          ownerEmailTitle.innerHTML = document.querySelector(".ownerName2").innerHTML ;
          break;
        case "3":
          ownerEmailTitle.innerHTML = document.querySelector(".ownerName3").innerHTML 
          break;
        case "4":
          ownerEmailTitle.innerHTML = document.querySelector(".ownerName4").innerHTML 
          break;
        case  "5":
          ownerEmailTitle.innerHTML = document.querySelector(".ownerName5").innerHTML 
        }
    }
});