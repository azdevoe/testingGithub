let todo = document.querySelector('#todoItem');
let form = document.querySelector('.form');
let display = document.querySelector('.display');
console.log(form);
let arr = []
form.addEventListener('submit',(e)=>{

    e.preventDefault()
            display.innerHTML = ''

    let todoValue  = todo.value
    console.log(todoValue);
    arr.push(todoValue)
    console.log(arr);
    rerender()
    
    todo.value = ''
})

function rerender(){
    display.innerHTML = ''
    for(let i=0; i<arr.length; i++){
        let newDiv = document.createElement('div');
        let head = document.createElement('h1')
        let button = document.createElement('button')
        newDiv.appendChild(head)
        newDiv.appendChild(button)
        button.innerText = 'delete'
        head.innerText = arr[i]
        display.appendChild(newDiv)



        button.addEventListener('click',()=>{
        arr.splice(i,1)

        rerender()
        })
    }
}


