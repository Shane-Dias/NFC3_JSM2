const wrapper=document.querySelector(".wrapper");
const loginlink=document.querySelector(".LoginLink");
const registerlink=document.querySelector(".RegisterLink");
const loginbutton=document.querySelector(".btnLogin-popup");
const crossbtn1=document.querySelector(".icon-close")
registerlink.addEventListener('click', () => {
    wrapper.classList.add('active')
});

loginlink.addEventListener('click', () => {
    wrapper.classList.remove('active')
});

loginbutton.addEventListener('click',  () => {
    wrapper.classList.add('popup')
});

crossbtn1.addEventListener('click', () => {
    wrapper.classList.remove('popup')    
    wrapper.classList.remove('active')
});