let counter = 0;
function count(){
    counter = counter + 1;
    document.querySelector('h1').innerHTML = counter;

    if (counter%10 === 0){
        alert(`Count is now ${counter}`)
    }
   //<!--- alert(counter); --->
}

//Event listener
document.addEventListener('DOMContentLoaded',function(){
    //Instead of calling count function in body
document.querySelector('button').onclick = count;
});