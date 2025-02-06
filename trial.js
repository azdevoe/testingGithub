let form = document.getElementById('form');
let todoItem = document.getElementById('todoItem');
let btn = document.getElementById('btn');
let display = document.querySelector('.display')
let todoValue = todoItem.value;
let arr = []



btn.addEventListener('click', (e)=>{
    e.preventDefault();

    arr.push(todoValue)
    console.log(arr);
    

})


Student 1: Name = "Alice", Score = 85.5

Student 2: Name = "Bob", Score = 72.0

Student 3: Name = "Charlie", Score = 90.0

Student 4: Name = "scott", Score = 64.9

how would it handle this
