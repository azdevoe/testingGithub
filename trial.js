let form = document.getElementById('form');
let todoItem = document.getElementById('todoItem');
let display = document.querySelector('.display');
let resetForm = document.getElementById('resetForm');
let resetInput = document.getElementById('reset');
let arr = [];
let updateIndex = null; // To store the index of the task being updated

// Add task
form.addEventListener('submit', (e) => {
    e.preventDefault();
    let todoValue = todoItem.value.trim();

    if (todoValue !== "") {
        arr.push(todoValue);
        add();
        todoItem.value = ""; // Clear the input field
    }
});

// Update task
resetForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let resetValue = resetInput.value.trim();

    if (resetValue !== "" && updateIndex !== null) {
        arr[updateIndex] = resetValue; // Update the task in the array
        add(); // Re-render the list
        resetForm.style.display = 'none'; // Hide the reset form
        resetInput.value = ""; // Clear the input field
        updateIndex = null; // Reset the update index
    }
});

// Render the list
function add() {
    display.innerHTML = ''; // Clear the display before re-rendering

    for (let i = 0; i < arr.length; i++) {
        let container = document.createElement('div');
        let hh = document.createElement('h1');
        let vh = document.createElement('span');
        let deleteBtn = document.createElement('button');
        let updateBtn = document.createElement('button');

        vh.innerText = arr[i];
        deleteBtn.innerText = 'Delete';
        updateBtn.innerText = 'Update';

        container.appendChild(hh);
        hh.appendChild(vh);
        hh.appendChild(deleteBtn);
        hh.appendChild(updateBtn);
        display.appendChild(container);

        // Delete task
        deleteBtn.addEventListener('click', () => {
            arr.splice(i, 1); // Remove the task from the array
            add(); // Re-render the list
        });

        // Show update form
        updateBtn.addEventListener('click', () => {
            resetForm.style.display = 'inline'; // Show the reset form
            resetInput.value = arr[i]; // Pre-fill the input with the current task
            updateIndex = i; // Store the index of the task being updated
        });
    }
}