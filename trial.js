let form = document.getElementById('form');
let todoItem = document.getElementById('todoItem');

let display = document.querySelector('.display')
let resetForm = document.getElementById('resetForm');
let reset = document.getElementById('reset');
let arr = []



form.addEventListener('submit', (e)=>{
    e.preventDefault();
    display.innerHTML = ''
    let todoValue = todoItem.value;

    console.log(todoValue);

    arr.push(todoValue)
    add()
   
    todoItem.value
})

function add(){
    display.innerHTML =''
     for(let i=0; i<arr.length; i++){
        let container = document.createElement('div');
        let hh = document.createElement('h1')
        let vh = document.createElement('span')
        let btn = document.createElement('button')
        let update = document.createElement('button')
        btn.innerText = 'delete'
        update.innerText = 'change task'

        container.appendChild(hh)
                hh.appendChild(vh)

                hh.appendChild(btn)
                hh.appendChild(update)
                vh.innerText = arr[i]

        display.appendChild(container)

        btn.addEventListener('click', function (){
            arr.splice(i, 1)

            add()
            
        
        })

        update.addEventListener('click', function (){
                resetForm.style.display = 'inline'
                let reset = document.createElement('form')
                let labe = document.createElement('label')
                

                arr[i] = 'reset'
                add()
                console.log(arr);
                
        })

    }


}
